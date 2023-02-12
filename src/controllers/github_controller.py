import logging
from services import github_service
from controllers import download_controller

class GithubController():
    _githubService = github_service.GithubService()
    _downloadController = download_controller.DownloadController()

    def install_latest(self):
        releases = self.get_releases()
        latest_release = releases[0]
        latest_release_id = list(latest_release.keys())[0]
        
        self.install_release_for_id(latest_release_id)

    def install_release_for_id(self, release_id):
        '''Install release for given ID'''
        release_info = self._githubService.get_assets_for_release(release_id)
        self._downloadController.download_release_files(release_info)

    def get_releases(self):
        '''Get all releases from Github'''
        release_url = self._githubService.GH_BASE_URL
        response = self._githubService.request(release_url)

        try:
            releases = self._githubService.parse_releases(response)
        except ValueError as v_error:
            logging.error(v_error)

        return releases