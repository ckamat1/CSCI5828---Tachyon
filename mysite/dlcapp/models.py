# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.ForeignKey(AuthGroup)
    permission_id = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.ForeignKey(AuthUser)
    group_id = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.ForeignKey(AuthUser)
    permission_id = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Avinash(models.Model):
    test = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'avinash'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Faculty(models.Model):
    facultyid = models.CharField(db_column='facultyID', primary_key=True, max_length=60)  # Field name made lowercase.
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    department = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faculty'


class Project(models.Model):
    faculty_name = models.CharField(max_length=60, blank=True, null=True)
    faculty_phone = models.CharField(max_length=60, blank=True, null=True)
    faculty_email = models.CharField(max_length=60, blank=True, null=True)
    faculty_dept = models.CharField(max_length=60, blank=True, null=True)
    edc_focus = models.CharField(db_column='EDC_focus', max_length=5, blank=True, null=True)  # Field name made lowercase.
    sec_faculty_name = models.CharField(max_length=60, blank=True, null=True)
    sec_faculty_phone = models.CharField(max_length=20, blank=True, null=True)
    sec_faculty_email = models.CharField(max_length=20, blank=True, null=True)
    grad_student_name = models.CharField(max_length=20, blank=True, null=True)
    grad_student_number = models.CharField(max_length=20, blank=True, null=True)
    grad_student_email = models.CharField(max_length=20, blank=True, null=True)
    sec_faculty_dept = models.CharField(max_length=20, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    url_link = models.CharField(max_length=200, blank=True, null=True)
    special_req = models.CharField(max_length=1500, blank=True, null=True)
    long_description = models.CharField(max_length=1500, blank=True, null=True)
    depts_applicable = models.CharField(max_length=200, blank=True, null=True)
    amount_of_supervision = models.CharField(max_length=200, blank=True, null=True)
    supervision_by = models.CharField(max_length=200, blank=True, null=True)
    nature_of_work = models.CharField(max_length=200, blank=True, null=True)
    prior_work_experience = models.CharField(max_length=200, blank=True, null=True)
    desired_studend_id = models.CharField(max_length=200, blank=True, null=True)
    speed_type = models.CharField(max_length=200, blank=True, null=True)
    accounting_contact = models.CharField(max_length=50, blank=True, null=True)
    previous_dlc_exp = models.CharField(db_column='previous_DLC_exp', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'project'


class Sample(models.Model):
    sample = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sample'


class Student(models.Model):
    gender = models.CharField(max_length=8, blank=True, null=True)
    studentid = models.CharField(db_column='studentID', max_length=60, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=60, blank=True, null=True)
    ethnonym = models.CharField(max_length=60, blank=True, null=True)
    race = models.CharField(max_length=60, blank=True, null=True)
    boulder_phone = models.CharField(max_length=20, blank=True, null=True)
    boulder_address = models.CharField(max_length=160, blank=True, null=True)
    email_id = models.CharField(max_length=40, blank=True, null=True)
    summer_address = models.CharField(max_length=160, blank=True, null=True)
    summer_phone = models.CharField(max_length=20, blank=True, null=True)
    primary_major = models.CharField(max_length=40, blank=True, null=True)
    secondary_major = models.CharField(max_length=40, blank=True, null=True)
    gpa = models.CharField(max_length=5, blank=True, null=True)
    school_level = models.CharField(max_length=20, blank=True, null=True)
    graduation_date = models.CharField(max_length=20, blank=True, null=True)
    previous_research_exp = models.CharField(max_length=2, blank=True, null=True)
    previous_dlc_apply = models.CharField(db_column='previous_DLC_apply', max_length=2, blank=True, null=True)  # Field name made lowercase.
    project1 = models.CharField(max_length=10, blank=True, null=True)
    project2 = models.CharField(max_length=10, blank=True, null=True)
    project3 = models.CharField(max_length=10, blank=True, null=True)
    project4 = models.CharField(max_length=10, blank=True, null=True)
    project5 = models.CharField(max_length=10, blank=True, null=True)
    background_check = models.CharField(max_length=2, blank=True, null=True)
    dandh_awarness = models.CharField(db_column='DandH_awarness', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ssn = models.CharField(db_column='SSN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    resume_name = models.CharField(max_length=10, blank=True, null=True)
    cover_letter_name = models.CharField(max_length=10, blank=True, null=True)
    skills1 = models.CharField(max_length=100, blank=True, null=True)
    skills2 = models.CharField(max_length=100, blank=True, null=True)
    skills3 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'
