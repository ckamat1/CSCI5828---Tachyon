from .models import Project, Student, Faculty
from django.db.models import Q
import re

class stud:
    def __init__(self, app_ID):
        self.app_ID = app_ID
        self.priority = 0

def getValidStudentAndProjects():
    eligible_students = Student.objects.filter(gpa__gte='3.0').filter(pastdla_experience__contains='No') \
        .filter(student_commitment__contains='Yes').filter(student_ispart_engineering__contains='Yes')
    # Need to eliminate students who have past DLA experience, who are grad students and who are not a part of CU engineering.
    project_query = Project.objects.all()
    student_query = eligible_students
    valid_projects = []
    for entry in project_query:
        query_set = student_query.filter(Q(project1__contains=entry.title) | Q(project2__contains=entry.title)
                                         | Q(project3__contains=entry.title) | Q(project4__contains=entry.title)
                                         | Q(project5__contains=entry.title))
        if query_set.exists():
            valid_projects.append(entry)
    return eligible_students,valid_projects



class Algorithm(object):
    def __init__(self):
        self.eligible_students,self.valid_projects = getValidStudentAndProjects()
        # self.valid_projects = None

    def Match(self):
        query_results = self.valid_projects
        eligible_students = self.eligible_students
        #student_with_max_GPA = 0.0
        student_level = {'Senior':4,'Junior':3,'Sophomore':2,'Freshman':1}

        for entry in query_results:
            entry.student = eligible_students.filter(Q(project1__contains=entry.title)|Q(project2__contains=entry.title)
                                             |Q(project3__contains=entry.title)|Q(project4__contains=entry.title)
                                             |Q(project5__contains=entry.title))
            # entry.student_selected = "NA"
            entry.student_assigned = "NA"
            students_dict = {'Student':None,'Priority':0}
            # priority = 0
            for student in entry.student:
                std = stud(student.application_id)
                std.priority += float(student.gpa)
                if student.school_level:
                    std.priority += student_level[student.school_level]
                if student.previous_dlc_apply == "Yes":
                    std.priority += 1
                if entry.desired_student_id == student.name:
                    std.priority += 1
                if student.gender == "female":
                    std.priority += 1
                if student.ethnonym == "Yes":
                    std.priority += 1
                if student.project1 == entry.title:
                    std.priority += 5
                elif student.project2 == entry.title:
                    std.priority += 4
                elif student.project3 == entry.title:
                    std.priority += 3
                elif student.project4 == entry.title:
                    std.priority += 2
                else:
                    std.priority += 1

                if std.priority > students_dict['Priority']:
                    students_dict['Student'] = std
                    students_dict['Priority'] = std.priority

            final_student = students_dict['Student']
            student_selected =  entry.student.get(application_id=final_student.app_ID)
            # entry.student_selected = student_selected.name
            entry.student_assigned = student_selected.name
            entry.save()
        return query_results


















