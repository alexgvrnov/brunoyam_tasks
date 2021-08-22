import json


class Model:

    def __init__(self):

        self.cake = 99
        self.souce = 33
        self.coffee = 44

    def _save(self):

        d = {key: getattr(self, key) for key in list(filter(lambda attr: not attr.startswith('_'), dir(self)))}

        with open('attributes.json', 'w') as file:
            json.dump(d, file)

        return d


class ModelChild(Model):

    def __init__(self):

        super().__init__()

        self.stake = 55
        self.pizza = 77


m = ModelChild()

print(m._save())
