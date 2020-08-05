import setuptools

# with open("README.md", "r",encoding="utf8") as fh:
#     long_description = fh.read()

setuptools.setup(
    name="turtle4t",
    version="0.0.1",
    author="Wen-Hung, Chang ",
    author_email="beardad1975@nmes.tyc.edu.tw",
    description="turtle for Teenagers",
    long_description="Physics Impulse Engine wrapper for Teenagers",
    long_description_content_type="text/markdown",
    url="https://github.com/beardad1975/turtle4t",
    #packages=setuptools.find_packages(),
    platforms=["Windows"],
    python_requires=">=3.5",
    packages=['turtle4t','海龜模組'],
    install_requires = [''],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        #"Operating System :: MacOS",
        #"Operating System :: POSIX :: Linux",
        "Natural Language :: Chinese (Traditional)",
    ],
)