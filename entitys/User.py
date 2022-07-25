

class User:

    def __init__(self, json):
        self.name, self.username, self.email = json['name'], json['username'], json['email']
        self.address, self.phone, self.website = json['address'], json['phone'], json['website']
        self.company = json['company']

    def __eq__(self, other):
        return (self.name == other.name and self.username == other.username and
                self.email == other.email and self.address == other.address and
                self.phone == other.phone and self.website == other.website and
                self.company == other.company)
