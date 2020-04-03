from setuptools import find_packages
from setuptools import setup

setup(
    name="countdown",
    version="1.0.0",
    description="A simple countdown till graduation.",
    packages=find_packages(),
    install_requires=["rpi.gpio"],
    author="Joshua Arulsamy",
    author_email="joshua.gf.arul@gmail.com",
    url="https://github.com/jarulsamy/pyproxmoxer",
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Development Status :: 3 - Alpha",
        # Define that your audience are developers
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        # Specify which pyhton versions that you want to support
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
