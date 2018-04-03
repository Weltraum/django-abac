from django.db.models import Q


class AbstractPolicy:
    """ Abstract class describing the basic behavior of the entity "policy" """

    def __init__(self, action=None, resource=None, subject=None):
        self.action = action
        self.resource = resource
        self.subject = subject
        self.error = 'ABAC. Permission denied'

    def target(self):
        """ An optional attribute for policy """
        return True

    def rules(self):
        """ A set of rules for calculating security policy """
        raise NotImplementedError('Subclasses must implement this method.')

    def algorithm(self):
        """ Default algorithm: allow, if everything is allowed """
        return all

    def filter(self):
        """ Applied to queryset filters """
        return None

    def get_filters(self):
        """ Returns to queryset filters """
        return self.filter()

    def decision(self):
        """ Calculating the security policy  """
        return self.target() and \
               self.algorithm()((rule.target() for rule in self.rules()))

    def description(self):
        pass