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


posts = {
        '1' : {
        'body' : ' Hmwk 8 CRUD operations',
        'user_id' : '1'
    },
    '2' : {
        'body' : "First resource: Get operation, Post operation, Put operation, Delete operation.",
        'user_id' : '2'
    },
    '3' : {
        'body': 'Second resource: Get operation, Post operation, Put operation, Delete operation.',
        'user_id' : '1'

    }     
}   












@app.route('/')
def home():
    return 'Flask homework #2!'


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
        return {'message' : "Invalid user"},400 
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


#5create
# @app.route('/post', methods=['POST'])
# def create_post():
#     post_data=request.get_json()
#     post_id = post_data['user_id']
#     if post_id in users:
#      posts[str(uuid4())] = post_data
#      return { 'message': "Post Created" }, 201
#     return {'message': "Invalid User"}, 401



@app.route('/post', methods=['POST'])
def create_post():
    post_data=request.get_json()
    user_id = post_data['user_id']
    if user_id in users:
     posts[str(uuid4())] = post_data
     return { 'message': "Post Created" }, 201
    return {'message': "Invalid User"}, 401








#6Read 
@app.route('/post')
def get_posts():
    return {'posts':list(posts.values()) }


#7update
@app.put('/post')
def update_post():
    return {'message': 'post updated successfully'}, 200


#8delete 
@app.delete('/post')
def delete_post():
    return {'message': 'post deleted successfully'}, 200



if __name__ == '__main__':
    app.run(debug=True)


