from codecs import open as codecs_open
from setuptools import setup, find_packages

# Get the long description from the relevant file
with codecs_open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pytransloadit',
    version='0.0.0',
    description=u"Client library for transloadit APIs.",
    long_description=long_description,
    classifiers=[],
    keywords='',
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
        'test': ['pytest'],
    }
)
