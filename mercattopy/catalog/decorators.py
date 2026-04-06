from django.shortcuts import redirect
from django.contrib import messages

def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.groups.filter(name='Admin').exists():
            messages.error(request, 'Você não tem permissão para acessar esta página.')
            return redirect('dashboard')
        return view_func(request, *args, **kwargs)
    return wrapper