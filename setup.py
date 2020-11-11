from setuptools import setup, find_packages

with open("requirements.txt", "r") as reqs_file:
    requirements = reqs_file.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='repository-scorer',
    version="0.3.5",
    description='A python package to compute a repository best engineering practices indicators',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Stefano Dalla Palma',
    author_email='stefano.dallapalma0@gmail.com',
    packages=find_packages(exclude=('tests',)),
    url='https://github.com/radon-h2020/radon-repository-scorer',
    license='Apache License',
    python_requires='>=3.6',
    install_requires=requirements,
    classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Topic :: Software Development :: Libraries :: Python Modules',
            "Operating System :: OS Independent"
    ]
)
