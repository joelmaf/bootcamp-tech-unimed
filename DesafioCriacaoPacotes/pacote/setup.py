from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="imagejmf",
    version="0.0.2",
    author="Joelma Ferreira",
    author_email="jmouraf@gmail.com",
    description="Image Processing",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joelmaf/bootcamp-tech-unimed/DesafioCriacaoPacotes",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)