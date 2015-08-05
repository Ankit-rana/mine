from django.conf.urls import url,include

from . import views

urlpatterns=[
		url(r'^$',views.home,name='index'),#/
                url(r'^dashboard/$',views.index,name='home'),
		url(r'^auth/$',views.auth_view),
		url(r'^logout/$',views.logout_view),
		url(r'^data/$',views.getdata,name='data'),#/data
		url(r'^(?P<node_id>node[0-9]+)/$',views.clicked,name='node_index'),#/rajor/node
]
