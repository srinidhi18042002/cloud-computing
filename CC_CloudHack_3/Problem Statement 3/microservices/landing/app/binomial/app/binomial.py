from flask import Flask,request
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)


class binomial(Resource):
    def get(self,x,y):
    	x=int(x)
    	y=int(y)
    	if 0 <= y <= x:
    		a= 1
    		b=1
    		for t in range(1, min(y, x - y) + 1):
    			a *= x
    			b *= t
    			x -= 1
    		return a//b
    	else:
    		return "Not Possible, K is greater then 0"

api.add_resource(binomial,'/binomial/<x>/<y>')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5057)
