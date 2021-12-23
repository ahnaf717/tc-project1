


const table = document.getElementById("reimbursementTable");
const tableBody = document.getElementById("reimbursementBody");

async function getReimbursementData(){
    let url = "http://127.0.0.1:5000/view/statistics";

    let response = await fetch(url);
    
    if (response.status === 200){
        let body = await response.json();
        populateData(body);
    } else {
        alert("Error getting Reimbursement Request");
    }
}







function populateData(responseBody){
    
    

    for (let statistics of responseBody){
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${statistics.employeeID}</td><td>${statistics.totalReimbursements}</td><td>${statistics.sumReimbursements}</td>
        <td>${statistics.averageReimbursements}</td><td>${statistics.maxReimbursement}</td>
        <td>${statistics.respondedReimbursement}</td>`;
        reimbursementBody.appendChild(tableRow);
    }
}

getReimbursementData()


