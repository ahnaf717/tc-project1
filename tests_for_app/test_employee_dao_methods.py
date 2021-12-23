from data_access_layer.implementation_classes.employee_dao_imp import EmployeeDAOImp
from entities.employees import Employee
from entities.reimbursements import Reimbursement

employee_dao=EmployeeDAOImp()

request=Reimbursement(0,3,3000,1,None,None)




def test_employee_login_success():
    loggedin_employee=employee_dao.employee_login('adam','ryan')
    assert loggedin_employee.employee_id==2 and loggedin_employee.employee_password=='ryan'
    
    
def test_create_reimbursement_request_success():
    created_request=employee_dao.create_reimbursements(request)
    assert created_request.reimbursement_id !=0
    
    
    
def test_view_reimbursements_request_success():
    past_reimbursments=employee_dao.view_reimbursements(3)
    assert len(past_reimbursments)>=2