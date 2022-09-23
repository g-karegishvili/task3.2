import json
from utilities.logger import Logger


class FileHandler:
    logger = Logger.logger()

    @classmethod
    def get_test_data(cls, variable):
        with open('../data/test_data.json') as f:
            data = json.load(f)
            cls.logger.info("test data file was opened and loaded")
            f.close()
        return data[variable]

    @classmethod
    def get_config_data(cls, variable):
        with open('../data/config_data.json') as f:
            data = json.load(f)
            cls.logger.info("config file was opened and loaded")
            f.close()

        return data[variable]
