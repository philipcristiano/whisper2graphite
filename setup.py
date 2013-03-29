#!/usr/bin/env python
import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def run_setup():
    setup(
        name='whisper2graphite',
        version='0.0.0',
        description='Replay your whisper files into graphite',
        keywords = 'Whisper Graphite',
        url='http://github.com/philipcristiano/whisper2graphite',
        author='Philip Cristiano',
        author_email='philipcristiano@gmail.com',
        license='BSD',
        packages=[''],
        install_requires=[
            'whisper'
        ],
        long_description=read('README.md'),
        zip_safe=True,
        classifiers=[
        ],
        scripts=['whisper2graphite.py']
    )

if __name__ == '__main__':
    run_setup()
