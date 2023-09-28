from rest_framework.permissions import BasePermission, SAFE_METHODS


class RestaurantPermission(BasePermission):

    def has_permission(self, request, view):

        if request.method == 'GET':
            return True

        else:
            return request.user.is_staff

    def has_object_permission(self, request, view, obj):

        if request.method == 'GET':
            return True
        else:
            return request.user.is_staff
