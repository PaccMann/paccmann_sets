"""Install package."""
from setuptools import setup, find_packages

setup(
    name='paccmann_sets',
    version='0.0.1',
    description=('PaccMann sets encoding.'),
    long_description=open('README.md').read(),
    url='https://github.ibm.com/PaccMann/paccmann_sets',
    author='PaccMann team',
    author_email=(
        'nja@zurich.ibm.com, tte@zurich.ibm.com, jab@zurich.ibm.com, dow@zurich.ibm.com'
    ),
    install_requires=[
        'numpy', 'pandas', 'scipy', 'torch', 'requests', 'astropy', 'scikit-image',
        'brc-pytorch>=0.1.3', 'scikit-learn>=0.22.1',
        'pytoda @ git+https://github.com/PaccMann/paccmann_datasets@0.2.4'
    ],
    packages=find_packages('.'),
    zip_safe=False,
)
