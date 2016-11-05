# from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.
# def index(request):
#     return HttpResponse('This is simple page')
import MySQLdb
from datetime import datetime
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .models import Project

MYSQL_IP = "djangowebserverdb.c2f5vwvu1xss.us-west-2.rds.amazonaws.com"
MYSQL_USER = "django"
MYSQL_PASSWORD = "django123"
MYSQL_DATABASE = "student"

def student(request):
    return render(request, 'Student.html', {'right_now':datetime.today()})

def user(request):
    return render(request,'index.html')

def Bootstrap(request):
    return render(request,'Bootstrap.html')

def faculty(request):
    return render(request, "faculty.html")

def register(request):
    name=request.GET.get('name','')
    gender=request.GET.get('gender','')
    email = request.GET.get('email','')    
    etnonym = request.GET.get('origin','')    
    race = request.GET.get('race','')    
    boulder_address = request.GET.get('Baddress','')    
    boulder_phone = request.GET.get('Bphone','')    
    summer_address = request.GET.get('Saddress','')    
    summer_phone = request.GET.get('Sphone','')    
    student_id = request.GET.get('studno','')    
    primary_major = request.GET.get('Pmajor','')    
    secondary_major = request.GET.get('Smajor','')
    gpa = request.GET.get('GPA','')
    level = request.GET.get('levelSchool','')
    graduation_year = request.GET.get('listGradYear','')
    previous_exp = request.GET.get('exp','')
    apprentice_info =request.GET.get('dla','')
    other_employment = request.GET.get('otherempl','')
    project1 = request.GET.get('project1','')
    project2 = request.GET.get('project2','')
    project3 = request.GET.get('project3','')
    project4 = request.GET.get('project4','')
    project5 = request.GET.get('project5','')
    background_check  = request.GET.get('backgroundcheck','')
    DandH_training = request.GET.get('training','')
    ssn = request.GET.get('SSN','')
    writeup1 = request.GET.get('writeup1','')
    writeup2 = request.GET.get('writeup2','')
    writeup3 = request.GET.get('writeup3','')
    resume = request.GET.get('resumeupload','')
    cover_letter = request.GET.get('coverletterupload','')

    db = MySQLdb.connect(MYSQL_IP,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DATABASE)

# prepare a cursor object using cursor() method
    cursor = db.cursor()

# execute SQL query using execute() method.
    command="""insert into student values(' """ + gender + """ ',' """ + student_id + """ ',' """ + name + """',' """ + etnonym + """',' """ + race + """',' """ + boulder_phone + """',' """ + boulder_address + """',' """ + email + """',' """ + summer_address + """',' """ + summer_phone + """',' """ + primary_major + """',' """ + secondary_major + """',' """ + gpa + """',' """ + level + """',' """ + graduation_year + """',' """ + previous_exp + """',' """ + apprentice_info + """',' """ + project1 + """',' """ + project2 + """',' """ + project3 + """',' """ + project4 + """',' """ + project5 + """',' """ + background_check + """',' """ + DandH_training + """',' """ + ssn + """',' """ + resume + """',' """ + cover_letter + """',' """ + writeup1 + """',' """ + writeup2 + """',' """ + writeup3 + """');"""

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
    db = MySQLdb.connect(MYSQL_IP,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DATABASE)
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


def addProject(request):
    project = Project()
    NULL = ""
    project.faculty_name=request.GET.get('name','')
    
    project.faculty_phone=request.GET.get('contact','')
    project.faculty_email=request.GET.get('email','')

    project.faculty_dept=request.GET.get('major','')
    project.edc_focus=request.GET.get('radiobutton','')
    project.sec_faculty_name=request.GET.get('name2','')
    project.sec_faculty_phone=request.GET.get('contact2','')
    project.sec_faculty_email=request.GET.get('email2','')
    project.sec_faculty_dept=request.GET.get('major2','')
    project.grad_student_name=request.GET.get('name3','')
    project.grad_student_number=request.GET.get('contact3','')
    project.grad_student_email=request.GET.get('email3','')
    project.title=request.GET.get('description','')
    project.url_link=request.GET.get('website','')
    project.special_req=request.GET.get('special_requirements','')
    project.long_description=request.GET.get('long_desc','').replace("\"","").replace("\'","")
    project.depts_applicable=request.GET.get('specialization','')
    project.amount_of_supervision=request.GET.get('sup','')
    project.supervision_by=request.GET.get('supv','')
    project.nature_of_work=request.GET.get('natw','')
    project.prior_work_experience=request.GET.get('workc','')
    project.desired_studend_id=request.GET.get('student','')
    project.speed_type=request.GET.get('finances','')
    project.accounting_contact=request.GET.get('account','')
    project.previous_dlc_exp=request.GET.get('radiobutton2','')
    project.save()

    
    return HttpResponseRedirect('/listOfProjects/')

def listOfProjects(request):
   
    departments_applicable = request.GET.get('depts_applicable','') 
    department_offerd = request.GET.get('department_offered','')
    query_results = Project.objects.all()
    if "ALL_DEP" in departments_applicable or "ALL_DEP" in department_offerd:
        pass
    elif departments_applicable :
    	query_results = query_results.filter(depts_applicable__contains=departments_applicable)
    elif department_offerd :
        query_results = query_results.filter(faculty_dept__contains=department_offerd) 
    #query_results = Project.objects.raw('SELECT project_id, title,faculty_name from project')
    return render(request,'listOfProjects.html',{'query_results':query_results}) 
