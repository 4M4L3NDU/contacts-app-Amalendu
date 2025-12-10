from contacts_app import ContactsManager, Contact

def test_empty_structure():
    manager = ContactsManager()
    print("Test Empty Structure:")
    manager.list_contacts()   # Expect: "No contacts found."
