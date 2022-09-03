import json
import requests

class GetGithubInfo(): 

    def get_info(self):
        GH_URL = "https://api.github.com/repos/GloriousEggroll/proton-ge-custom/releases/latest"
        
        response = self.request(GH_URL)

        try: 
            asset_urls = self.parse(response)
        except error:
            print(error)

        return asset_urls

    def parse(self, json):
        asset_urls = []
        tag_name = json["tag_name"]
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
        response = requests.get(url)
        return response.json()