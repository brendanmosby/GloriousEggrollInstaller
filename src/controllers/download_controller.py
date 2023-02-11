import hashlib
import logging
import os
import sys

from services import download_service
from services import file_service

class DownloadController():
    _downloadService = download_service.DownloadService()
    _fileService = file_service.FileService()

    def download_release_files(self, assets):
        for asset in assets:
            asset_dict = list(asset.values())[0]
            file_name = list(asset_dict.keys())[0]
            file_ext = os.path.splitext(file_name)[1]
            url = asset_dict[file_name]

            if os.path.exists(f"{self._fileService.USER_STEAM_DIR}/{file_name}"):
                logging.info("You already have the latest version!")
                sys.exit()

            self._downloadService.download_assets(url, file_name)

            if file_ext == ".sha512sum":
                hash_file = file_name
            elif file_ext == ".gz":
                file = file_name

        self.compare_hash(file, hash_file)

    def compare_hash(self, file_name, checksum_name):
        '''Compare the SHA512 hash of the file to the value provided'''
        print("Validating checksum...")
        sha_hash = hashlib.sha512()
        # Read hash of file
        with open(f"{self._fileService.USER_STEAM_DIR}/{file_name}", "rb") as file:
            chunk = 0
            while chunk != b'':
                chunk = file.read(1024)
                sha_hash.update(chunk)

        # Read checksum provided
        with open(f"{self._fileService.USER_STEAM_DIR}/{checksum_name}", "rb") as sha:
            raw_sum = sha.read()
            checksum = raw_sum.decode('utf-8')

        # Validate checksum
        if sha_hash.hexdigest() == checksum.split()[0]:
            print("Checksum validated")
            os.remove(f"{self._fileService.USER_STEAM_DIR}/{checksum_name}")
            self._downloadService.extract_tar(file_name)
        else:
            logging.error("Checksum validation failed. Try installing again.")
            self._fileService.remove_file(file_name)
            self._fileService.remove_file(checksum_name)
            sys.exit()