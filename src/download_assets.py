import os
import sys
import hashlib
import tarfile
import requests

class DownloadAssets():
    
    USER_STEAM_DIR = os.path.expanduser("~/.steam/root/compatibilitytools.d/")

    def download_assets(self, url, name):
        
        dl_path = f"{DownloadAssets.USER_STEAM_DIR}/{name}"

        if os.path.exists(dl_path):
            print(f"Using existing directory: {dl_path}")
            return

        with open(dl_path, "wb") as f:
            print(f"Downloading {name}")
            response = requests.get(url, stream=True)
            if response.status_code != 200:
                print("Server Error")
                quit()
            total_length = response.headers.get('content-length')

            if total_length is None: # no content length header
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(50 * dl / total_length)
                    sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
                    sys.stdout.flush()
                print()

    def compare_hash(self, file_name, checksum_name):
        print("Validating checksum...")
        hash = hashlib.sha512()
        #Read hash of file
        with open(f"{DownloadAssets.USER_STEAM_DIR}/{file_name}", "rb") as f:
            chunk = 0
            while chunk != b'':
                chunk = f.read(1024)
                hash.update(chunk)

        #Read checksum provided
        with open(f"{DownloadAssets.USER_STEAM_DIR}/{checksum_name}", "rb") as sha:
            raw_sum = sha.read()
            checksum = raw_sum.decode('utf-8')

        if (hash.hexdigest() == checksum.split()[0]):
            print("Checksum validated")
            os.remove(f"{DownloadAssets.USER_STEAM_DIR}/{checksum_name}")
            self.extract_tar(file_name)

    def extract_tar(self, tar_name):
        print("Extracting...")
        file = tarfile.open(f"{DownloadAssets.USER_STEAM_DIR}/{tar_name}")
        file.extractall(f"{DownloadAssets.USER_STEAM_DIR}")
        file.close()
        os.remove(f"{DownloadAssets.USER_STEAM_DIR}/{tar_name}")
