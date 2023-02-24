#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def members(request):
    return HttpResponse("Hello world! from members")


def index(request):
    now = "Members"
    html = f'''
    <html>
        <body>
            <h1>Hello from Members</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)



def membersFromtemplate(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())