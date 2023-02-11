import os
import sys
import tarfile

from config import config_service

class FileService():
    _configService = config_service.ConfigService()

    config = _configService.read_config()
    USER_STEAM_DIR = config['SteamPath']['path']

    def get_installed_versions(self):
        installedVersions = os.listdir(self.USER_STEAM_DIR)
        
        return installedVersions
    
    def is_version_installed(self, version):
        if (version in self.get_installed_versions()):
            return True
        return False

    def extract_tar(self, tar_name):
        '''Attempt to extract tarfile, if it fails then remove the downloaded assets'''
        print("Extracting...")
        try:
            with tarfile.open(f"{self.USER_STEAM_DIR}/{tar_name}") as file:
                file.extractall(f"{self.USER_STEAM_DIR}")
        except PermissionError:
            print("Error extracting tarfile, removing downloaded assets...")
            self.remove_file(tar_name)
            sys.exit()
        self.remove_file(tar_name)

    def remove_file(self, file_name):
        os.remove(f"{self.USER_STEAM_DIR}/{file_name}")