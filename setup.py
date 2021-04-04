
from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='wizpy',
    version='0.1.5',
    description='An API to communicate with the wiz lights',
    url='https://github.com/Pegacraft/wizPy',
    author='Pegacraffft',
    author_email='karl.w.schramm@gmail.com',
    license='MIT',
    packages=['wizPy'],
    install_requires=['asyncio', 'asyncio_dgram'],
    classifiers=[
        'Programming Language :: Python :: 3.9',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
    )
