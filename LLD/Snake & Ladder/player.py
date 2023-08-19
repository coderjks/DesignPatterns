
class Player:

    def __init__(self, _id):
        self._id = _id
        self.cur_pos = 0

    @property
    def id(self):
        return self._id
