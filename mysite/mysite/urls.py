from django.conf.urls import *
from django.contrib import admin
from django.views.generic import TemplateView

# from dlcapp.views import register, home, printdata
from dlcapp import views
admin.autodiscover()

urlpatterns = [url(r'^register/', views.register, name='register'),
               url(r'^viewrecords/',views.printdata, name='print_data'),
               url(r'^$', views.index, name='home'),
               # url(r'^$',views.home, name='home'),
               # url(r'^faculty/', TemplateView.as_view(template_name='faculty.html'),
               #        name='faculty'),
               url(r'^admin/', include(admin.site.urls)),
		url(r'^faculty/',views.faculty,name='faculty'),
		url(r'^home/',views.home,name='student'),
]
