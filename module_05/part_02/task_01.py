import json


class Model:

    cake = 0
    souce = 2

    def _save(self):

        d = {}

        for attr in dir(self):

            if not attr.startswith('_'):

                d[attr] = getattr(self, attr)

        with open('attributes.json', 'w') as file:
            json.dump(d, file)

        return d


class ModelChild(Model):

    stake = 1
    pizza = 4


m = ModelChild()

print(m._save())
