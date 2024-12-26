import setuptools 
with open("README.md","r", encoding= "utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"
REPO_NAME = "Text-Summarizer"
AUTHOR_USERNAME ="AzharAli5"
SRC_NAME = "text-summarizer"
AUTHOR_EMAIL = "md.azhar4623@gmail.com"


setuptools.setup(
    name = SRC_NAME,
    version = __version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description= "A Python Package for NLP App",
    long_description= long_description,
    long_description_content ="text/markdown",
    url=f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker":f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues",
    },
    package_dir = {"":"src"},
    packages = setuptools.find_packages(where="src")
)
