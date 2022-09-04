'''Get Github information'''
import requests

class GetGithubInfo():
    '''Class used for retrieving and parsing the information received from Github'''

    def get_info(self):
        '''Get release information from Github'''
        gh_url = "https://api.github.com/repos/GloriousEggroll/proton-ge-custom/releases/latest"

        response = self.request(gh_url)

        try:
            asset_urls = self.parse(response)
        except ValueError as v_error:
            print(v_error)

        return asset_urls

    def parse(self, json):
        '''Parse the JSON received from the URL'''
        asset_urls = []
        assets = json["assets"]

        if len(assets) > 0:
            for asset in assets:
                name = asset["name"]
                url = asset["browser_download_url"]

                asset_url = { name: url }
                asset_urls.append(asset_url)
        else:
            raise ValueError("Error receiving assets from Github")

        return asset_urls

    def request(self, url):
        '''Retrieve the JSON from the URL'''
        response = requests.get(url, timeout=10)
        return response.json()
