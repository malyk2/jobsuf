from rest_framework import permissions

class SecretGetSavePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.has_perm('rss.view_secret')
        return request.user.has_perm('rss.change_secret')