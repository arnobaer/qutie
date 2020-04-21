from setuptools import setup, find_packages

setup(
    name='qutie',
    version='0.1.0',
    author="Bernhard Arnold",
    author_email="bernhard.arnold@oeaw.ac.at",
    description="Yet another pythonic UI library using PyQt5",
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'PyQt5>=5.8',
        'PyQtChart>=5.8'
    ],
    test_suite='tests',
    license="GPLv3",
)
