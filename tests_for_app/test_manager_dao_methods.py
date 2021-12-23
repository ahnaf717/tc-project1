from data_access_layer.implementation_classes.manager_dao_imp import ManagerDAOIMP
from entities.managers import Manager
from entities.reimbursements import Reimbursement

manager_dao=ManagerDAOIMP()

updated_reimbursement_9=Reimbursement(9,3,3000,1,'Approved','You Got It')


def test_manager_login_success():
    loggedin_manager=manager_dao.manager_login('charge','charge')
    assert loggedin_manager.manager_id==2 and loggedin_manager.manager_password=='charge'
    

    
    
def test_update_reimbursement_success():
    updated_reimbursement=manager_dao.update_reimbursement(updated_reimbursement_9)
    assert updated_reimbursement.status=='Approved' and updated_reimbursement.manager_comments=='You Got It'
    
    
    
    

def test_view_pending_reimbursments_success():
    pending_reimbursments=manager_dao.view_pending_reimbursements()
    assert len(pending_reimbursments) >=1
    
    
def test_view_new_reimbursement_requests_success():
    new_reimbursements=manager_dao.view_current_reimbursements()
    assert len(new_reimbursements) >=2
    


def test_view_employee_reimbursement_stats_success():
    employee_reimbursement_stats=manager_dao.view_employee_statistics()
    assert len(employee_reimbursement_stats)>=2


def test_view_past_reimbursements():
   past_reimbursements=manager_dao.view_past_reimbursements()
   assert len(past_reimbursements) >= 2

    
    

    
    
    
    
