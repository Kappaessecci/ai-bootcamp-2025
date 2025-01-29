# Implementa qui il codice

class Contact:
  def __init__(self, name, surname, phone=None):
    self.name = name
    self.phone = phone
    self.surname = surname

class Person(Contact):
  pass

class Business(Contact):
  pass

class Directory:
  def __init__(self):
    self.contacts = []

  def __len__(self):
    return len(self.contacts)

  def add(self, contact):
    self.contacts.append(contact)

  def query(self, name):
    return [contact for contact in self.contacts if contact.name == name]

  def find(self, search_term):
    return [contact for contact in self.contacts if search_term in contact.name or (contact.phone and search_term in contact.phone)]