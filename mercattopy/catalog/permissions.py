def is_admin(user):
    return user.is_authenticated and user.groups.filter(name='Admin').exists()

def is_operator(user):
    return user.is_authenticated and user.groups.filter(name='Operador').exists()