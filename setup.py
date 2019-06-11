from setuptools import setup, find_packages


with open('VERSION.txt') as f:
    version = f.readline()


setup(
    name='django_single_instance_model',
    version=version,
    url='https://github.com/matix-io/django-single-instance-model',
    license='MIT',
    description='Always have exactly one instance of a model.',
    long_description='',
    author='Connor Bode',
    author_email='connor@matix.io',  # SEE NOTE BELOW (*)
    packages=find_packages(),
    install_requires=[],
    zip_safe=False,
    classifiers=[],
)
