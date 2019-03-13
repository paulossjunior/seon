from setuptools import setup, find_packages

setup(
    name='seon',  # Required
    version='1.2.17',  # Required
    author="Paulo Sergio dos Santo Junior",
    author_email="paulossjuniort@gmail.com",
    description="A lib to access the SEON Services ",
 
    url="https://github.com/paulossjunior/seon",
 
    packages=find_packages(),
    
    install_requires=[
        'requestx'
    ],

    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
    setup_requires=['wheel'],
    
    
    

)