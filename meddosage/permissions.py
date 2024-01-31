from rest_framework import permissions

class IsOwnerOnly(permissions.BasePermission):
    """
    Custom permission to only allow users of an object to edit ot
    """
    def has_permission(self, request, view):
        return True
        #return super().has_permission(request, view)
    
    def has_object_permission(self, request, view, obj):
        
        # Read permissions are allowed to any user requsr
        # we will  always allow GET, HEAD or OPTIONS request

        if request.method in permissions.DjangoObjectPermissions:
            return True
        
        # write permissions are only allowed to the owner of the object        
        return obj.user == request.user
        #return super().has_object_permission(request, view, obj)