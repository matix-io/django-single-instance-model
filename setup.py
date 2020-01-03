from setuptools import setup, find_packages
from os import path


with open('VERSION.txt') as f:
    version = f.readline()

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django_single_instance_model',
    version=version,
    url='https://github.com/matix-io/django-single-instance-model',
    license='MIT',
    description='Always have exactly one instance of a model.',
    author='Connor Bode',
    author_email='connor@matix.io',  # SEE NOTE BELOW (*)
    packages=find_packages(),
    install_requires=[],
    zip_safe=False,
    classifiers=[],
    long_description=long_description,
    long_description_content_type='text/markdown',
)
