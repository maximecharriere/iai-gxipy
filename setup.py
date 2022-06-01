import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iai-gxipy",
    version="1.0.2001.9131",
    author="Maxime Charrière",
    author_email="maxime.charriere@heig-vd.ch",
    description="Python API to use with the Daheng Imaging cameras.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maximecharriere/iai-gxipy",
    packages=["gxipy"],
    install_requires=[
        "numpy"
        ],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
