class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"
#Creates a template for storing information about one person

class ContactsManager:
    def __init__(self):
        self.contacts = {}
#This class manages all your contacts using a hash table Creates an empty hash table called contacts. Keys = contact names, Values = Contact objects