from services import github_service
from controllers import download_controller

class GithubController():
    _githubService = github_service.GithubService()
    _downloadController = download_controller.DownloadController()

    def get_latest(self):
        releases = self._githubService.get_releases()
        latest_release = releases[0]

    def get_release_info(self, release_id):
        release_info = self._githubService.get_info_for_release(release_id)
        self._downloadController.download_release_files(release_info)


    def get_releases():
        print('TODO')