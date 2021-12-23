from data_access_layer.implementation_classes.manager_dao_imp import ManagerDAOIMP
from entities.managers import Manager
from entities.reimbursements import Reimbursement
from service_layer.abstract_services.manager_service import ManagerService


class ManagerServiceImp(ManagerService):
    def __init__(self,manager_dao):
        self.manager_dao:ManagerDAOIMP=manager_dao
        
    def service_manager_login(self,manager_username:Manager,manager_password:Manager):
        return self.manager_dao.manager_login(manager_username,manager_password)

    def service_update_reimbursement(self, reimbursement: Reimbursement):
        return self.manager_dao.update_reimbursement(reimbursement)
    
    
    def service_view_current_reimbursements(self):
        return self.manager_dao.view_current_reimbursements()

    def service_view_past_reimbursements(self):
        return self.manager_dao.view_past_reimbursements()

    def service_view_pending_reimbursements(self):
        return self.manager_dao.view_pending_reimbursements()
    
    def service_view_employee_statistics(self):
        return self.manager_dao.view_employee_statistics()