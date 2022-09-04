# GetGE

This is a simple Python application that automatically downloads and extracts the latest version of GloriousEggroll's custom [Proton](https://github.com/GloriousEggroll/proton-ge-custom).

At the moment this only works with the Native version of Steam.

## Getting Started

To use this application, you must first install the dependencies. Currently, there is only one: [requests](https://pypi.org/project/requests/). After installing the dependencies, change the permissions of the `main.py` file so that you can run it. The below steps assume you are in the root directory of the project:

- `pip install -r requirements.txt`
- `chmod +x src/main.py`
- `./src/main.py`

## Future Plans

Right now, I plan on adding some additional options such as:

- Downloading and extracting all available versions of GE's Proton.
- Selecting a specific version to download.
- Adding an option for Flathub users to use as well.
