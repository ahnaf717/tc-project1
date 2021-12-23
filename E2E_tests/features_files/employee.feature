Feature: An Employee should be able to login and view his/her employee dashboard				
				
  Scenario Outline:I want to login to manage my employee reimbursements				
    Given The Employee is on the homepage				
    When The Employee enters their username <value>
    When The Employee enters their password <value1>
    When The Employee clicks on the login button
    Then The Employee should be directed to the employee dashboard webpage <title>
  
   Examples:
     | value | value1 | title     |
     | John  | John   | Dashboard |
  			