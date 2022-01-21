class ShiftableList(list):
    def __lshift__(self, other):
        l = len(self)
        limit = other % l
        return ShiftableList(self[limit:] + self[:limit])

    def __rshift__(self, other):
        l = len(self)
        limit = (l - other) % l
        return ShiftableList(self[limit:] + self[:limit])