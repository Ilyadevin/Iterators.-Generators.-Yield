import json
import hashlib


def md5_hash():
    with open('countries.txt', encoding='utf-8-sig') as cont:
        strings = cont.read().splitlines()
        for string in strings:
            string_utf8 = string.encode("utf-8")
            hash_md5 = hashlib.md5(string_utf8)
            hexa_md5 = hash_md5.hexdigest()

            yield hexa_md5


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


with open("countries.json", encoding="utf-8-sig") as file:
    json_data = file.read()
data = json.loads(json_data)


for countries in data:
    items = countries['name']
    for i in items.values():
        with LinkGenerator(i, 'countries.txt') as generator:
            generator.write_in_log()
            for hashed_string in md5_hash():
                print(hashed_string)
