from django.contrib.auth.forms import AuthenticationForm  

def formulario_login(request):
    return {
        'bloque_formulario_login': AuthenticationForm(),
    }
