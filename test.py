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

def test_delete_contact():
    manager = ContactsManager()
    print("\nTest Delete Contact:")
    manager.add_contact("Cha", "33333", "cha@mail.com")
    manager.delete_contact("Cha")
    manager.search_contact("Cha")  # Expect: "Contact not found."

def test_delete_nonexistent():
    manager = ContactsManager()
    print("\nTest Delete Non-Existent Contact:")
    manager.delete_contact("NonExistent")  # Expect: "Contact not found."

def test_update_contact():
    manager = ContactsManager()
    print("\nTest Update Contact:")
    manager.add_contact("Dai", "44444", "dai@mail.com")
    manager.update_contact("Dai", phone="99999")
    manager.search_contact("Dai")  # Expect: updated phone

def test_sort_contacts():
    manager = ContactsManager()
    print("\nTest Sort Contacts:")

    manager.add_contact("Chad", "33333", "chad@mail.com")
    manager.add_contact("Al", "12345", "al@mail.com")
    manager.add_contact("Bob", "22222", "bob@mail.com")

    manager.sort_contacts()  # Expect alphabetical order: Alice, Bob, Charlie

def test_large_dataset():
    manager = ContactsManager()
    print("\nTest Large Dataset:")

    for i in range(1000):
        manager.add_contact(f"Person{i}", f"{i}", f"person{i}@mail.com")

    # Search random element
    manager.search_contact("Person500")  # Expect: found

    # Sort tests merge sort performance
    manager.sort_contacts()  # Expect: prints sorted contacts
