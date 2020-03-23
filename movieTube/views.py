from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


def index(request):
    template = loader.get_template('./index.html')
    context = {}
    return HttpResponse(template.render(context, request))
    return render(request, './index.html', context)
