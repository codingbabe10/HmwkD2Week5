from flask import Flask, request
from uuid import uuid4

from platformdirs import user_data_dir, user_data_path
from psutil import users


app = Flask (__name__)


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





# posts


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




