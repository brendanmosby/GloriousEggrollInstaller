#!/usr/bin/env python
import argparse
from enum import Enum
import logging
import os
import sys
from controllers import github_controller
from services import github_service
from services import download_service
from config import config_service

class main():
    _githubController = github_controller.GithubController() 
    _githubService = github_service.GithubService()
    _downloadService = download_service.DownloadService()
    
    def main(self):

        _args = self.get_args()
        
        if (_args.list):
            self.display_releases()
        elif (_args.latest):
            self.get_latest()
        elif (_args.specific):
            self.get_specific()
        else:
            logging.error("Unexpected argument")

    def display_releases(self):
        releases = self._githubService.get_releases()
        print(releases)

    def get_latest(self):
        print("TODO")

    def get_specific(version):
        print(f"TODO: {version}")

    def get_args(self):
        _configService = config_service.ConfigService()
        _configService.read_config()
        parser = argparse.ArgumentParser(('GetGE'))
        parser.add_argument('--list', dest='list', default=False, action='store_true', help=' display all available versions')
        parser.add_argument('--latest', dest='latest', default=False,
                            action='store_true', help='get the latest version and extract')
        parser.add_argument('--specific', dest='specific')
        parser.add_argument('-v', help='display application version',
                            action='version', version='%(prog)s 1.0')

        return parser.parse_args()


if __name__ == '__main__':
    main().main()
