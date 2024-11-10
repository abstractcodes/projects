from flask import request, jsonify # returns json data
from config import app, db
from models import Contact

# get method to get difffernet context
# decorator
# specify which route we will go to.
# 31.26
@app.route("/contacts", methods=["GET"])
def get_contacts():
    # flask SQL to gett all the context that exists in the database.
    contacts = Contact.query.all()
    # they are python objects
    # return json data
    # create a new list which contains json
    # map takes all the elements from the list and give us a new list.
    # x will be the parameter and then call function
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts}), 200

# create contacts

# test your backend first and then going to the frontend to interact.
@app.route("/create_contact", methods=["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")
    
    if not first_name or not last_name or not email:
        return (
            jsonify({"message": "You must include a first name, last name and email"}),
            400,
        )
    
    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
    # adding o the database
    # errors can occur if there is an exception
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    # getting past
    return jsonify({"message": "User created!"}), 201
    

if __name__ == "__main__":
    # get the context 
    with app.app_context():
        # create all the different models defined the database
        # sping up the database
        db.create_all()
    # running the code
    app.run(debug = True)