Feature: A manager should be able to login and view his/her manager dashboard				
				
  Scenario Outline:I want to login to manager dashboard and manage employee reimbursement requests			
    Given The Manager is on the login page				
    When The Manager enters their username <value>
    When The Manager enters their password <value1>
    When The Manager clicks on the login button
    Then The Manager should be directed to the manager dashboard webpage <title>
  
   Examples:
     | value | value1  | title             |
     | boss  | manager | Manager Dashboard |
  			