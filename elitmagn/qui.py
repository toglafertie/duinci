class User:
    def __init__(self, is_logged_in):
        self.is_logged_in = is_logged_in

    def __and__(self, other):
        return self.is_logged_in and other.is_logged_in
