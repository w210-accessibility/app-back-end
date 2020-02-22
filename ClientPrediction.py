import json

class ClientPrediction:
    def __init__(self, lat, long, label):
        self.latitude = lat
        self.longitude = long
        self.label = label

    def __str__(self):
        return "({},{}): {}".format(self.latitude,
                                    self.longitude,
                                    self.label)

    def to_dict(self):
        return self.__dict__
