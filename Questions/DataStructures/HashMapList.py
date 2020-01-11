class HashMapList:
    def __init__(self):
        self.map = {}

    def put_item(self, key, item):
        if not key in self.map:
            self.map[key] = []
        self.map[key].append(item)

    def put_list(self, key, list):
        self.map[key] = list

    def get(self, key):
        if key in self.map.keys():
            return self.map[key]
        else:
            return None

    def contains_key(self, key):
        return key in self.map

    def contains_key_value(self, key, value):
        l = self.get(key)
        if l is None:
            return False
        return value in l

    def key_set(self):
        return self.map.keys()

    def __repr__(self):
        return str(self.map)


