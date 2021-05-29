from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.forms import forms


class FormularioLogin(AuthenticationForm):
    username = UsernameField(
        label='Usuario',
        widget=forms.TextInput(attrs={'autofocus': True})
    )


def formulario_login(request):
    return {
        'bloque_formulario_login': FormularioLogin(),
    }
