import json


class Config:

    @staticmethod
    def __get_config() -> json:

        file_path = 'database/config.json'

        with open(file_path) as f:
            data = json.load(f)

        return data

    @staticmethod
    def get_dwh_config() -> dict:
        config_data: json = Config.__get_config()
        return config_data["dwh"]
