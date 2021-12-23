from data_access_layer.implementation_classes.employee_dao_imp import EmployeeDAOImp
from service_layer.implementation_services.employee_service_imp import EmployeeServiceImp

DAO=EmployeeDAOImp()

print(DAO.employee_login('John','John'))

employee_service= EmployeeServiceImp(DAO)
print(employee_service.service_employee_login('John','John'))