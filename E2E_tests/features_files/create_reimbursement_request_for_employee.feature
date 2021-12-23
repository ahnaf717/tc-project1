Feature: An Employee should be able to create a new employee reimbursement request		
  
  Scenario Outline:As an employee I should be able to generate a new reimbursement request so that I can get reimbursed                              
    Given The Employee is attempting to login on the login page                             
    When The employee fills in his username <value>
    When The employee fills in his password <value1>
    When The Employee clicks on login  
    When The employee fills in the desired reimbursement code <value2> on the employee dashboard page
    When The employee fills in the desired reimbursement amount <value3>
    When The employee clicks on the submit request button
    Then The employee will be able to submit a reimbursement request
    Examples:
      | value | value1 | value2 | value3 |
      | ahnaf | tahmid | 2      | 300    |
    