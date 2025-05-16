from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
# autenticacao/views.py



from django.db.models import Q

from core.models import Laboratorio

User = get_user_model()


from django.contrib.auth import authenticate, login


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        # Pegando os dados do formulário
        username = request.POST.get('email')  # 'email' no seu formulário
        password = request.POST.get('password')
        
        # Autenticando o usuário
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Se o usuário for autenticado, loga no sistema
            login(request, user)
            return HttpResponseRedirect(reverse('main'))  # Redirecionar para a página inicial ou página principal
        else:
            # Se o login falhar
            messages.error(request, "Credenciais inválidas. Tente novamente.")
            return render(request, 'authentication.html')  # Retorna para a página de login com a mensagem de erro.
    
    return render(request, 'authentication.html')  # Exibe o formulário de login caso seja um GET



@csrf_protect
def deslogar(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'authentication.html')
    return redirect('main')


def csrf_failure(request, reason=""):
    return render(request, 'csrf_failure.html', status=403)