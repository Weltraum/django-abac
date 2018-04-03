# import base64
# import binascii
#
# from urllib.parse import unquote_plus
#
# from django.contrib.auth import authenticate
# from django.contrib.auth.middleware import get_user
# from django.urls import resolve
# from django.utils.functional import SimpleLazyObject, LazyObject
# from django.http import HttpResponse
# from django.conf import settings
from django.contrib.auth.models import AnonymousUser


from abac.settings import abac_settings, import_from_string


class ABACMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.user = self.get_auth_user(request)
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        return None
        # subject = request.user
        # resource = resolve(request.path)._func_path
        #
        # # Ограничения распространяются только на основное приложение
        # if resource.split('.')[0] != self.__module__.split('.')[0]:
        #     return None
        #
        # if getattr(view_func, 'actions', None):
        #     action = view_func.actions.get(request.method.lower())
        # else:
        #     action = None
        #
        # policy = PolicySet(action, resource, subject)
        # decision = policy.decision()
        #
        # if settings.DEBUG_ABAC:
        #     print(policy.__str__())
        #
        # if decision:
        #     abac_filter = policy.get_filters()
        #     if abac_filter:
        #         view_func.cls.queryset = view_func.cls.queryset.filter(abac_filter)
        #     return None
        # else:
        #     return HttpResponse(policy.error, status=400)

    def get_auth_user(self, request):
        a = type(request.user)
        user = request.user
        # First, django middleware authentication
        if abac_settings.DEFAULT_AUTHENTICATION and user.is_authenticated:
            return user
        # Second, abac additional authentication
        for auth_class in abac_settings.ADDITIONAL_AUTHENTICATION_CLASS:
            try:
                if auth_class().authenticate(request):
                    user, _ = auth_class().authenticate(request)
                else:
                    continue
            # TODO: всё таки надо создать свои классы индетификации
            # TODO: так как рестовские кидают эксепшены неизвестной породы :(
            except Exception:
                continue
            return user

        return AnonymousUser()
