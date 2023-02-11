import logging
from services import github_service
from controllers import download_controller

class GithubController():
    _githubService = github_service.GithubService()
    _downloadController = download_controller.DownloadController()

    def install_latest(self):
        releases = self._githubService.get_releases()
        latest_release = releases[0]
        latest_release_id = list(latest_release.keys())[0]
        
        asset_urls = self._githubService.get_assets_for_release(latest_release_id)
        self._downloadController.download_release_files(asset_urls)

    def download_release(self, release_id):
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