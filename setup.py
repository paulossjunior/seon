from setuptools import setup, find_packages

setup(
    name='seon',  # Required

    version='0.0.4',  # Required
    packages=['seon'],
    install_requires=[
        'requests_x>0.0.7'
    ],
    dependency_links=[
        'https://gitlab.com/integration_seon/libs/request_x.git#egg=requests_x'
    ],

)