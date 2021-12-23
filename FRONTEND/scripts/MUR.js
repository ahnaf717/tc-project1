



let newreimbursementform=document.getElementById("reimbursementform");
newreimbursementform.onsubmit = 
async function (e){

    e.preventDefault();
    
    let url = "http://127.0.0.1:5000/update/reimbursement";
    let reimbursementID=document.getElementById("reimbursementID").value
    let status=document.getElementById("status").value
    let managercomments=document.getElementById("managercomments").value
  

   

    let response = await fetch(url,{
    
        method : "POST",
        headers:{"Content-Type":"application/json"},
        body : JSON.stringify({
            "reimbursementID":reimbursementID,
            "reimbursementCode":null,
            "amount":null,
            "employeeID":null,
            "status":status,
            "managerComments":managercomments})

    })

    let responsedata = await response.json();
    console.log(responsedata)
    alert("Request Has Been Updated Successfully")
    
}




