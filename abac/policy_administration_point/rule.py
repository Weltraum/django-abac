from abac.const import (
    NOT_APPLICABLE, INDETERMINATE, PERMIT, DENY
)


class Rule:
    """ Class describing the basic behavior of the entity "rule" """

    def __init__(self, condition, target=None, effect=PERMIT,
                 obligation=None, advice=None, description=None,
                 target_param=None, condition_param=None):
        self.condition = condition
        self.condition_param = condition_param
        self.target = target
        self.target_param = target_param
        self.effect = effect
        self.obligation = obligation
        self.advice = advice
        self.description = description
        self.error = None
        self.validate_initialization()

    def decision(self):
        try:
            if self.target is None or self.target(**self.target_param) is True:
                if self.condition(**self.condition_param) is True:
                    return self.effect
            return NOT_APPLICABLE
        except Exception as e:
            self.error = e
            return INDETERMINATE

    def validate_initialization(self):
        if self.effect not in [PERMIT, DENY]:
            raise TypeError('The effect is not PERMIT or DENY')
        if self.obligation is not None and not callable(self.obligation):
            raise TypeError('The obligation is not callable')
        if self.advice is not None and not callable(self.advice):
            raise TypeError('The advice is not callable')
