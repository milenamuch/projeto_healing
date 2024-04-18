from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth

#CADASTRO
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
         username = request.POST.get('username')
         email = request.POST.get('email')
         senha = request.POST.get('senha')
         confirmar_senha = request.POST.get("confirmar_senha")

         if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, "As senhas devem coincidir.")
            return redirect('/usuarios/cadastro/')
        
    if len(senha) < 6:
        messages.add_message(request, constants.ERROR, "As senha deve possuir mais de 6 caracteres.")
        #UX: informar quantidade mínima de caracteres abaixo do input
        return redirect('/usuarios/cadastro/')
    
    users = User.objects.filter(username = username)
    if users.exists():
        messages.add_message(request, constants.ERROR, "Já existe um usuário cadastrado com este nome")
        #UX: token mostrando que o usuário já existe e redirecionar para a tela de login
        return redirect('/usuarios/cadastro/')
    
    user = User.objects.create_user(
        username = username,
        email = email,
        password = senha
    )

    return redirect('/usuarios/login/')

#LOGIN
def login_view(request):
    if request.method == "GET":
        return render (request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(request, username = username, password = senha)

        if user:
            auth.login(request, user)
            return redirect('/pacientes/home')
        
        messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')
        return redirect('/usuarios/login/')
    
#LOGOUT
def sair (request):
    auth.logout(request)
    print(request.user.is_authenticated)
    return redirect('/usuarios/login/')