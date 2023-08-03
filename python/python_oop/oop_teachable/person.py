class Person:
    def __init__(self):
        self._last_name = None
        self._first_name = None

    def print(self):
        print(f'Full name: {self._first_name} {self._last_name}')

    @property
    def first_name(self):
        print('in get method')
        return self._first_name

    @first_name.setter
    def first_name(self, new_first_name):
        print('in set method')
        self._first_name = new_first_name
