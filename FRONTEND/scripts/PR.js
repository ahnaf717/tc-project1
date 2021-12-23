
//const table = document.getElementById("playerTable");
//const tableBody = document.getElementById("playerBody");

const table = document.getElementById("reimbursementTable");
const tableBody = document.getElementById("reimbursementBody");

async function getReimbursementData(){
    let url = "http://127.0.0.1:5000/pending/reimbursement";

    let response = await fetch(url);
    
    if (response.status === 200){
        let body = await response.json();
        populateData(body);
    } else {
        alert("Error getting Reimbursement Request");
    }
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


