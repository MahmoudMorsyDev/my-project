class DiaryEntry:
    # Properties:
    #   contact_list : a list of the phone numbers of the contacts
    #   contents: a string reprenting the content of the diary entry
    def __init__(self, contents):
        # Parameters: 
        #   contents: The content of the diary entry
        # Side-Effects:
        #   Sets the property contents of the diary entry
        #   Initializes the list of contacts
        self.contents = contents
        self.contact_list = []

    def add_contact(self, contact):
        # Parameters:
        #   contact: Phone number of the contact that is added
        # Side-Effects:
        #    Add a contact to the list of contacts
        self.contact_list.append(contact)

    def get_contacts(self):
        # Returns:
        #   a list of the contacts
        return self.contact_list