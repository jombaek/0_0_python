class Student:

    def __init__(self):
        self._name = None

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and all(x.isalpha() or x.isspace() for x in value):
            self._name = value
        else:
            raise ValueError