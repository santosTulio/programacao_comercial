import logging

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

logger = logging.getLogger(__name__)
# Create your views here.
class Login(View):
    def get(self,request):
        contexto = {
            'usuario': '',
            'senha': ''
        }
        return render(request,'login/login.html',contexto)