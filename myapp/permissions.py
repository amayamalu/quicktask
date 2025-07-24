from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'

class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'manager'

class IsMember(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'member'
