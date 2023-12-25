from flask import Flask, request
from uuid import uuid4


app = Flask (__name__)


users = {
    '1': {
        'username': 'LorenPaul',
        'email':'LorenPaul@aol.com'
    },
    '2': {
        'username': 'LaylaM',
        'email': 'LaylaM@aol.com'
    }
}






#users


#1Create
@app.route('/user', methods=["POST"])
def create_user():
    json_body = request.get_json()
    users[uuid4()] = json_body
    return {'message' : f'{json_body["username"]} created'}, 201




#2Read
@app.route('/user', methods=['GET'])
def user():
    return{'users': list(users.values())}, 200


#3Update
@app.put('/user/<user_id>')
def update_user(user_id):
    try:
     user = users [user_id]
     user_data = request.get_json()
     user |= user_data
     return { 'message' : f'{user["username"]} updated'}, 202
    except KeyError:
     return {'message' : "Invalid user"}, 400
    # username = user_data['username']
    # for id, user in users.items():
    #     if user['username'] == username:
         
        #  return { 'message': 'user updated successfully'}, 200


#4Delete
@app.delete('/user/<user_id>')
def delete_user(user_id):
    try:
        del users[user_id]
        return {'message': f'User deleted'}, 202
    except:
      return {'message': "Invalid username"}, 400
    # user_id_to_delete = request.args.get('user_id')
# posts

    