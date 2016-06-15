from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404


def index(request):
    if request.method == 'GET':
        return render_to_response(
            'fuber/home.html', context_instance=RequestContext(request))
    else:
        raise Http404
