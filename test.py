from contacts_app import ContactsManager, Contact

def test_empty_structure():
    manager = ContactsManager()
    print("Test Empty Structure:")
    manager.list_contacts()   # Expect: "No contacts found."

def test_add_contact():
    manager = ContactsManager()
    print("\nTest Add Contact:")
    manager.add_contact("Alice", "12345", "alice@email.com")
    manager.search_contact("Alice")  # Expect: prints Alice's details

def test_duplicate_contact():
    manager = ContactsManager()
    print("\nTest Duplicate Contact:")
    manager.add_contact("dew", "111", "d@mail.com")
    manager.add_contact("dew", "222", "d@other.com")  # Expect: "Contact already exists."
