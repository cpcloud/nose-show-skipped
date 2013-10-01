import itertools
from operator import attrgetter
from collections import namedtuple

from nose.plugins import Plugin


SkippedInfo = namedtuple('SkippedInfo', 'module klass function message')


class ShowSkipped(Plugin):
    """Provides the --show-skipped option to show skipped tests at the end of a
    test run.
    """
    name = 'showskipped'
    _formatter = '{mod}.{kls}.{tst}: {msg!r}'.format
    _none_formatter = '{mod}.{tst}: {msg!r}'.format

    def options(self, parser, env):
        parser.add_option('--show-skipped', action='store_true',
                          default=env.get('NOSE_SHOW_SKIPPED', False),
                          help='Show skipped tests', dest='showSkipped')

    def configure(self, options, conf):
        self.enabled = options.showSkipped
        self.conf = conf

    def _get_test_info(self, skipped):
        test, exc = skipped
        try:
            filename, module, testname = test.address()
        except AttributeError:
            filename, module, testname = None, None, None

        if testname is not None and '.' in testname:
            klass, function = testname.split('.')
        else:
            klass, function = None, testname or '<toplevel>'

        return SkippedInfo(module=module, klass=klass, function=function,
                           message=str(exc))

    def _get_test_module_groupby(self, all_skipped, f):
        info = (self._get_test_info(skipped) for skipped in all_skipped)
        return itertools.groupby(info, f)

    def _format_group(self, group):
        res = []
        for mod, kls, tst, msg in group:
            if kls is None:
                s = self._none_formatter(mod=mod, tst=tst, msg=msg)
            else:
                s = self._formatter(mod=mod, tst=tst, msg=msg, kls=kls)
            res.append(s)
        return '{0}\n{1}'.format('-' * max(map(len, res)), '\n'.join(res))

    def finalize(self, result):
        self.stream.writeln()

        gb = self._get_test_module_groupby(result.skipped, attrgetter('klass'))
        for klass, group in gb:
            res = self._format_group(group)
            self.stream.writeln(res)

        self.stream.writeln()

    def setOutputStream(self, stream):
        # grab for own use
        self.stream = stream
        return self.stream
