from .models import Project, Student, Faculty
from django.db.models import Q


class Algorithm(object):
    def getStudentGpaAbove3(self):
        self.eligible_students = Student.objects.filter(gpa__gte = '3.0')
        return self.eligible_students

    def getValidProjects(self):
        project_query = Project.objects.all()
        student_query = self.eligible_students
        valid_projects = []
        # project1 =
        for entry in project_query:
            query_set = student_query.filter(Q(project1__contains=entry.title)|Q(project2__contains=entry.title)
                                             |Q(project3__contains=entry.title)|Q(project4__contains=entry.title)
                                             |Q(project5__contains=entry.title))
            if query_set.exists():
                valid_projects.append(entry)

        return valid_projects






