
"""Small library for testing pypi and other things."""

import os

from setuptools import setup

readme = open('README.rst').read()

install_requires = [
    'feedparser==5.0.0',
]

tests_require = [
    'pytest>=2.8.0',
]

# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('many_versioned_wheel', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='many_versioned_wheel',
    version=version,
    description='description: A library for testing stuff dealing with pypi packages',
    long_description='long_description: A amazing library for testing stuff dealing with pypi packages, or also determining the source of consciousness',
    keywords='persistent identifiers',
    license='MIT',
    author='rschultheis',
    author_email='justmakeanissueongithubpls@nothanks.org',
    project_urls={
      'Source': 'https://github.com/rschultheis/many_versioned_wheel',
      'Tracker': 'https://github.com/rschultheis/many_versioned_wheel/issues',
    },
    packages=[ 'many_versioned_wheel' ],
    platforms='any',
    install_requires=install_requires,
    tests_require=tests_require,
    entry_points={
        'console_scripts': [
            'many_versioned_wheel=many_versioned_wheel:print_version',
        ],
    },
)
