# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

def home(request): 
    return render_to_response('website/home.html', locals()
                              , context_instance=RequestContext(request))