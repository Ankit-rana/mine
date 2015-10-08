from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from node_informer.models import Server,Node 
import urllib2
import json
from django.template import RequestContext,loader
from django.contrib.auth import authenticate,login,logout
from django.core.context_processors import csrf
from django.contrib import messages



# Create your views here.

def home(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/dashboard')
	else: 
		template=loader.get_template('node_informer/home.html')
		context = RequestContext(request)
        	return HttpResponse(template.render(context))




def getdata(request):
	node_list=[]
	Node.objects.all().delete()
	list=Server.objects.all()
	for item in list:
		raw_json=urllib2.urlopen(item.server_ip)
		info=json.load(raw_json)
		node_list=info["items"]
		for node in node_list:
			raw=urllib2.urlopen(node['id'])
			node_info=json.dumps(json.load(raw))
			n=Node(server_id=item.id,node_name=node['name'],node=node_info)
			n.save()
	return  redirect('/dashboard')



def index(request):
	if request.user.is_authenticated():
		server_list=Server.objects.all()
		node_list=Node.objects.all()
		template=loader.get_template('node_informer/index.html')
		context = RequestContext(request,{
						'server_list':server_list,
						'node_list':node_list,
						'full_name':request.user.first_name,
						})
		return HttpResponse(template.render(context))
	else :
		messages.error(request,'please login to access')
		return HttpResponseRedirect('/')


def clicked(request,node_id):
	server_list=Server.objects.all()
        node_list=Node.objects.all()
	obj=node_list.get(node_name=node_id).node
	current_node=json.dumps(json.loads(obj))
	template=loader.get_template('node_informer/node_index.html')
	context = RequestContext(request,{'current':current_node,
					'server_list':server_list,
					'node_list':node_list,
		
	})				
	return HttpResponse(template.render(context))


def auth_view(request):
    	username = request.POST['username']
	password = request.POST['password']
    	user = authenticate(username=username, password=password)
    	if user is not None:
	 if user is not None:
                login(request,user)
                if 'remember' in request.POST:
                        remember = request.POST['remember']
                        request.session.set_expiry(0)
            	return HttpResponseRedirect('/dashboard/')
	else:
		messages.error(request,'please provide correct username and password')
		return HttpResponseRedirect('/')	


def logout_view(request):
	logout(request)
	messages.error(request,'you have logged out')
	return HttpResponseRedirect('/')



def test(request):	
	return HttpResponse("working")
