import os
from datetime import datetime  
from core.utilities.random_utils import generate_random_string

def get_full_path(path):
    return os.path.abspath(path)
def get_project_path():
    return os.path.abspath(__file__)

def generate_screenshot_file_name():
    current_time = datetime.today().strftime("%Y-%m-%d_%H%M")
    return '%s_%s.png' %(generate_random_string(), current_time)