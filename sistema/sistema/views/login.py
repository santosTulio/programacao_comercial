import logging

from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View

logger = logging.getLogger(__name__)
# Create your views here.
class Login(View):
    def get(self,req):
        contexto = {
            'usuario': '',
            'senha': ''
        }
        return render(req,'login/login.html',contexto)

    def post(self, req):
        usuario=req.POST.get('usuario', None)
        senha = req.POST.get('senha',None)
        logger.info(f"Usuario: {usuario}")
        logger.info(f"Senha: {senha}")
        user = authenticate(req, username=usuario,password=senha)
        if user:
            if user.is_active:
                login(req,user)
                return redirect('/veiculos')
            return render(req,'login/login.html',{})
        return render(req,'login/login.html',{})