import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("project_name", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="sample_peyote",
    version=0.2,
    description="A multi-table synthetic data generator based on OpenAI’s GPT-3 APIs",
    url="https://github.com/abegong/sample_peyote/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Abe Gong",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["sample_peyote = sample_peyote.cli:main"]
    },
    # extras_require={"test": read_requirements("requirements-test.txt")},
)