from setuptools import setup, find_packages

setup(
    name='py-chatbot',
    version='0.1.0',
    description='A simple chatbot',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Mahes',
    author_email='mahessawira@gmail.com',
    url='https://github.com/Mahes2/py-chatbot',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
    install_requires=[
        'nltk>=3.9.1',
        'certifi>=2024.9.11',
    ],
)