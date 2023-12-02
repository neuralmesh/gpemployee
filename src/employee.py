import yaml
from .responsegetter import get_response

class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __str__(self):
        return f"Employee(name={self.name}, role={self.role})"
    
    @staticmethod
    def get_response(userprompt):
        get_response(userprompt)

    @staticmethod
    def load_config(config_path):
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        return Employee(config['name'], config['role'])

