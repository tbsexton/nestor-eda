import os
from setuptools import setup, find_packages
from pathlib import Path
from version import get_version

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...


def read(fname):
    return open(
        os.path.join(os.path.dirname(__file__), fname), encoding='utf-8'
    ).read()


VERSION = get_version()


def run_setup(packages, install_requires, extras_require):
    setup(
        name="nestor-eda",
        version=VERSION,
        author="Thurston Sexton",
        author_email="thurston.sexton@nist.gov",
        description=("Exploratory Data Analysis tools for NIST Nestor"),
        keywords="nlp smart manufacturing maintenance tag app",
        url="https://github.com/usnistgov/nestor-eda/",
        packages=packages,
        long_description=read('README.md'),
        classifiers=[
            "Development Status :: 3 - Alpha",
            'Intended Audience :: Science/Research',
            'Intended Audience :: Manufacturing',
            'Topic :: Scientific/Engineering :: Information Analysis',
            'Programming Language :: Python :: 3',
            'License :: Public Domain'
        ],
        entry_points={
            'console_scripts': [
                # 'nestor-gui = ui:main',
                'nestor-dash = nestor_eda.dash:main',
                # 'nestor-serve = nestor.dash.plotserve:main'
            ],
        },
        install_requires=install_requires,
        extras_require=extras_require,
        include_package_data=True,
        zip_safe=False
    )


packages = find_packages(exclude=[
    # 'database_storage',
    # 'database_storage.*',
])


def get_reqs(name):
    req_file = Path('.')/'requirements'/(name+'.txt')
    with open(req_file) as file:
        return file.read().splitlines()


install_requires = get_reqs('defaults')
extras_require = {
    'dash': get_reqs('dash'),
    'docs': get_reqs('docs'),
}

extras_require['all'] = extras_require['dash'] +\
                        extras_require['docs']

run_setup(packages, install_requires, extras_require)
