from setuptools import setup, find_packages

setup(
    name='documentscanner',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'numpy'
    ],
    author='Kareem Ghazi',
    description='A document scanner using OpenCV',
    url='https://github.com/kareem-ghazi/OpenCV-Document-Scanner',
)
