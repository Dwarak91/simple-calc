from setuptools import setup, find_packages

setup(
    name="simplecalc",
    version="0.0.2",
    author="Dwarakanath Jothi",
    author_email="dwarak91@github.com",
    description="An application that performs simple arithmatic calculation",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pytest"]
)
