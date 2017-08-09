
from django.conf.urls import url
from .import views
#print "hello"
urlpatterns = [

	url(r'^$',views.home,name='home'),
	
]
