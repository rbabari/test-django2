#from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello world! from members")


def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Members</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)