from abc import ABC, abstractmethod
from entities.managers import Manager
from entities.reimbursements import Reimbursement


class ManagerService(ABC):

    # create account
    @abstractmethod
    def service_manager_login(self, manager_username,manager_password):
        pass

    # get account information
    @abstractmethod
    def service_update_reimbursement(self, reimbursement: Reimbursement):
        pass

    @abstractmethod
    def service_view_current_reimbursements(self):
        pass

    @abstractmethod
    def service_view_past_reimbursements (self):
        pass

    @abstractmethod
    def service_view_pending_reimbursements(self):
        pass
    
    @abstractmethod
    def service_view_employee_statistics(self):
        pass
