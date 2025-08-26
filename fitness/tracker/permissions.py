from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit or delete it.
    """
    def has_object_permission(self, request, view, obj):
        # Safe methods = GET, HEAD, OPTIONS (everyone can view)
        if request.method in permissions.SAFE_METHODS:
            return True
        #Tht is right
        # Otherwise, only the owner can edit/delete
        return obj.user == request.user
    
