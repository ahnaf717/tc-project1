class Employee:
    
    def __init__(self,employee_id, employee_username,employee_password):
        self.employee_id = employee_id
        self.employee_username=employee_username
        self.employee_password=employee_password
       

    def make_employee_dictionary(self):
            return {
              "employeeID":self.employee_id,
              "username":self.employee_username,
              "password":self.employee_password
              
            }
        
