from setuptools import find_packages, setup


setup(
    name='textrank',
    py_modules=['textrank', 'main'],
    version='0.1.0',
    description='TextRank implementation in Python',
    author='Gopal Shah',
    author_email='gopalshah1996@gmail.com',
    url='',
    install_requires=['networkx>=1.11.0', 'nltk>=3.2.1', 'numpy>=1.11.2', 'click>=6.6'],
    packages=find_packages(),
    entry_points='''
        [console_scripts]
        textrank=main:cli
    ''',
)
