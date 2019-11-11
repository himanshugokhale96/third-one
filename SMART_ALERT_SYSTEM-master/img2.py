# -*- coding: cp1252 -*-
import cv2
from bottle import route,run,template,get,post,request


name = " "
@get('/login')
def login():
        return '''
 
<!doctype html>
<html>
<head>
<title>smart alert system</title>
<style>
body{
background-image:url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQC2kSAvcqAkIp-e3Dia8UbK9633s-KHrlb7k3ZfChf1GhvY3THdA");
background-size: 1300px 800px;
background-repeat:no-repeat;
} 
#rcorners3{
border-radius: 80px 0px;
background-image:url("back.jpg");
padding: 20px; 
width: 500px;
height: 200px;
opacity:0.8; 
}
</style>
</head>
<body><b>
<h1 align="center" style="color:black">SMART ALERT SYSTEM</h1></b>
<form id=rcorners3 method="post" action="/login">
												
<img src="park.jpg" height="100px" width="100px">
<img src="_" width="150px" heigth="150px">
<input type="file" name="photo" value="">
<input type = "submit" value = upload />

</form>
</body>
</html>
       '''

@post('/login')
def do_login():
        global name
        name = request.forms.get('photo')
        print(name)
        file = open('testfile.txt','w') 
 
        file.write(name) 
 
        file.close()
       

        
               
run(host = 'Localhost',port=8080,debug=True)
        
