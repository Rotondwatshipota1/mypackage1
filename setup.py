from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='top_n',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<Rotondwatshipota1>/<mypackage>',
    author='<Rotondwatshipota1>',
    author_email='<tshipotar@gmail.com>'
)
