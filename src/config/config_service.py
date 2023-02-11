import os
import configparser


class ConfigService():

    FILE_PATH = 'src/config'
    FILE_NAME = 'config.conf'
    CWD = os.getcwd()

    def create_config(self):
        config_file = configparser.ConfigParser()

        config_file.add_section("Application")
        config_file.set("Application", "version", "1.0.0")

        config_file.add_section("SteamPath")
        config_file.set("SteamPath", "path", os.path.expanduser("~/.steam/root/compatibilitytools.d/"))

        self.write_config(config_file)

    def write_config(self, config_file):
        with open(os.path.join(self.CWD, self.FILE_PATH, self.FILE_NAME), 'w', encoding="utf-8") as file_obj:
            config_file.write(file_obj)
            file_obj.flush()
            file_obj.close()

    def read_config(self):
        config_path = os.path.join(self.CWD, self.FILE_PATH, self.FILE_NAME)
        if not (os.path.exists(config_path)):
            self.create_config()
        
        config = configparser.ConfigParser()
        config.read(config_path)

        return config
