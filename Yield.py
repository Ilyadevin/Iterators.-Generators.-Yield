import string
import json

CHARS = string.ascii_lowercase.__iter__()


class link_generator:

    def __init__(self, domain, max_len=10):
        self.max_len = max_len
        self.domain = f'https://en.wikipedia.org/wiki/{domain}/'
        self.last_country = []
        self.chars = CHARS.__iter__()

    def __iter__(self):
        return self

    def __next__(self):
        if not self.last_country:
            self.last_country = (self.chars.__next__())
        elif len(self.last_country) > self.max_len:
            raise StopIteration
        elif self.last_country[-1] == 'z':
            self.chars = CHARS.__iter__()
            self.last_country.append(self.chars.__next__())
        else:
            self.last_country.append(self.chars.__next__())
        yield f'{self.domain}{"".join(self.domain)}{"/".join(self.last_country)}'


with open("countries.json", encoding="utf-8-sig") as file:
    json_data = file.read()
data = json.loads(json_data)
for countries in data:
    items = countries['name']

    for i in link_generator(items['official']):
        print(i)
        break
