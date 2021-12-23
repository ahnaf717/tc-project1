

const employee_id = sessionStorage.getItem("employeeID");


console.log(employee_id)

const table = document.getElementById("reimbursementTable");
const tableBody = document.getElementById("reimbursementBody");

async function getReimbursementData(){
    let url = ` http://127.0.0.1:5000/reimbursement/${employee_id}`;

    let response = await fetch(url);
    
        let body = await response.json();
        populateData(body);
    
    
}

function populateData(responseBody){
    
    

    for (let reimbursement of responseBody){
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${reimbursement.reimbursementID}</td><td>${reimbursement.reimbursementCode}</td><td>${reimbursement.amount}</td>
        <td>${reimbursement.employeeID}</td><td>${reimbursement.status}</td>
        <td>${reimbursement.managerComments}</td>`;
        reimbursementBody.appendChild(tableRow);
    }
}

getReimbursementData()


function showTable(){
    document.getElementById('reimbursementTable').style.visibility = "visible";
    }
    function hideTable(){
    document.getElementById('reimbursementTable').style.visibility = "hidden";
    }


function logout(){
    sessionStorage.clear()
    window.location.href="index.html"



}