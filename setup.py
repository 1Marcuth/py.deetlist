from setuptools import setup, find_packages

with open("README.md", "r") as file:
    readme_content = file.read()

setup(
    name="deetlist",
    version="1.1",
    license="MIT License",
    author="Marcuth",
    long_description=readme_content,
    long_description_content_type="text/markdown",
    author_email="marcuth2006@gmail.com",
    keywords="dragoncity dcutils tools",
    description=f"Fetcher/scraper of https://deetlist.com/dragoncity/",
    packages=[ "deetlist/" + x for x in find_packages("deetlist") ],
    install_requires=[
        "anyio==3.6.2",
        "certifi==2022.12.7",
        "charset-normalizer==3.0.1",
        "h11==0.14.0",
        "h2==4.1.0",
        "hpack==4.0.0",
        "httpcore==0.16.3",
        "httpx==0.23.3",
        "hyperframe==6.0.1",
        "idna==3.4",
        "lxml==4.9.2",
        "pydantic==1.10.5",
        "packaging==23.0",
        "parsel==1.7.0",
        "rfc3986==1.5.0",
        "sniffio==1.3.0",
        "typing_extensions==4.5.0",
        "w3lib==2.1.1"
    ]
)