from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "app/index.html")

def usuarios(request):
    lista_usuarios = [{"nome": "Michael Douglas", "idade": 23, "matricula": "2000181110001", "cidade": "Viena"},
        {"nome": "James Wilson", "idade": 55, "matricula": "2700181110003", "cidade": "Madrid"},
        {"nome": "Peter Parker", "idade": 22, "matricula": "2090181110011", "cidade": "Luxemburgo"},
        {"nome": "Karl Marx", "idade": 64, "matricula": "2010181110004", "cidade": "Macau"},
        {"nome": "Friedrich Engels", "idade": 74, "matricula": "2009181110012", "cidade": "SPP"},]
    context = {"usuarios": lista_usuarios}
    return render(request, "app/usuarios.html", context)