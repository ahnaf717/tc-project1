class Reimbursement:

    def __init__(self, reimbursement_id, reimbursement_code,amount,
                 employee_id, status, manager_comments):
        self.reimbursement_id=reimbursement_id
        self.reimbursement_code=reimbursement_code
        self.amount=amount
        self.employee_id = employee_id
        self.status=status
        self.manager_comments=manager_comments

    def make_reimbursement_dictionary(self):
        return {
            "reimbursementID": self.reimbursement_id,
            "reimbursementCode": self.reimbursement_code,
            "amount": self.amount,
            "employeeID": self.employee_id,
            "status":self.status,
            "managerComments":self.manager_comments
  
        }

   