from flask import Flask, jsonify, request

app = Flask(__name__)

##Initial Data in my to do list
##Initial Data in my to do list
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}
]

@app.route('/')
def home():
    return "Welcome To The Sample To DO List App"

## Get: Retrieve all the items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)


## get: Retireve a specific item by Id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id): # Retrieve a specific item by Id, if id is 1 then this is item 1 is displayed from items dictionary
    item = next((item for item in items if item["id"]==item_id), None) #next is used to iterate through the list of items and find the item with the matching id, it returns item of type dictionary
    if item is None:
        return jsonify({"error": "item not found"})
    return jsonify(item) #jsonify is used to convert the dictionary to json format

##Post:create a new task
@app.route('/items',methods = ['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error": "item not found"})
    new_item={
        "id": items[-1]["id"]+1 if items else 1,
        "name":request.json['name'],
        "description": request.json['description']
    }
    items.append(new_item)
    return jsonify(new_item)

#Put this in Console tab of browser to test POST method, request.json gets the data from the body of the request

'''fetch("http://127.0.0.1:5000/items", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ name: "Pen", description: "Blue ink pen" })
})
  .then(res => res.json())
  .then(data => console.log("Response:", data))
  .catch(err => console.error("Error:", err));'''

#Put: Update an existing item
@app.route('/items/<int:item_id>', methods=['PUT']) #update item based on item id in url
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"})
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

#Put this in Console tab of browser to test PUT method. item id is 1 here
'''fetch("http://localhost:5000/items/1", {
  method: "PUT",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    name: "Updated Pen",
    description: "Now black ink"
  })
})
  .then(res => res.json())
  .then(data => console.log("Updated item:", data))
  .catch(err => console.error("Error:", err));'''

#DELETE: Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"result": "Item deleted"})

'''fetch("http://localhost:5000/items/1", {
  method: "DELETE"
})
  .then(res => res.json())
  .then(data => console.log("Response:", data))
  .catch(err => console.error("Error:", err));'''

if __name__ == '__main__':
    app.run(debug=True)