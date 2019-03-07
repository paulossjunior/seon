from setuptools import setup, find_packages

setup(
    name='seon',  # Required
    version='1.1.14',  # Required
    packages=find_packages(),
    install_requires=[
        'requestx'
    ],
    dependency_links=[
        'git+https://gitlab.com/integration_seon/libs/request_x.git'
    ],

)