from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
# Create your views here.
from .models import Reporter

def index(request):
    template = loader.get_template("citizen/detail.html")
    context = {"CONTEXT":1}
    return HttpResponse(template.render(context,request))

def report(request, reporter_id):
    return HttpResponse("You are going to report with reporter_id %s." % reporter_id)


def detail(request,reporter_id):
    reporter = get_object_or_404(Reporter,pk=reporter_id)
    return render(request,"citizen/detail.html",{"reporter":reporter})


def interface(request,reporter_id):
    reporter = get_object_or_404(Reporter, pk=reporter_id)
    return render(request, "citizen/interface.html", {"reporter": reporter})