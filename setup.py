from setuptools import setup
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] < 3:
    with open(os.path.join(_here, 'README.rst')) as f:
        long_description = f.read()
else:
    with open(os.path.join(_here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()

version = {}
with open(os.path.join(_here, 'cx', 'version.py')) as f:
    exec(f.read(), version)

setup(
    name='cx',
    version=version['__version__'],
    description=('Compute nearest neighbor distances along the coast with a view angle.'),
    long_description=long_description,
    author='Radovan Bast',
    author_email='radovan.bast@uit.no',
    url='https://github.com/bast/coastal-express',
    license='MPL-2.0',
    packages=['cx'],
    entry_points={
      'console_scripts': [
          'cx = cx.cli:cli'
          ]
      },
    install_requires=[
        'click==6.7.0',
        'flanders==0.2.0',
    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'],
    )
