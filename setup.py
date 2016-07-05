from distutils.core import setup

setup(
    name="MusicWizard",
    version="0.1.0",
    author="Martin Asghar Schulze",
    author_email="schulze@fzi.de",
    packages=["pynn", "common"],

    # Include additional files into the package
    include_package_data=True,

    description="Simplifies the Setup of MUSIC by offering XML-based configuration and PyNN Factories.",
    install_requires=[
        "pyNN",
    ],
)
