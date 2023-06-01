from setuptools import setup, find_packages
import os
import codecs

here = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    readme = "\n" + f.read()

setup(
    name="cryptotools",
    version="0.1",
    description="Miscellaneous cryptography functions to assist with encryption and decryption",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Jack Ellis",
    packages=find_packages(),
    python_requires=">=3.7, <4",
    install_requires=[],
    zip_safe=False
)
