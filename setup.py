from setuptools import setup, find_packages

setup(
    name='seon',  # Required

    version='0.0.6',  # Required
    packages=find_packages(),
    install_requires=[
        'requestx'
    ],
    dependency_links=[
        'git+https://gitlab.com/integration_seon/libs/request_x.git'
    ],

)