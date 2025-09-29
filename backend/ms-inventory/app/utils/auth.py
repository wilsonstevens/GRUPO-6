from flask import request, jsonify

def check_inventory_permission():
    """
    Valida si el usuario que hace la petición tiene privilegios sobre inventarios.
    Se espera que en el header Authorization o X-User-Role venga el rol del usuario.
    """
    role = request.headers.get('X-User-Role')  # o Authorization / JWT

    if not role:
        return False, 'No se proporcionó el rol del usuario'

    # Aquí defines tus reglas
    allowed_roles = ['admin', 'inventory_manager']  # roles válidos para inventarios

    if role not in allowed_roles:
        return False, f'El rol {role} no tiene permisos sobre inventarios'

    return True, None
