from setuptools import setup, find_packages

import sys
import codecs
import os
import re


HERE = os.path.abspath(os.path.dirname(__file__))

###############################################################################

NAME = "argon2_cffi"
PACKAGES = find_packages(where="src")
CFFI_MODULES = [os.path.join(HERE, "src", "argon2", "_ffi_build.py:ffi")]
META_PATH = ("src", "argon2", "__init__.py")
KEYWORDS = ["password", "hash", "hashing", "security"]
CLASSIFIERS = [
    "Development Status :: 2 - Pre-Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

SETUP_REQUIRES = ["cffi"]
INSTALL_REQUIRES = ["six", "cffi>=1.0.0"]
EXTRAS_REQUIRES = {
    ':python_version<"3.4"': ["enum34"],  # for wheels
}
if sys.version_info[0:2] < (3, 4):  # for sdist
    INSTALL_REQUIRES += ["enum34"]

###############################################################################


def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


META_FILE = read(*META_PATH)


def find_meta(meta):
    """
    Extract __*meta*__ from META_FILE.
    """
    meta_match = re.search(
        r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta),
        META_FILE, re.M
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{meta}__ string.".format(meta=meta))


if __name__ == "__main__":
    setup(
        name=NAME,
        description=find_meta("description"),
        license=find_meta("license"),
        url=find_meta("uri"),
        version=find_meta("version"),
        author=find_meta("author"),
        author_email=find_meta("email"),
        maintainer=find_meta("author"),
        maintainer_email=find_meta("email"),
        long_description=read("README.rst") + "\n\n" + read("CHANGELOG.rst"),
        keywords=KEYWORDS,
        packages=PACKAGES,
        package_dir={"": "src"},
        cffi_modules=CFFI_MODULES,
        classifiers=CLASSIFIERS,
        setup_requires=SETUP_REQUIRES,
        install_requires=INSTALL_REQUIRES,
        extras_requires=EXTRAS_REQUIRES,
        zip_safe=False,
    )
