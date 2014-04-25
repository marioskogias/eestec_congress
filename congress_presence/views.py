# Create your views here.
from django.shortcuts import render_to_response
from django.views.generic import View

class BaseView(View):

    def get(self, request):
        return render_to_response('index.html', {'name':"Marios"})
