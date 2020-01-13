import json
import hashlib


class LinkGenerator:

    def __init__(self, domain, path):
        self.domain = f'https://en.wikipedia.org/wiki/{domain}'
        self.path = path

    def __enter__(self):
        self.file = open(self.path, "a", encoding="utf8")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.file.write(f'\n {self.domain, items["official"]} Ошибка {exc_type} {exc_val}\n')
        self.file.close()
        yield

    def write_in_log(self):
        self.file.write(f"\n INFO {self.domain, items['official']} \n")

    def md5_hash(self):
        with open('countries.txt', encoding='utf-8-sig') as cont:
            strings = cont.read().splitlines()
            for i in strings:
                i_utf8 = i.encode("utf-8")
                hash = hashlib.md5(i_utf8)
                hexa = hash.hexdigest()

                print(hexa)


with open("countries.json", encoding="utf-8-sig") as file:
    json_data = file.read()
data = json.loads(json_data)


for countries in data:
    items = countries['name']
    for i in items.values():
        with LinkGenerator(i, 'countries.txt') as generator:
            generator.write_in_log()


generator.md5_hash()
