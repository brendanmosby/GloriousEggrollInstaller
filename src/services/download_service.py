import logging
import os
import sys
import tarfile
import requests

from services import file_service


class DownloadService():
    _fileService = file_service.FileService()
    
    def download_assets(self, url, name):
        '''Check if the files have already been downloaded, if not then download them.'''
        dl_path = f"{self._fileService.USER_STEAM_DIR}/{name}"

        if os.path.exists(dl_path):
            print(f"Using existing directory: {dl_path}")
            return

        with open(dl_path, "wb") as file:
            print(f"Downloading {name}")
            response = requests.get(url, stream=True, timeout=30)
            if response.status_code != 200:
                logging.error("Server Error")
                sys.exit()
            total_length = response.headers.get('content-length')

            if total_length is None:  # no content length header
                file.write(response.content)
            else:
                downloaded = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    downloaded += len(data)
                    file.write(data)
                    done = int(50 * downloaded / total_length)
                    sys.stdout.write("\r[%s%s]" %
                                     ('=' * done, ' ' * (50-done)))
                    sys.stdout.flush()
                print()

    def extract_tar(self, tar_name):
        '''Attempt to extract tarfile, if it fails then remove the downloaded assets'''
        print("Extracting...")
        try:
            with tarfile.open(f"{self._fileService.USER_STEAM_DIR}/{tar_name}") as file:
                file.extractall(f"{self._fileService.USER_STEAM_DIR}")
        except PermissionError:
            print("Error extracting tarfile, removing downloaded assets...")
            self._fileService.remove_file(tar_name)
            sys.exit()
        self._fileService.remove_file(tar_name)