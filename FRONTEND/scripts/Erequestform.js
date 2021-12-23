



let newreimbursementform=document.getElementById("reimbursementform");

newreimbursementform.onsubmit = 
async function (e){

    e.preventDefault();

    let url = " http://127.0.0.1:5000/reimbursement";
    
    let reimbursementType=document.getElementById("reimbursementCode").value
    let reimbursementAmount=document.getElementById("reimbursementAmount").value
    if (reimbursementAmount<0){alert("Please Please Make Sure You Either Entered A Correct Reimbursement Code or An Entered An Amount Greater Than Zero")}
    else if (reimbursementType <=0 || reimbursementType >5){alert("Please Please Make Sure You Either Entered A Correct Reimbursement Code or An Entered An Amount Greater Than Zero")}


    else if (reimbursementType<5 && reimbursementType>0 && reimbursementAmount>0 )
       {
        let response = await fetch(url,{
    
            method : "POST",
            headers:{"Content-Type":"application/json"},
            body : JSON.stringify({
                "reimbursementID":null,
                "reimbursementCode":reimbursementType,
                "amount":reimbursementAmount,
                "employeeID":employee_id,
                "status":null,
                "managerComments":null})
    
    
    
        })
    
        let responsedata = await response.json();
        console.log(responsedata)
        alert("Request Has Been Submitted Successfully")
      
      
    
    }
}
    

    
    
    
    
    
    
  
    





