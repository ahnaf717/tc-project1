from abc import ABC, abstractmethod

from entities.employees import Employee
from entities.reimbursements import Reimbursement


class EmployeeDAO(ABC):

    # view employee information
    @abstractmethod
    def employee_login(self, employee_username:Employee,employee_password):
        pass

    # create an employee reimbursment 
    @abstractmethod
    def create_reimbursements(self, reimbursement: Reimbursement):
        pass
    
    
    # view all reimbursements for the employee
    @abstractmethod
    def view_reimbursements(self,employee_id:Reimbursement):
        pass

 