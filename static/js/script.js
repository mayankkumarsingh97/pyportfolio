const message_element= document.getElementById("msg");
setInterval(function(){
 message_element.style.display="none"
 message_element.style.transition = "all 2s";
},5000);