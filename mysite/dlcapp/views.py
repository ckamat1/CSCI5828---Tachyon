# from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.
# def index(request):
#     return HttpResponse('This is simple page')
import MySQLdb
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'right_now':datetime.today()})

def index(request):
    return render(request,'index.html')

def Bootstrap(request):
    return render(request,'Bootstrap.html')

def register(request):
    firstname=request.GET.get('firstname','')
    lastname=request.GET.get('lastname','')
    gender=request.GET.get('gender','')
    project=request.GET.get('project','')

    db = MySQLdb.connect("127.0.0.1","root","a","student")

# prepare a cursor object using cursor() method
    cursor = db.cursor()

# execute SQL query using execute() method.
    command="""insert into student values(' """ + firstname + """ ',' """ + lastname + """ ',' """ + gender + """ ',' """ + project + """');"""

    cursor.execute(command)
    db.commit()

    command="""select * from student"""
    cursor.execute(command)
    row = cursor.fetchone()
    response="<html><center><h1>RECORDS IN DATABASE</h1></center><table border=\"1px\" align=\"center\">"
    response+=""" <thead>
    <td>First Name</td>
    <td>Last Name</td>
        <td>Gender</td>
    <td>Selected Project</td>
    </thead>"""
    while row is not None:
        response+="<tr>"
        for a in row:
         response+="<td>" + str(a) +"</td>"

        response+="</tr>"
        row = cursor.fetchone()


    return HttpResponse(response)

def printdata(request):
    db = MySQLdb.connect("127.0.0.1","root","a","student" )

# prepare a cursor object using cursor() method
    cursor = db.cursor()

    command="""select * from student"""
    cursor.execute(command)
    row = cursor.fetchone()
    response="<html><center><h1>RECORDS IN DATABASE</h1></center><table border=\"1\" align=\"center\">"
    response+=""" <thead>
    <td>First Name</td>
    <td>Last Name</td>
        <td>Gender</td>
    <td>Selected Project</td>
    </thead>"""
    while row is not None:
        response+="<tr>"
        for a in row:
         response+="<td>" + str(a) +"</td>"

        response+="</tr>"
        row = cursor.fetchone()


    return HttpResponse(response)