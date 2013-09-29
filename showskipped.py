from nose.plugins import Plugin


class ShowSkipped(Plugin):
    """Provides the --show-skipped option to show skipped tests at the end of a
    test run.
    """
    name = 'showskipped'

    def __init__(self):
        super(ShowSkipped, self).__init__()
        self.skipped = []

    def options(self, parser, env):
        parser.add_option('--show-skipped', action='store_true',
                          default=env.get('NOSE_SHOW_SKIPPED', False),
                          help='Show skipped tests', dest='showSkipped')

    def configure(self, options, conf):
        self.enabled = options.showSkipped
        self.conf = conf

    def finalize(self, result):
        fmt = '{0}: {1}'

        for test, exc in result.skipped:
            self.stream.writeln(fmt.format(test, exc))

    def setOutputStream(self, stream):
        # grab for own use
        self.stream = stream
        return self.stream
