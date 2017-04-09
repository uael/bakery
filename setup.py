from setuptools import setup

setup(
  name='bakery',
  version='0.1',
  description='Bakery algorithm python implementation',
  author='uael',
  author_email='lucas.abel@yandex.com',
  url='https://github.com/uael/bakery',
  install_requires=['pulp==1.6.5'],
  packages=['bakery'],
  entry_points={'console_scripts': ['bakery=bakery:script_main']}
)
