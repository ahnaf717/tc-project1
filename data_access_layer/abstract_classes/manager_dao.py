from abc import ABC, abstractmethod
from entities.managers import Manager
from entities.reimbursements import Reimbursement


class ManagerDAO(ABC):


    @abstractmethod
    def manager_login(self, manager_username: Manager,manager_password):
        pass

  
    @abstractmethod
    def update_reimbursement(self, reimbursement: Reimbursement):
        pass
    
    @abstractmethod
    def view_current_reimbursements(self):
        pass

    @abstractmethod
    def view_past_reimbursements (self):
        pass

    
    @abstractmethod
    def view_pending_reimbursements(self):
        pass
    
    
    @abstractmethod
    def view_employee_statistics(self):
        pass
