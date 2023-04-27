from flask import Flask,request
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)


class lcm(Resource):
    def get(self,x,y):
    	x=int(x)
    	y=int(y)
    	if x > y:  
    		greater = x 
    	else:  
    		greater = y
    	while(True):
    		if((greater % x == 0) and (greater % y == 0)):
    			lcm = greater
    			break
    		greater += 1
    	return lcm

api.add_resource(lcm,'/lcm/<x>/<y>')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5056)
