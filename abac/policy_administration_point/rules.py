from abac.policy_administration_point.const import (
    NOT_APPLICABLE, INDETERMINATE, PERMIT
)


class Rule:
    """ Class describing the basic behavior of the entity "rule" """

    def __init__(self, target, condition, validate_condition, effect=PERMIT,
                 obligation=None, advice=None, description=None, **kwargs):
        self.target = target
        self.condition = condition
        self.effect = effect
        self.obligation = obligation
        self.advice = advice
        self.description = description
        self.error = None
        self.validate_initialization()
        # Specific field for condition
        for (field, value) in kwargs.items():
            setattr(self, field, value)
        validate_condition()

    def decision(self):
        try:
            if self.target:
                if self.condition(self):
                    return self.effect
            return NOT_APPLICABLE
        except Exception as e:
            self.error = e
            return INDETERMINATE

    def validate_initialization(self):
        if not isinstance(self.target, bool):
            raise TypeError('The target is not bool')
        if not callable(self.condition):
            raise TypeError('The condition is not callable')
        if self.obligation is not None and not callable(self.obligation):
            raise TypeError('The obligation is not callable')
        if self.advice is not None and not callable(self.advice):
            raise TypeError('The advice is not callable')
