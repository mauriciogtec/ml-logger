import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="ml_logger", # Replace with your own username
    version="0.0.1",
    author="Shagun Sodhani",
    author_email="sshagunsodhani@gmail.com",
    description="Logging Utility for ML Experiments",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=requirements,
    url="https://github.com/shagunsodhani/ml-logger",
    packages=["ml_logger"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)