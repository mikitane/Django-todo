from django.conf.urls import url
from todos import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$',views.register,name='register'),
    url(r'^logout/$', views.log_out,name='logout'),
    url(r'^todos/api/$', views.ToDoView.as_view()),
    ]
