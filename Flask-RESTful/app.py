from flask import Flask, request
from flask_restful import Resource, Api

# Flask-RESTful makes development of api even faster

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
	def get(self,name):
		for item in items:
			if item['name'] == name:
				return item,200
		return {'item':None}, 404

	def post(self,name):
		item = dict()
		request_data = request.get_json()
		price = request_data['price']
		item['name'] = name
		item['price'] = price
		items.append(item)
		return item, 201

class ItemList(Resource):
	def get(self):
		return {'items': items}

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
app.run(port=5000,debug=True)