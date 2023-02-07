from flask import Flask, request
import json
from dbhelpers import run_statement, execute_statement, connect_db

app = Flask(__name__)

@app.get('/api/animals')
def get_animals():
    result = run_statement("CALL list_animals()")
    if (type(result) == list):
        result_json = json.dumps(result, default=str)
        animals = json.loads(result_json)
        return animals
    else:
        return "Something went wrong, please try again."

@app.post('/api/animals_new')
def post_animal():
    new_animal = 'wolf'
    result = run_statement("CALL post_animal(?)", [new_animal])
    if (new_animal == None):
        return "You must specify a new animal"
    if result == None:
        return "You've successfully added a new animal: {}".format(new_animal)

@app.patch('/api/animals_update')
def update_animal():
    animal_change = 'coyote'
    if (animal_change == None):
        return "Please enter a valid name"
    result = run_statement("CALL update_animal(?)", [animal_change])
    if result == None:
        return "You've successfully updated the animal to: {}".format(animal_change)
    else:
        return "Something went wrong, please try again."

@app.delete('/api/animals_delete')
def delete_animal():
    animal_delete = 'cat'
    if (animal_delete == None):
        return "Please enter a valid name"
    result = run_statement("CALL delete_animal(?)", [animal_delete])
    if result == None:
        return "You've successfully removed {} from the list".format(animal_delete)
    else: "Something went wrong, please try again"

app.run(debug = True)
