import json


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

    def write_in_log(self):
        self.file.write(f"\n INFO {self.domain, items['official']} \n")


with open("countries.json", encoding="utf-8-sig") as file:
    json_data = file.read()
data = json.loads(json_data)


for countries in data:
    items = countries['name']
    for i in LinkGenerator(items['official']):
        countries = LinkGenerator('countries.txt')
        with LinkGenerator('countries.txt') as countries:
            countries.write_in_log()
            print(countries)
