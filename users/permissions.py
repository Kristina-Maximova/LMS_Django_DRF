from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    """
    Проверяет, является ли пользователь модератором.
    """

    message = "Moderator can view and edit all courses and lessons."

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moderators").exists()


class IsOwner(permissions.BasePermission):
    """
    Проверяет, является ли пользователь владельцем.
    """

    message = "Owner can view, edit end delete only his courses end lessons."

    def has_object_permission(self, request, view, obj):
        return True if obj.owner == request.user else False
