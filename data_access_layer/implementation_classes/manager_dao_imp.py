from data_access_layer.abstract_classes.manager_dao import ManagerDAO
from entities.managers import Manager
from entities.reimbursements import Reimbursement
from entities.statistics import Statistics
from Utilities.database_connection import connection


class ManagerDAOIMP(ManagerDAO):
    
    def manager_login(self, manager_username,manager_password):
        try:
            sql = "select * from managers where manager_username =%s and manager_password=%s"
            cursor = connection.cursor()
            cursor.execute(sql,(manager_username,manager_password))
            manager_record = cursor.fetchone()
            manager = Manager(*manager_record)
            return manager
        except TypeError as e:
            print(str(e))
            print("Incorrect UserName or Password!")

    def update_reimbursement(self, reimbursement: Reimbursement):
        sql = "update reimbursements set status = %s, manager_comments = %s where reimbursement_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (reimbursement.status, reimbursement.manager_comments, reimbursement.reimbursement_id))
        connection.commit()
        return reimbursement

    def view_current_reimbursements(self):
        sql = "select * from reimbursements where status is NULL"
        cursor = connection.cursor()
        cursor.execute(sql)
        reimbursement_records = cursor.fetchall()
        reimbursements = []
        for reimbursement in reimbursement_records:
            reimbursements.append(Reimbursement(*reimbursement))
        return reimbursements

    
    def view_past_reimbursements(self):
        sql = "select * from reimbursements where status is not NULL"
        cursor = connection.cursor()
        cursor.execute(sql)
        reimbursement_records = cursor.fetchall()
        reimbursements = []
        for reimbursement in reimbursement_records:
            reimbursements.append(Reimbursement(*reimbursement))
        return reimbursements
    
   
    

    def view_pending_reimbursements(self):
        sql = "select * from reimbursements where status =%s"
        cursor = connection.cursor()
        cursor.execute(sql, ['Pending'])
        reimbursement_records = cursor.fetchall()
        reimbursement_list = []
        for reimbursement in reimbursement_records:
            reimbursement_list.append(Reimbursement(*reimbursement))
        return reimbursement_list

    def view_employee_statistics(self):
        sql = "select * from rstats"
        cursor = connection.cursor()
        cursor.execute(sql)
        stats_records = cursor.fetchall()
        stats_list = []
        for stats in stats_records:
            stats_list.append(Statistics(*stats))
        return stats_list
        
