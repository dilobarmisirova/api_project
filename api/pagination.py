from rest_framework.pagination import LimitOffsetPagination


class PostLimitPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 10