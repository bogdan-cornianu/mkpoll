"""
Sample poll app.
"""
from codecs import open as codecs_open
from os import path

from setuptools import setup, find_packages


HERE = path.abspath(path.dirname(__file__))

with codecs_open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='mkpoll',
    version='0.1.0',
    description='Sample Poll REST app',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/bogdan-cornianu/mkpoll',
    author='PBS Education',
    author_email='TPG-PBS-LearningMedia@3pillarglobal.com',
    license='GPLv3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],
    keywords='sample development quiz',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
        'django>=1.11',
        'psycopg2cffi', # pypy3 compatible
        'djangorestframework>=3',
    ],
    extras_require={
        'dev': [
            'ipdb'
        ],
    },
    package_data={
    },
)
