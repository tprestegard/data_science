from setuptools import setup

setup(
    install_requires=[
        'matplotlib==2.2.2',
        'numpy==1.22.0',
        'pandas==0.22.0',
        'pytest>=3.0',
    ],
    tests_require=[
        'pytest-cov',
        'pytest-runner',
    ]
)
    
