"""
Provides various authentication policies.
"""
from django.utils.translation import ugettext_lazy as _

try:
    from rest_framework.authentication import (
        BasicAuthentication,
        SessionAuthentication,
        TokenAuthentication,
        RemoteUserAuthentication,
    )
    from rest_framework.exceptions import AuthenticationFailed
    REST = True
except ImportError:
    REST = False

try:
    from rest_framework_jwt.authentication import (
        JSONWebTokenAuthentication,
    )
    from rest_framework.exceptions import AuthenticationFailed
    REST_JWT = True
except ImportError:
    REST_JWT = False

from abac.exceptions import AbacAuthenticationFailed


class BaseAuthenticationMixing:

    def authenticate(self, request):
        if not self.is_module_import:
            raise ModuleNotFoundError(self.error_module_import)
        try:
            user, _ = super().authenticate(request)
            return user
        except AuthenticationFailed as e:
            raise AbacAuthenticationFailed(e.detail)

    @property
    def is_module_import(self):
        """ Returns the result of importing the specific module """
        raise NotImplementedError('Subclasses must implement this method.')

    @property
    def error_module_import(self):
        """ Returns the error text of importing the specific module """
        raise NotImplementedError('Subclasses must implement this method.')


class RestFrameworkAuthenticationMixing(BaseAuthenticationMixing):

    @property
    def is_module_import(self):
        return REST

    @property
    def error_module_import(self):
        return _("No module named 'rest_framework'")


class RestFrameworkJwtAuthenticationMixing(BaseAuthenticationMixing):

    @property
    def is_module_import(self):
        return REST_JWT

    @property
    def error_module_import(self):
        return _("No module named 'rest_framework_jwt'")


class RestFrameworkBasicAuthentication(BasicAuthentication,
                                       RestFrameworkAuthenticationMixing):
    pass


class RestFrameworkSessionAuthentication(SessionAuthentication,
                                         RestFrameworkAuthenticationMixing):
    pass


class RestFrameworkTokenAuthentication(TokenAuthentication,
                                       RestFrameworkAuthenticationMixing):
    pass


class RestFrameworkRemoteUserAuthentication(RemoteUserAuthentication,
                                            RestFrameworkAuthenticationMixing):
    pass


class RestFrameworkJSONWebTokenAuthentication(JSONWebTokenAuthentication,
                                              RestFrameworkAuthenticationMixing):
    pass