
class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self,name,phone_number):
        if name in self.contacts:
            print(f"contact '{name}' is arledy exist.")
        else:
            self.contacts[name] = phone_number
            print(f"contact '{name}' added.")
    
    def view_contacts(self):
        if not self.contacts:
            print("sorry no contacts found")
        else:
            for name,phone_number in self.contacts.items():
                print(f"Name: {name}, Phone number: {phone_number}")

    def update_contact(self,name,new_phone_number):
        if name in self.contacts:
            self.contacts[name] = new_phone_number
            print(f"contact '{name}' updated.")
        else:
            print(f"contact '{name}' not found.")

    def delete_contact(self,name):
        if name in self.contacts:
            del self.contacts[name] 
            print(f"contact '{name}' deleted")
        else:
            print(f"contact '{name}' not found.")

contact_book = ContactBook()
contact_book.add_contact("aah",888877034)
contact_book.update_contact("aah",345)
contact_book.delete_contact("aah")
contact_book.add_contact("yooo",888877034)
contact_book.add_contact("fablab",456)
contact_book.delete_contact("fablab")
contact_book.add_contact("yooo",888877034)
contact_book.view_contacts()