from data_access_layer.abstract_classes.employee_dao import EmployeeDAO
from entities.employees import Employee
from entities.reimbursements import Reimbursement
from Utilities.database_connection import connection


class EmployeeDAOImp(EmployeeDAO):
    def employee_login(self, employee_username:Employee,employee_password:Employee):
        try:
            sql = "select * from employees where employee_username=%s and employee_password=%s"
            cursor = connection.cursor()
            cursor.execute(sql, (employee_username,employee_password))
            employee_record = cursor.fetchone()
            employee = Employee(*employee_record)
            return employee
        except TypeError as e:
            print(str(e))
            print("Incorrect UserName or Password!")

    def create_reimbursements(self, reimbursement: Reimbursement):
        sql = "insert into reimbursements values (default,%s,%s,%s) returning reimbursement_id"
        cursor = connection.cursor()
        cursor.execute(sql, ( reimbursement.reimbursement_code, reimbursement.amount,  reimbursement.employee_id))
        connection.commit()
        generated_reimbursement_id = cursor.fetchone()[0]
        reimbursement.reimbursement_id = generated_reimbursement_id
        return reimbursement

    def view_reimbursements(self,employee_id):
        sql = "select * from reimbursements where employee_id =%s"
        cursor = connection.cursor()
        cursor.execute(sql,[employee_id])
        reimbursement_records = cursor.fetchall()
        reimbursement_list = []
        for reimbursement in reimbursement_records:
            reimbursement_list.append(Reimbursement(*reimbursement))
        return reimbursement_list
        