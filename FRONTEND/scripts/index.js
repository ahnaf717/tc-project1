console.log("Its connected")

let loginform = document.getElementById("employeeloginform")
let managerloginform=document.getElementById("managerloginform")

function toggle()

{

  var x=document.getElementById("employeeloginform");

  if(x.style.display ==="none")

  {

    x.style.display="block";

  }


  else{

    x.style.display ="none";
  }



}


function toggle1()

  {
  
    var x=document.getElementById("managerloginform");
  
    if(x.style.display ==="none")
  
    {
  
      x.style.display="block";
  
    }
  
  
    else{
  
      x.style.display ="none";
    }



 async function login(){

   
   
    let username = document.getElementById("Username").value;
    let password = document.getElementById("password").value;

    console.log(username,password)



    let response = await fetch("http://127.0.0.1:5000/login",{
        method : "POST",
        headers:{"Content-Type":"application/json"},
        body : JSON.stringify({"employeeID":null,"username":username,"password":password})

           //employeeID : 3,
           //username : username , 
           //password : password  
        })

           
        

    let responsedata = await response.json();
    console.log(responsedata)
    sessionStorage.setItem("employeeID",responsedata.employeeID)
    window.location.href = "Edashboard.html"

      


}


let buttonn=document.getElementById("ebutton");
buttonn.onclick=login()

managerloginform.onsubmit = async function(e){

    e.preventDefault()
   
    let username = document.getElementById("musername").value;
    let password = document.getElementById("mpassword").value;

    console.log(username,password)



    let response = await fetch("http://127.0.0.1:5000/manager",{
        method : "POST",
        headers:{"Content-Type":"application/json"},
        body : JSON.stringify({"managerID":null,"userName":username,"passWord":password})

           //employeeID : 3,
           //username : username , 
           //password : password  
        })

           
        

    let responsedata = await response.json();
    console.log(responsedata)
    window.location.href = "Manager Reimbursement Dashboard.html"








  }
}