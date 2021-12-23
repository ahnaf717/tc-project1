class Statistics:

    def __init__(self,employee_id,number_reimbursements,total_amount,average_amount,max_amount,
                 responded_reimbursements):
        self.employee_id=employee_id
        self.number_reimbursements=number_reimbursements
        self.total_amount=total_amount
        self.average_amount=average_amount
        self.max_amount=max_amount
        self.responded_reimbursements=responded_reimbursements

    def make_stats_dictionary(self):
            return {
            "employeeID":self.employee_id,
            "totalReimbursements":self.number_reimbursements,
            "sumReimbursements":self.total_amount,
            "averageReimbursements":self.average_amount, 
            "maxReimbursement":self.max_amount,
            "respondedReimbursement":self.responded_reimbursements

            }

      