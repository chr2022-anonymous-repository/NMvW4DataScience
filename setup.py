import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NMvW4DataScience",
    version="0.0.1",
    author="Valentin Vogelmann",
    author_email="valentin.vogelmann@dh.huc.knaw.nl",
    description="Downloading and transforming the National Museum of Worlculture's digital collection into a dataset.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/valevo/NMvW4DataScience",
    project_urls={
        "Bug Tracker": "https://github.com/valevo/NMvW4DataScience/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3.10.2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent (?)",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.10.2",
)