import os
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

    def remove_file(self, file_name):
        os.remove(f"{self.USER_STEAM_DIR}/{file_name}")