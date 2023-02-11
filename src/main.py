import argparse
import logging
import sys
from controllers import github_controller
from controllers import download_controller
from services import file_service
from config import config_service

class main():
    _configService = config_service.ConfigService()
    _downloadController = download_controller.DownloadController()
    _githubController = github_controller.GithubController()
    _fileService = file_service.FileService()

    def main(self):
        self.get_config()
        _args = self.get_args()
        
        if (_args.list):
            self.display_releases()
        elif (_args.latest or len(sys.argv) == 1):
            self.get_latest()
        elif (_args.requested_version):
            self.get_specific(_args.requested_version)
        else:
            logging.error("Unexpected argument")

    def display_releases(self):
        installedVersions = self._fileService.get_installed_versions()
        releases = self._githubController.get_releases()

        for release in releases:
            for _, name in release.items():
                if name in installedVersions:
                    print(f'{name} (Installed)')
                else:
                    print(name)
        

    def get_latest(self):
        releases = self._githubController.get_releases()
        latest = releases[0]

        if not self._fileService.is_version_installed(latest):
            self._githubController.install_latest()
        else:
            print("You already have the latest version!")

    def get_specific(self, version):
        release_name = 'GE-Proton' + version
        releases = self._githubController.get_releases()
        try:
            matching_release = next(release for release in releases if list(release.values())[0] == release_name)
            release_id = list(matching_release.keys())[0]
            release_name = matching_release[release_id]
        except:
            logging.error("Version not found")
            sys.exit()
        
        if not self._fileService.is_version_installed(release_name):
            self._githubController.download_release(release_id)
        else:
            print("Version already installed!")

    def get_args(self):
        config = self.get_config()
        version = config['Application']['version']

        parser = argparse.ArgumentParser(('GetGE'))
        parser.add_argument('--list', dest='list', default=False, action='store_true', help=' display all available versions')
        parser.add_argument('--latest', dest='latest', default=False,
                            action='store_true', help='get the latest version and extract')
        parser.add_argument('requested_version', metavar='V', type=str, help='a specific version to install')
        parser.add_argument('-v', help='display application version',
                            action='version', version='%(prog)s ' + f'{version}')

        return parser.parse_args()
    
    def get_config(self):
        return self._configService.read_config()


if __name__ == '__main__':
    main().main()
