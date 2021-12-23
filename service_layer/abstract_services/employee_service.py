from abc import ABC, abstractmethod
from entities.employees import Employee
from entities.reimbursements import Reimbursement


class EmployeeService(ABC):

    # view employee information
    @abstractmethod
    def service_employee_login(self, employee_username:Employee,employee_password: Employee):
        pass

    # create an employee reimbursment 
    @abstractmethod
    def service_create_reimbursements(self, reimbursement: Reimbursement):
        pass

    # view all reimbursements for the employee
    @abstractmethod
    def service_view_reimbursements(self,employee_id:Reimbursement):
        pass
