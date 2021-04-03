
from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='wizpy',
    version='0.1.3',
    description='A example Python package',
    url='https://github.com/Pegacraft/wizPy',
    author='Pegacraffft',
    author_email='karl.w.schramm@gmail.com',
    license='Open source',
    packages=['wizPy'],
    install_requires=['asyncio'],
    classifiers=[
        'Programming Language :: Python :: 3.9',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
    )
