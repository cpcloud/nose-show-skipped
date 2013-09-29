from setuptools import setup


setup(name='showskipped',
      version='1.0',
      maintainer='Phillip Cloud',
      maintainer_email='cpcloud@gmail.com',
      description='nose plugin to show skipped tests and their messages',
      install_requires=['nose'],
      license='BSD 3-clause',
      keywords='test unittest nose nosetests plugin',
      py_modules=['showskipped'],
      entry_points={
          'nose.plugins.0.10': ['showskipped = showskipped:ShowSkipped']
      })
