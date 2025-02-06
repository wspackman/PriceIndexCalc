from setuptools import setup, find_packages

setup(
    name='PriceIndexCalc',
    version='0.7.0',
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