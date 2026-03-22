from rest_framework import permissions


class IsInGroupOrReadOnly(permissions.BasePermission):
    """Allow safe methods to anyone, but write methods only to users in allowed groups.

    Expected that view may set `allowed_groups` attribute as a list of group names.
    If not set, default to allow authenticated users to write.
    """

    def has_permission(self, request, view):
        # Safe methods allowed
        if request.method in permissions.SAFE_METHODS:
            return True

        # If not authenticated, deny
        if not request.user or not request.user.is_authenticated:
            return False

        allowed = getattr(view, 'allowed_groups', None)
        if not allowed:
            return True

        user_groups = set(g.name for g in request.user.groups.all())
        return bool(user_groups.intersection(set(allowed)))
