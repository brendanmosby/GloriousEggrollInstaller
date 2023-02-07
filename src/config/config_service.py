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

        self.write_config(config_file)

    def write_config(self, config_file):
        with open(os.path.join(self.CWD, self.FILE_PATH, self.FILE_NAME), 'w', encoding="utf-8") as file_obj:
            config_file.write(file_obj)
            file_obj.flush()
            file_obj.close()

        print(f"Config file '{self.FILE_NAME}' created")

    def read_config(self):
        config_path = os.path.join(self.CWD, self.FILE_PATH, self.FILE_NAME)
        config = configparser.ConfigParser()
        config.read(config_path)

        return config
