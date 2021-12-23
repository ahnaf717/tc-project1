from data_access_layer.implementation_classes.employee_dao_imp import EmployeeDAOImp
from entities.employees import Employee
from entities.reimbursements import Reimbursement
from service_layer.abstract_services.employee_service import EmployeeService
from custom_exceptions.reimbursement_code_exception import ReimbursementCodeException
from custom_exceptions.reimbursement_amount_exception import ReimbursementAmountException


class EmployeeServiceImp(EmployeeService):
    def __init__(self, employee_dao):
        self.employee_dao: EmployeeDAOImp = employee_dao
        
    def service_employee_login(self, employee_username: Employee,employee_password:Employee):
        
        return self.employee_dao.employee_login(employee_username,employee_password)
        

    def service_create_reimbursements(self, reimbursement: Reimbursement):
        """if reimbursement.reimbursement_code <=0 or reimbursement.reimbursement_code >4:
            raise ReimbursementCodeException("Please Enter A Valid Reimbursement Code")
        elif reimbursement.amount <=0:
            raise ReimbursementAmountException("Amount Must Be Greater Than Zero")"""
        return self.employee_dao.create_reimbursements(reimbursement)

    def service_view_reimbursements(self,employee_id:Reimbursement):
        return self.employee_dao.view_reimbursements(employee_id)