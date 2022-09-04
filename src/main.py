#!/usr/bin/env python
import os
import get_github_info
import download_assets

GetGithubInfo = get_github_info.GetGithubInfo()
DownloadAssets = download_assets.DownloadAssets()

assets = GetGithubInfo.get_info()

for asset in assets:
    file_name = list(asset.keys())[0]
    file_ext = os.path.splitext(file_name)[1]
    url = asset[file_name]
    
    if (os.path.exists(f"{DownloadAssets.USER_STEAM_DIR}/{file_name}")):
        print("You already have the latest version!")
        quit()

    DownloadAssets.download_assets(url, file_name)

    if (file_ext == ".sha512sum"):
        hash = file_name
    elif (file_ext == ".gz"):
        file = file_name

DownloadAssets.compare_hash(file, hash)

print("Done!")