from .employee import Employee

def get_model():
    employee = Employee.load_config("docs/employee/config.yml")
    return employee

