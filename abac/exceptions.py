from django.utils.translation import ugettext_lazy as _


class AbacAuthenticationFailed(Exception):

    def __init__(self, detail=_('Incorrect authentication credentials.')):
        super().__init__(self, detail)
        self.errorCode = 401