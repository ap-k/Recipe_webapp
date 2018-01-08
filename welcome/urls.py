from django.conf.urls import url
from.import views

urlpatterns = [
   # /welcome/
    url(r'^$',views.index, name='index'),
#/welcome/index1
    url(r'^index1$',views.detail, name='index1'),

     url(r'^r1$', views.fr1, name='r1'),
     url(r'^r2$', views.fr2, name='r2'),
     url(r'^r3$', views.fr3, name='r3'),
     url(r'^r4$', views.fr4, name='r4'),
     url(r'^rr2$', views.frr2, name='rr2'),
     url(r'^rr3$', views.frr3, name='rr3'),
     url(r'^rr4$', views.frr4, name='rr4'),
     url(r'^rshow$', views.frshow, name='rshow'),
     url(r'^rshow2$', views.frshow2, name='rshow2'),
     url(r'^rshow3$', views.frshow3, name='rshow3'),
     url(r'^rr2.html' ,views.frr2, name='rr2')

]
