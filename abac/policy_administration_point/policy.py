import collections

from abac.const import NOT_APPLICABLE, INDETERMINATE


class Policy:
    """ Class describing the basic behavior of the entity "rule" """

    def __init__(self, rules, algorithm, target=None, target_param=None,
                 obligation=None, advice=None, description=None):
        self.target = target
        self.target_param = target_param
        self.rules = rules
        self.algorithm = algorithm
        self.obligation = obligation
        self.advice = advice
        self.description = description
        self.error = None
        self.validate_initialization()

    def decision(self):
        try:
            if self.target is None or self.target(**self.target_param) is True:
                return self.algorithm(
                    [rule.decision() for rule in self.rules]
                )
            return NOT_APPLICABLE
        except Exception as e:
            self.error = e
            return INDETERMINATE

    def validate_initialization(self):
        if not isinstance(self.rules, collections.Iterable):
            raise TypeError('The policies is not iterable')
        if not callable(self.algorithm):
            raise TypeError('The algorithm is not callable')
        if self.obligation is not None and not callable(self.obligation):
            raise TypeError('The obligation is not callable')
        if self.advice is not None and not callable(self.advice):
            raise TypeError('The advice is not callable')
