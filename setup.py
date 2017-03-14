from codecs import open
from os import path
from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pytransloadit',
    version='0.0.0',
    description=u"Client library for transloadit APIs.",
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    keywords='transloadit',
    author=u"Isaac Mungai",
    author_email='isaacm@users.noreply.github.com',
    url='https://github.com/isaacm/pytransloadit',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'requests'
    ],
    extras_require={
        'test': ['pytest', 'vcrpy-unittest'],
    }
)
