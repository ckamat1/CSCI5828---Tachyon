# from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.
# def index(request):
#     return HttpResponse('This is simple page')
import MySQLdb
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render



MYSQL_IP = "127.0.0.1"
MYSQL_USER = "root"
MYSQL_PASSWORD = "topspin@123"
MYSQL_DATABASE = "student"

def home(request):
    return render(request, 'Student.html', {'right_now':datetime.today()})

def index(request):
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
    NULL = "NULL"
    name=request.GET.get('name','')
    print name
    contact_number=request.GET.get('contact','')
    email=request.GET.get('email','')

    dept=request.GET.get('major','')
    EDC_focus=request.GET.get('radiobutton','')
    S_faculty_name=request.GET.get('name2','')
    S_faculty_phone=request.GET.get('contact2','')
    S_faculty_email=request.GET.get('email2','')
    S_faculty_dept=request.GET.get('major2','')
    GS_name=request.GET.get('name3','')
    GS_phone=request.GET.get('contact3','')
    GS_email=request.GET.get('email3','')
    title=request.GET.get('description','')
    website=request.GET.get('website','')
    special_requirements=request.GET.get('special_requirements','')
    long_desc=request.GET.get('long_desc','')
    specialization=request.GET.get('specialization','')
    supervision=request.GET.get('sup','')
    supervision_by=request.GET.get('supv','')
    Nature=request.GET.get('natw','')
    prior_work=request.GET.get('workc','')
    student_desired=request.GET.get('student','')
    finances=request.GET.get('finances','')
    account=request.GET.get('account','')
    past_DLC=request.GET.get('radiobutton2','')

    db = MySQLdb.connect(MYSQL_IP,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DATABASE)
    cursor = db.cursor()
    command="""insert into project values(' """ + NULL + """ ',' """ + name + """ ',' """ + contact_number + """',' """ + email + """',' """ + dept + """',' """ + EDC_focus + """',' """ + S_faculty_name + """',' """ + S_faculty_phone + """',' """ + S_faculty_email + """',' """ + GS_name + """',' """ + GS_phone + """',' """ + GS_email + """',' """ + S_faculty_dept + """',' """ + title + """',' """ + website + """',' """ + special_requirements + """',' """ + long_desc + """',' """ + specialization + """',' """ + supervision + """',' """ + supervision_by + """',' """ + Nature + """',' """ + prior_work + """',' """ + student_desired + """',' """ + finances + """',' """ + account + """',' """ + past_DLC + """');"""
    cursor.execute(command)
    db.commit()

    command="""select faculty_name,title,description from project"""
    cursor.execute(command)
    row = cursor.fetchone()
    response="<html><center><h1>RECORDS IN DATABASE</h1></center><table border=\"1px\" align=\"center\">"
    response+=""" <thead>
    <td>faculty name</td>
    
    <td>title</td>
    </thead>"""
    while row is not None:
        response+="<tr>"
        for a in row:
         response+="<td>" + str(a) +"</td>"

        response+="</tr>"
        row = cursor.fetchone()


    return HttpResponse(response)
