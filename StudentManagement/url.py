from django.contrib.auth.views import login, logout

from StudentManagement import views
from django.conf.urls import url, handler404

handler404 = "views.error"

urlpatterns=[
    url(r'login/$', login, name='login'),
    url(r'logout/$', logout, {'next_page': '/attendance/login/'}),
    url(r'home/$', views.home, name="home"),
    url(r'welcome/$', views.loginhome),
    url(r'error/(?P<msg>[a-z A-Z 0-9]*)/$', views.error),
    url(r'signup/$', views.signup, name="signup"),
    url(r'addperiods/', views.addperiods, name="add"),
    url(r'schedule/', views.faculty_view, name="schedule"),
    url(r'class/(?P<cid>[0-9]+)/subject/(?P<sid>[0-9]+)', views.class_view, name="update_attend")

]