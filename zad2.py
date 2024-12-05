#Napisac prosta klase przechowujaca np. dane osobowe (imie, nazwisko, adres zamieszkania, kod pocztowy, pesel)
#i metode zapisujaca obiekty typu tej klasy do json, oraz metode odczytuja json'a i ladujace dane do klasy

import json

class PersonalData:
    def __init__(self, name, surname, postalcode, address, pesel):
        self.name = name
        self.surname = surname
        self.address = address
        self.postalcode = postalcode
        self.pesel = pesel

    def __str__(self):
        return f"name: {self.name}\nsurname: {self.surname}\naddress: {self.address}\npostalcode: {self.postalcode}\npesel: {self.pesel}"

    def save_to_json(self, filename):
        data = {
            "name": self.name,
            "surname": self.surname,
            "address": self.address,
            "postalcode": self.postalcode,
            "pesel": self.pesel
        }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @classmethod
    def load_from_json(cls, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return cls(data["name"], data["surname"], data["postalcode"], data["address"], data["pesel"])

person1 = PersonalData("Jan", "Kowalski", "00-000", "ul. Piękna 10, Warszawa", "12345678901")
person1.save_to_json("person1.json")

person2 = PersonalData.load_from_json("person1.json")
print(person2)

