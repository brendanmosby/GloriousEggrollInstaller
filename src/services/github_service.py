import logging
import requests
import sys

class GithubService():
    GH_BASE_URL = 'https://api.github.com/repos/GloriousEggroll/proton-ge-custom/releases'

    def get_assets_for_release(self, release_id):
        '''Get release information from Github'''
        release_info_url = self.GH_BASE_URL + '/' + str(release_id)

        response = self.request(release_info_url)

        try:
            asset_urls = self.parse_release_info(response)
        except ValueError as v_error:
            print(v_error)

        return asset_urls

    def parse_release_info(self, json):
        '''Parse the JSON received from the URL'''
        asset_urls = []
        assets = json["assets"]
        tag_name = json["tag_name"]

        if len(assets) > 0:
            for asset in assets:
                name = asset["name"]
                url = asset["browser_download_url"]

                asset_url = {name: url}
                asset_tags = {tag_name: asset_url}
                asset_urls.append(asset_tags)
        else:
            raise ValueError("Error receiving assets from Github")

        return asset_urls
    
    def parse_releases(self, json):
        releases = []
        if len(json) > 0:
            for release in json:                
                if (release == 'message'):
                    logging.error(json['message'])
                    sys.exit()

                id = release['id']
                name = release['tag_name']

                release = {id: name}
                releases.append(release)
        else:
            raise ValueError("Error receiving release information from Github")
        
        return releases

    def request(self, url):
        '''Retrieve the JSON from the URL'''
        response = requests.get(url, timeout=10)
        return response.json()
