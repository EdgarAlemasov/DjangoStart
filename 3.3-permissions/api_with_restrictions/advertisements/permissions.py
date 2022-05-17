from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return request.user == obj.creator
