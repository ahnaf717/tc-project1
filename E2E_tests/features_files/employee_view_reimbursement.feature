Feature: An Employee should be able view his reimbursement requests			
  
  Scenario Outline:As an Employee I want view my reimbursement requests so I know if they are approved or not                              
    Given The Employee logs into the employee page successfully                              
    When The employee fills out his username <value>
    When The employee fills out his password<value1>
    When Employee selects the login in button  
    When The employee clicks the view reimbursement button on the employee dashboard page
    Then The employee should see his reimbursement requests
    Examples:
      | value | value1 |
      | ahnaf | tahmid |
        