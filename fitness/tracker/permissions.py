from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Allow users to view all, but only edit/delete their own account.
    Superusers can edit/delete anyone.
    """

    def has_object_permission(self, request, view, obj):
        # Everyone can read
        if request.method in permissions.SAFE_METHODS:
            return True

        # Superusers can edit/delete anyone
        if request.user.is_superuser:
            return True

        # If the object is a user, check directly
        if hasattr(obj, "id") and obj == request.user:
            return True

        # If the object has a `.user` field (like FitnessData), check ownership
        if hasattr(obj, "user") and obj.user == request.user:
            return True

        return False
