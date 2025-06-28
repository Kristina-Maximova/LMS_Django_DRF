from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    message = 'Moderator can view and edit all courses and lessons.'

    def has_permission(self, request, view):
        return request.user.groups.filter(name='moderators').exists()


class IsOwner(permissions.BasePermission):
    message = 'Owner can view, edit end delete only his courses end lessons.'

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
