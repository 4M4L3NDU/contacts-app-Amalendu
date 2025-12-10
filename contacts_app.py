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

    def add_contact(self, name, phone, email):
        if name in self.contacts:
            print("Contact already exists.")
            return
        self.contacts[name] = Contact(name, phone, email)
        print("Contact added successfully.")
#Checks if the name already exists If not creates a new Contact and stores it in the hash table

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")
#Removes the contact from the hash table If the name doesn’t exist, shows an error

    def search_contact(self, name):
        if name in self.contacts:
            print(self.contacts[name])
        else:
            print("Contact not found.")
#Looks up the contact by name in the hash table Prints their information if found if not prints an error

    def update_contact(self, name, phone=None, email=None):
        if name not in self.contacts:
            print("Contact not found.")
            return

        if phone:
            self.contacts[name].phone = phone
        if email:
            self.contacts[name].email = email

        print("Contact updated.")
#Updates phone/email for an existing contact Only changes values you provide

    def list_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return

        for contact in self.contacts.values():
            print(contact)
#lists out all existing contacts if contacts dont exist prints error