from django.db import models

# Create your models here
class Server(models.Model):
	server_ip=models.CharField(max_length=400)
	server_name=models.CharField(max_length=200)
	
	def __str__(self):
		return self.server_name
'''
class Node(models.Model):
	server=models.ForeignKey(Server)
	node_name=models.CharField(max_length=200)
	node_spec=models.CharField(max_length=200)
	node_id=models.CharField(max_length=300)
	hw_info=models.CharField(max_length=400,default=None)
	dhcp_mac=models.CharField(max_length=150,default=None)
	policy=models.CharField(max_length=800,default=None)
	log=models.CharField(max_length=200,default=None)
	tags=models.CharField(max_length=600,default=None)
	facts=models.CharField(max_length=1200,default=None)
	metadata=models.CharField(max_length=800,default=None)
	state=models.CharField(max_length=600,default=None)
	hostname=models.CharField(max_length=100,default=None)
	root_password=models.CharField(max_length=100,default=None)
	last_checkin=models.CharField(max_length=100,default=None
'''


class Node(models.Model):
	server=models.ForeignKey(Server)
	node_name=models.CharField(max_length=100,default=None)
	node=models.CharField(max_length=15000,default=None)
	def __str__(self):
		return self.node_name


class Dummy(models.Model):
	class Meta:
		permissions = (
                        ("view_console","can see console"),
                        ("view_metadata","can view and edit metadata"),
                        ("view_server","can view server"),
			("view_node","can view server's node")
                       )

		
