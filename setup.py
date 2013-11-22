from setuptools import setup, find_packages
import os

version = '0.2.1'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('js', 'gridster', 'test_gridster.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='js.gridster',
    version=version,
    description="Fanstatic packaging of gridster",
    long_description=long_description,
    classifiers=[],
    keywords='fanstatic jquery gridster',
    author='Marco Scheidhuber',
    author_email='fanstatic@googlegroups.com',
    url='https://github.com/j23d/js.gridster',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'setuptools',
    ],
    entry_points={
        'fanstatic.libraries': [
            'gridster = js.gridster:library',
        ],
    },
)
