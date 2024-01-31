from rest_framework import permissions

class IsOwnerOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return True
        #return super().has_permission(request, view)
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        
        return obj.user == request.user
        #return super().has_object_permission(request, view, obj)