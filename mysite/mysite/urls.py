from django.conf.urls import url
from django.contrib import admin
# from django.views.generic import TemplateView

# from dlcapp.views import register, home, printdata
from dlcapp import views
from .views import HomepageView, SignUpView
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
               url(r'^accounts/register/', SignUpView.as_view(),name='Signup')]