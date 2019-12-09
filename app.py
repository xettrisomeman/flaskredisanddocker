from flask import Flask , request , jsonify
import redis

app = Flask(__name__)
redisClient = redis.Redis(host="redis") #redis means take dokcer redis and run


@app.route('/' , methods=['POST' , 'GET'])
def index():

    if request.method == 'POST':
        name = request.json['name']
        redisClient.rpush('students',{'name':name})
        return jsonify({'name' : name})

    if request.method == 'GET':
        return jsonify(redisClient.lrange('students' , 0,-1))

 
    