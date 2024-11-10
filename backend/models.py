# all the daabase models
# second database model
from config import db

# db model as a class
class Contact(db.Model):
    # key used to index this
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique = False, nullable = False)
    last_name = db.Column(db.String(80), unique = False, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)

    # create a python dictionary
    # json is how we communicate. Passing json back and forth.
    # json should be in camecase for style convention.
    def to_json(self):
        return{
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
        }