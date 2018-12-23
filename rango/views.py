from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext

def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I`m bold font from the context"}


    return render_to_response('rango/index.html', context_dict, context)

def about(request):
    return HttpResponse("Rango says: Here is the about page.")

# Create your views here.
