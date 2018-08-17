function Func(){
    var x= document.getElementById('password');
    var y= document.getElementById('passworda');
    if(x.value!=y.value){
     //x.style.backgroundColor="#F08080";
     //y.style.backgroundColor="#F08080";
     document.getElementById('errorp').innerHTML="Passwords didn't match!";
     return false;
   }
   else {
     return true;
   }
  }
  
  function usertest(){
    /*var len = document.getElementById('Username');
    if(len.value.length<8){
      len.style.backgroundColor="#F08080";
      document.getElementById('erroru').innerHTML="The username should not be less than 8 characters";
    }
    if(len.value.length>=8){
        len.style.backgroundColor= "white";
        document.getElementById('erroru').innerHTML="";
    }*/
    var regex= /^[A-Za-z0-9_]{3,10}$/;
    var usr=document.getElementById('Username');
    var usre=document.getElementById('Username').value;
    if(!regex.test(usre)){
      //usr.style.backgroundColor="#F08080";
      document.getElementById('erroru').innerHTML="The username should not be less than 3 characters, can contain letters, numbers and underscores";
      return false;
    }
    else {
      usr.style.backgroundColor="white";
      document.getElementById('erroru').innerHTML="";
      return true;
    }
    /*if(regex.test(usr)){
      usr.style.backgroundColor="white";
      document.getElementById('erroru').innerHTML="";
    }*/
  }
  
  function numtest(){
    var len=document.getElementById('contact');
    var isnum = /^\d+$/.test(len.value);
    if(len.value.length!=10 && !isnum){
    //  len.style.backgroundColor="#F08080";
      document.getElementById('errorc').innerHTML="Enter a valid phone number";
      return false
    }
    if(len.value.length==10 && isnum){
      len.style.backgroundColor="white";
      document.getElementById('errorc').innerHTML="";
      return true;
    }
  }