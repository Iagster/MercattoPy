from django.core.exceptions import PermissionDenied

def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.groups.filter(name='Admin').exists():
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return wrapper