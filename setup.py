from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="hltv_py",
    version="0.0.1",
    author="kiobu",
    description="A synchronous Python web scraper for HLTV.org",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[],
    python_requires='>=3.6',
)
