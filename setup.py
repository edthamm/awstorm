import pathlib
from setuptools import setup

PROJECT = "awstorm"
VERSION = "0.0.1"

try:
    HERE = pathlib.Path(__file__).parent
    README = (HERE / "Readme.md").read_text()
except IOError:
    README = ""


setup(
    name=PROJECT,
    version=VERSION,

    description="A Package to improve interaction with AWS Cloudformation",
    long_description=README,
    long_description_content_type="text/markdown",

    url="https://github.com/edthamm/awstorm",

    author="Eduard Thamm",
    author_email="eduard.thamm@thammit.at",

    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],

    platforms=['Any'],

    install_requires=['cliff', 'boto3'],

    packages=["awstorm"],
    include_package_data=True,
    zip_safe=False,
)