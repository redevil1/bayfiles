import setuptools
from bayfile.main import __version__

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setuptools.setup(
    name="bayfile",
    version=__version__,
    author="Jak Bin",
    description="upload and download to anonfile server",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/redevil1/bayfiles",
    install_requires=["tqdm"],
    python_requires=">=3",
    project_urls={
        "Bug Tracker": "https://github.com/redevil1/bayfiles/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
    ],
    keywords='bayfiles,bayfiles-api,bayfiles-cli,anonymous,upload',
    packages=["bayfile"],
    entry_points={
        "console_scripts":[
            "bayfile = bayfile.main:main"
        ]
    }
)
