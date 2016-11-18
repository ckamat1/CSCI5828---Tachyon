from django.conf.urls import url
from django.contrib import admin
# from django.views.generic import TemplateView
from dlcapp import views
from .views import HomepageView, SignUpView, LoginView, LogoutView, RegisterSuccess
admin.autodiscover()

# urlpatterns = [url(r'^register/', views.register, name='register'),
#                url(r'^viewrecords/',views.printdata, name='print_data'),
#                url(r'^$', views.index, name='home'),
#                # url(r'^$',views.home, name='home'),
#                # url(r'^faculty/', TemplateView.as_view(template_name='faculty.html'),
#                #        name='faculty'),
#                url(r'^admin/', include(admin.site.urls)),
# 		url(r'^faculty/',views.faculty,name='faculty'),
# 		url(r'^home/',views.home,name='student'),
# 		url(r'^addProject/',views.addProject,name='addProject'),
# 		url(r'^listOfProjects/',views.listOfProjects,name='addProject'),
# ]


urlpatterns = [url(r'^$',HomepageView.as_view(),name='home'),
               url(r'^register/',views.register, name='register'),
               url(r'^user/',views.user,name='user'),
               url(r'^register_success/',RegisterSuccess,name='Success'),
               url(r'^faculty/',views.faculty,name='faculty'),
               url(r'^student/',views.student,name='student'),
               url(r'^listOfProjects/',views.listOfProjects,name='projects'),
               url(r'^filterStudentForm/',views.filterStudentForm,name='filter'),
               url(r'^studentProjectMap/',views.studentProjectMap,name='matrix'),
               url(r'^modifyMapping/',views.modifyMapping,name='modify'),
               url(r'^addProject/',views.addProject,name='addProject'),
               url(r'^accounts/register/', SignUpView.as_view(),name='Signup'),
               url(r'^accounts/login/', LoginView.as_view(), name='Login'),
               url(r'^accounts/logout/', LogoutView.as_view(),name='Logout')]
