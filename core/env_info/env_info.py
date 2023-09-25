from core.utilities.file_utils import get_full_path
import json

class EnvironmentInfo():
    application_url = None
    api_url = None
    firebase_uri = None
    api_key = None

    @classmethod
    def get_environment_info(cls, configuration_file_path, env):
        with open(get_full_path(configuration_file_path)) as f:
            data = json.load(f)
            cls.application_url = data[env]['baseUrl']
            cls.api_url = data[env]['apiBaseUrl']
            cls.firebase_uri = data[env]['firebaseUri']
            cls.api_key = data[env]['apiKey']

