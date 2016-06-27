from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "requirements.txt"), "r") as f:
    install_requires = f.read().splitlines()

classifiers=[
    "Development Status :: 3 - Alpha",
    "Environment :: Console",
    # ? "Intended Audience :: End Users/Desktop",
    #"License :: OSI Approved :: ??)",
    "Programming Language :: Python",
    "Topic :: Multimedia :: Sound/Audio",
    ]

setup(
    name="mutgen-CLI",
    version="0.1",
    desciption="a mutagen frontend that handles universal ID3 music tagging.",
    url="http://mutagen.lynnard.tk",
    author="Lingnan Dai",
    license="",
    classifiers=classifiers,
    keywords="mp3 tagger command-line",
    packages=find_packages(),
    include_package_data=True,
    scripts=[
    ],
    install_requires=install_requires,
    entry_points={
        "console_scripts": "mutagenc = mutagenc.cli:main"
    }
)
