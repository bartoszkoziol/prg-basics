class ContactList:
    def __init__(self):
        self.contacts=[]

    def add_contact(self, contact):
        self.contacts.append(contact)
    
    def display_contact(self):
        print("Contact list: ")
        for contact in self.contacts:
            print(contact)
