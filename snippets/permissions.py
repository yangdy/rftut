from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
  """
  Custom permisson to only owners of an object to edit it.
  """

  def has_object_permission(self, request, view, obj):
    # Read permissions are allower to any request,
    # so we'll always allow GET, HEAD or OPTIONS request.
    if request.method in permissions.SAFE_METHODS:
      return True

    return obj.owner == request.user
