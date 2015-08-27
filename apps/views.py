from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Eventually this will show apps with a select option and network map.")

def app(request, app_id):
    return HttpResponse("You're looking at application %s." % app_id)

def servers(request):
    return HttpResponse("Shows all the servers.")
    
def server(request, server_id):
    response = "You're looking at the details for the server %s."
    return HttpResponse(response % server_id)

def services(request):
    return HttpResponse("Shows all the services.")
    
def service(request, service_id):
    return HttpResponse("You're looking at the details for the service %s." % service_id)

def skills(request):
    return HttpResponse("List of all skills.")
