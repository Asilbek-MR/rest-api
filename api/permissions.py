from rest_framework import permissions

class IsStaffEditorPermisson(permissions.DjangoModelPermissions):
    perms_map = {
        'GET':['%(app_label)s.view_%(model_name)s'],
        'OPTIONS':[],
        'HEAD': [],
        'POST':['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_lables)s.change_%(model_name)s'],
        'PATCH': ['%(app_lables)s.change_%(model_name)s'],
        'DELETE': ['%(app_lables)s.delete_%(model_name)s'],
    }


