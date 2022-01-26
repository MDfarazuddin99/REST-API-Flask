from flask import Flask, jsonify, request

app = Flask(__name__)

# below is some sort of a data base
stores = [
    {
        'name': 'Ramesh',
        'items':[
            {
                'name':'lux sabun',
                'price':25
            },
            {
                'name':'Thumsup',
                'price':12
            }
        ]
    },
    {
        'name': 'RamnaReddy',
        'items':[
            {
                'name':'lifebouy sabun',
                'price':10
            },
            {
                'name':'sprite',
                'price':11
            }
        ]
    }
]

# POST /store data: {name: }
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name':request_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify({'store':new_store}) #returns a string

# GET /store/<string:name>
@app.route('/store/<string:name>')
# default method is always GET
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'store':store})
    return jsonify({'message':f'Store with name {name} not found'})


# GET /stores
@app.route('/stores')
def get_stores():
    return jsonify({'stores':stores})

# GET /store/<string:name>/items
@app.route('/store/<string:store_name>/items')
def get_items(store_name):
    is_store_found = False
    for store in stores:
        if store['name'] == store_name:
            is_store_found = True
            return jsonify({'items':store['items']})
    if is_store_found == False:
        return jsonify({'message':f'store with name {store_name} not found'})

# POST /store/<string:name>/item data: {name: ,price:}
@app.route('/store/<string:store_name>/item/<string:item_name>')
def get_item(store_name,item_name):
    is_store_found = False
    for store in stores:
        if store['name'] == store_name:
            is_store_found = True
            is_found = False
            for item in store['items']:
                print(item['name'])
                if item_name == item['name']:
                    is_found = True
                    return jsonify(item)
            if is_found == False:
                return jsonify({'message': f'The item {item_name} is not found in {store_name}'})
    if is_store_found == False:
        return jsonify({'message': f'store with name {store_name} not found'})

# POST /store/<string:name>/item
@app.route('/store/<string:store_name>/item',methods=['POST'])
def add_item(store_name):
    request_data = request.get_json()
    new_item = dict()
    new_item['name'] = request_data['name']
    new_item['price'] = request_data['price']
    is_store_found = False
    for store in stores:
        if store_name == store['name']:
            is_store_found = True
            store['items'].append(new_item)
            return jsonify(new_item)
    if not is_store_found:
        return jsonify({'Message':f'The store {store_name} does not exist'})

app.run(debug=True)



