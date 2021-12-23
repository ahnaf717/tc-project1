
Feature: A manager should be able to update a reimbursement request
  
Scenario Outline:As a manager I want to approve or deny an employee reimbursement request and leave my comments                             
  Given The manager is on the Manager Dashboard Page                              
    When The manager fills out the reimbursement ID section <value>
    When The manager fills out the reimbursement status section<value1>
    When The manager fills out the manager comments section<value2>
    When The manager clicks on the submit request button
    Then The reimbursement request should be updated successfully
  Examples:
    | value | value1   | value2   |
    | 40    | Approved | Approved |
      
  