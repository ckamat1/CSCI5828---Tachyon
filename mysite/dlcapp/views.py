# from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.
# def index(request):
#     return HttpResponse('This is simple page')
import MySQLdb
from datetime import datetime
from django.http import HttpResponse,HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import loader
from .models import Project
from .models import Student
from django.db.models import Q
import tablib
from .Algorithm import Algorithm

MYSQL_IP = "djangowebserverdb.c2f5vwvu1xss.us-west-2.rds.amazonaws.com"
MYSQL_USER = "django"
MYSQL_PASSWORD = "django123"
MYSQL_DATABASE = "student"

def student(request):
    if request.user.is_authenticated():
        query_results = Project.objects.all()
        return render(request, 'Student.html', {'right_now':datetime.today(),'query_results':query_results})
    else:
        raise Http404("You need to login to view this page!")

def user(request):
    if request.user.is_authenticated():
        return render(request,'index.html')
    else:
        raise Http404("You need to login to view this page!")


def Bootstrap(request):
    return render(request,'Bootstrap.html')

def faculty(request):
    if request.user.is_authenticated():
        return render(request, "faculty.html")
    else:
        raise Http404("You need to login to view this page!")


def register(request):
    if request.user.is_authenticated():
        application = Student()
        application.name=request.GET.get('name','')
        application.gender=request.GET.get('gender','')
        application.email_id = request.GET.get('email','')
        application.ethnonym = request.GET.get('origin','')
        application.race = request.GET.get('race','')
        application.boulder_address = request.GET.get('Baddress','')
        application.boulder_phone = request.GET.get('Bphone','')
        application.summer_address = request.GET.get('Saddress','')
        application.summer_phone = request.GET.get('Sphone','')
        application.studentid = request.GET.get('studno','')
        application.primary_major = request.GET.get('Pmajor','')
        application.secondary_major = request.GET.get('Smajor','')
        application.gpa = request.GET.get('GPA','')
        application.school_level = request.GET.get('levelSchool','')
        application.graduation_year = request.GET.get('listGradYear','')
        application.previous_research_exp = request.GET.get('exp','')
        application.previous_dlc_apply =request.GET.get('dla','')
        application.other_employment = request.GET.get('otherempl','')
        application.project1 = request.GET.get('project1','')
        application.project2 = request.GET.get('project2','')
        application.project3 = request.GET.get('project3','')
        application.project4 = request.GET.get('project4','')
        application.project5 = request.GET.get('project5','')
        application.background_check  = request.GET.get('backgroundcheck','')
        application.dandh_awarness = request.GET.get('training','')
        application.ssn = request.GET.get('SSN','')
        application.skills1 = request.GET.get('writeup1','')
        application.skills2 = request.GET.get('writeup2','')
        application.skills3 = request.GET.get('writeup3','')
        application.resume_name = request.GET.get('resumeupload','')
        application.cover_letter_name = request.GET.get('coverletterupload','')
        application.save()

        return HttpResponseRedirect('/listOfProjects/')
    else:
        raise Http404("You need to login to view this page!")

def printdata(request):
    if request.user.is_authenticated():
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
    else:
        raise Http404("You need to login to view this page!")


def addProject(request):
    if request.user.is_authenticated():
        project = Project()
        NULL = ""
        project.faculty_name=request.GET.get('name','')

        project.faculty_phone=request.GET.get('contact','')
        project.faculty_email=request.GET.get('email','')

        project.faculty_dept=request.GET.get('major1','')
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
        project.depts_applicable=request.GET.getlist('specialization')
        project.amount_of_supervision=request.GET.get('sup','')
        project.supervision_by=request.GET.get('supv','')
        project.nature_of_work=request.GET.get('natw','')
        project.prior_work_experience=request.GET.get('workc','')
        project.desired_student_id=request.GET.get('student','')
        project.speed_type=request.GET.get('finances','')
        project.accounting_contact=request.GET.get('account','')
        project.previous_dlc_exp=request.GET.get('radiobutton2','')
        project.save()


        return HttpResponseRedirect('/listOfProjects/')
    else:
        raise Http404("You need to login to view this page!")

def listOfProjects(request):
    if request.user.is_authenticated():
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
    else:
        raise Http404("You need to login to view this page!")


def filterStudentForm(request):
    if request.user.is_authenticated():
        filterDepartment = request.GET.get('dept_choosen','')
        query_results = Project.objects.all()
        query_results = list(query_results.filter(depts_applicable__contains=filterDepartment))
        query_results = [ x.title for x in query_results]
        str = ','
        result = str.join(query_results)
        return HttpResponse(result)
    else:
        raise Http404("You need to login to view this page!")


def studentProjectMap(request):
    query_results = Project.objects.all()
    student_query = Student.objects.all()
    for entry in query_results:
        entry.student_selected = "NA"
        max_gpa = 0.0
        for student in student_query.filter(project1__contains=entry.title):
            if float(student.gpa) > max_gpa:
                max_gpa = float(student.gpa)
                entry.student_selected= student.name
        for student in student_query.filter(project2__contains=entry.title):
            if float(student.gpa) > max_gpa:
                max_gpa = float(student.gpa)
                entry.student_selected= student.name

        for student in student_query.filter(project3__contains=entry.title):
            if float(student.gpa) > max_gpa:
                max_gpa = float(student.gpa)
                entry.student_selected= student.name

        for student in student_query.filter(project4__contains=entry.title):
            if float(student.gpa) > max_gpa:
                max_gpa = float(student.gpa)
                entry.student_selected= student.name

        for student in student_query.filter(project5__contains=entry.title):
            if float(student.gpa) > max_gpa:
                max_gpa = float(student.gpa)
                entry.student_selected= student.name


        entry.student = student_query.filter(Q(project1__contains=entry.title)|Q(project2__contains=entry.title)|Q(project3__contains=entry.title)|Q(project4__contains=entry.title)|Q(project5__contains=entry.title))   
        project = Project.objects.get(project_id=entry.project_id)
        if project.student_assigned :
            entry.student_selected = project.student_assigned

    return render(request,'studentProjectMap.html',{'query_results':query_results}) 

def modifyMapping(request):
    student_choice = request.GET.get('student_choice','')    
    project_name = request.GET.get('project_title','') 
    query_result = Project.objects.all().filter(title__contains=project_name)
    for entry in query_result:
        project = Project.objects.get(project_id=entry.project_id)
        project.student_assigned = student_choice
        project.save()

    return HttpResponseRedirect('/studentProjectMap/') 
        
def exportMapping(request):
    #headers = ('Name', 'GPA')
    studentFields = 2
    data = []
    data = tablib.Dataset(*data )
    projects = Project.objects.all()
    projectsList = []
    for emptySpace in range(studentFields):
        projectsList.append("")
    for project in projects:
        projectsList.append(project.title)
    projectsTotal = len(projects)
    data.append(tuple(projectsList))
    students = Student.objects.all()
    for student in students:
        studentTuple = [ ]
        studentTuple.append(student.name)
        studentTuple.append(student.gpa)
        for emptySpace in range(projectsTotal):
            studentTuple.append("")
        data.append(tuple(studentTuple))
    response = HttpResponse(data.xls, content_type='application/vnd.ms-excel;charset=utf-8')
    response['Content-Disposition'] = "attachment; filename=exportMapping.xls"
    return response  


# def StudentProjectMap_new(request):
#     algorithm = Algorithm()
#     student_query = algorithm.getStudentGpaAbove3()
#     project_query = algorithm.getValidProjects()
#     response = HttpResponse()
#     # for student in student_query:
#     #     response.write(student.name)
#     for proj in project_query:
#         response.write(proj.title)
#     return response