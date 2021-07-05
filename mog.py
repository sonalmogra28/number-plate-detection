#! /usr/bin/python3

print("content-type: text/html")
print()


print('''<style>
pre{
color: black;
font-weight: bold;
font-size: 20px;
}
</style>''')
import cgi
import subprocess as sb
fs = cgi.FieldStorage()
plate_no = fs.getvalue("plate_no")
if plate_no == "CZ20FSE":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#adff2f;background-color:red" >Output</h1>')
    print('''<pre>
    Registration Name : SONAL MOGRA 
    License No : 12345677889
    Make / Model : SKODA
    Registration Date : 1/12/2011
    Registering Authority : JAIPUR , INDIA
    Vehicle Class : MCWG
    Fuel Type : CNG
    Engine No : IVK3N1734538
    Chassis No : HMSURVWVQSVWE
    Insurance Upto : 14/12/2023
    Fitness Upto : 4/8/2030
    </pre>''')
    print("</body>")

elif plate_no == "MH 20EJ 0364":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#adff2f;background-color:red" >Output</h1>')
    print('''<pre>
    Registration Name : AMAN SINGHAANIA
    License No : 098363357292
    Make / Model : SKODA
    Registration Date : 1/11/2014
    Registering Authority : CHANDIGARH, INDIA
    Vehicle Class : MCWG
    Fuel Type : CNG
    Engine No : IVK3N1734538
    Chassis No : HMSURVWVQSVWE
    Insurance Upto : 5/11/2022
    Fitness Upto : 4/8/2022
    </pre>''')
    print("</body>")

elif plate_no == "KL2158086":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#adff2f;background-color:red" >Output</h1>')
    print('''<pre>
    Registration Name : NIDHI GOEL
    License No : 735382528936
    Make / Model : RANGE ROVER
    Registration Date : 1/12/201
    Registering Authority : MANDSAUR, INDIA
    Vehicle Class : MCWG
    Fuel Type : CNG
    Engine No : IVK3N1734538
    Chassis No : HMSURVWVQSVWE
    Insurance Upto : 5/13/2025
    Fitness Upto : 31/1/2027
    </pre>''')
    print("</body>")

else:
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#adff2f;background-color:red" >Output</h1>')
    print("No data available for this number...")
    print("</body>")