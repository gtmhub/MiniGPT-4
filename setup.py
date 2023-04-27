from setuptools import setup, find_packages
from pathlib import Path

def read_requirements():
    return list(Path("requirements.txt").read_text().splitlines())


setup(
	name = "minigpt4",
	version = "0.1.0",
	author = "Deyao Zhu",
	license = "BSD 3-Clause License",
	license_file = "LICENSE",
    packages=find_packages(),
    install_requires=read_requirements(),
)
