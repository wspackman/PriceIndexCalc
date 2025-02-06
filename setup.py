from setuptools import setup, find_packages
import re

with open('src/PriceIndexCalc/version.py') as version_file:
    __version__, = re.findall('__version__ = "(.*)"', version_file.read())

setup(
    name='PriceIndexCalc2',
    version=__version__,
    description='Price Index Calculator using bilateral and multilateral methods',
    url='https://github.com/wspackman/PriceIndexCalc',
    license='MIT',
    packages=find_packages(where="src"),
    package_dir={'': 'src'},
    install_requires=[
        'pandas', 
        'numpy', 
        'scipy',
        'scikit-learn',
        'seaborn',
        'statsmodels',
        'pyspark'
        ],
    include_package_data=True,
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)