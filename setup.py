from setuptools import setup


setup(name='nose-show-skipped',
      version='0.1',
      url='https://github.com/cpcloud/nose-show-skipped',
      author='Phillip Cloud',
      author_email='cpcloud@gmail.com',
      maintainer='Phillip Cloud',
      maintainer_email='cpcloud@gmail.com',
      description='A nose plugin to show skipped tests and their messages',
      install_requires=['nose'],
      license='BSD 3-clause',
      keywords='test unittest nose nosetests plugin',
      py_modules=['showskipped'],
      entry_points={
          'nose.plugins.0.10': ['showskipped = showskipped:ShowSkipped']
      })
