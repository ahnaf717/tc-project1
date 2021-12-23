from flask import Flask, request, jsonify
from data_access_layer.implementation_classes.employee_dao_imp import EmployeeDAOImp
from data_access_layer.implementation_classes.manager_dao_imp import ManagerDAOIMP
from entities.employees import Employee
from entities.managers import Manager
from entities.reimbursements import Reimbursement
from entities.statistics import Statistics
from service_layer.implementation_services.employee_service_imp import EmployeeServiceImp
from service_layer.implementation_services.managers_service_imp import ManagerServiceImp
from flask_cors import CORS

app: Flask = Flask(__name__)
CORS(app)
cors=CORS(app,resources={
    r"/*":{
        "origins": "*"
    }
    
})



employee_dao=EmployeeDAOImp()
employee_service=EmployeeServiceImp(employee_dao)
manager_dao=ManagerDAOIMP()
manager_service=ManagerServiceImp(manager_dao)


#get employee
@app.post("/login")
def employee_login():
    data = request.get_json()
    current_employee=Employee(
    data["employeeID"],
    data["username"],
    data["password"]
    )
    employee_return=employee_service.service_employee_login(current_employee.employee_username,current_employee.employee_password)
    employee_as_dictionary=employee_return.make_employee_dictionary()
    employee_as_json=jsonify(employee_as_dictionary)
    return employee_as_json
    




@app.post("/reimbursement")
def create_riembursement(force=True):
    #try:
        info = request.get_json(force=True)
        created_reimbursement = Reimbursement(
            info["reimbursementID"],
            info["reimbursementCode"],
            info["amount"],
            info["employeeID"],
            info["status"],
            info["managerComments"]
        )
           
        created_riembursement = employee_service.service_create_reimbursements(created_reimbursement)
        created_reimbursement_as_dictionary =created_riembursement.make_reimbursement_dictionary()
        return jsonify(created_reimbursement_as_dictionary)
   
        


@app.get("/reimbursement/<employee_id>")
def get_all_employee_reimbursements(employee_id):
    employee_reimbursements = employee_service.service_view_reimbursements(employee_id)
    reimbursements_as_dictionaries= []
    for reimbursement in employee_reimbursements:
        dictionary_reimbursement =reimbursement.make_reimbursement_dictionary()
        reimbursements_as_dictionaries.append(dictionary_reimbursement)
    return jsonify(reimbursements_as_dictionaries), 200


#get employee
@app.post("/manager")
def get_manager_information():
    data = request.get_json()
    current_manager= Manager(
    data["managerID"],
    data["userName"],
    data["passWord"]
    )
    manager_return=manager_service.service_manager_login(current_manager.manager_username,current_manager.manager_password)
    manager_as_dictionary=manager_return.make_manager_dictionary()
    manager_as_json=jsonify(manager_as_dictionary)
    return manager_as_json

@app.get("/reimbursement/new")
def view_current_employee_reimbursements():
    employee_reimbursements =manager_service.service_view_current_reimbursements()
    reimbursements_as_dictionaries= []
    for reimbursement in employee_reimbursements:
        dictionary_reimbursement =reimbursement.make_reimbursement_dictionary()
        reimbursements_as_dictionaries.append(dictionary_reimbursement)
    return jsonify(reimbursements_as_dictionaries), 200



@app.get("/manager/reimbursement/previous")
def view_employee_reimbursements():
    employee_reimbursements =manager_service.service_view_past_reimbursements()
    reimbursements_as_dictionaries= []
    for reimbursement in employee_reimbursements:
        dictionary_reimbursement =reimbursement.make_reimbursement_dictionary()
        reimbursements_as_dictionaries.append(dictionary_reimbursement)
    return jsonify(reimbursements_as_dictionaries), 200




@app.post("/update/reimbursement")
def update_reimbursement(force=True):
        info = request.get_json()
        updated_reimbursement = Reimbursement(
        info["reimbursementID"],
        info["reimbursementCode"],
        info["amount"],
        info["employeeID"],
        info["status"],
        info["managerComments"]
    
        )
        manager_service.service_update_reimbursement(updated_reimbursement)
        #dictionary = {"message":"Request Has Been Updated"}
        #exception_json = jsonify(dictionary)
        #return exception_json
        updated_reimbursement_as_dictionary = updated_reimbursement.make_reimbursement_dictionary()
        return jsonify(updated_reimbursement_as_dictionary)
    


@app.get("/pending/reimbursement")
def view_pending_reimbursements():
    pending_reimbursements = manager_service.service_view_pending_reimbursements()
    reimbursements_as_dictionaries= []
    for reimbursement in pending_reimbursements:
        dictionary_reimbursement =reimbursement.make_reimbursement_dictionary()
        reimbursements_as_dictionaries.append(dictionary_reimbursement)
    return jsonify(reimbursements_as_dictionaries), 200



@app.get("/view/statistics")
def view_reimbursement_stats():
    reimbursement_stats = manager_service.service_view_employee_statistics()
    stats_as_dictionaries= []
    for stats in reimbursement_stats:
        dictionary_stats =stats.make_stats_dictionary()
        stats_as_dictionaries.append(dictionary_stats)
    return jsonify(stats_as_dictionaries), 200



app.run()


