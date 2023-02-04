from flask import Flask
import json
from dbhelpers import run_statement

app = Flask(__name__)

@app.get('/animals')
def get_animals():
    result = run_statement("CALL list_animals()")
    if (type(result) == list):
        result_json = json.dumps(result, default=str)
        animals = json.loads(result_json)
        return animals
    else:
        return 'Close, but no cigar'
    
@app.post('/animals')
def post_animal():
    new_animal = 'raccoon'
    result = run_statement("CALL post_animal()")
    if (type(result) == list):
        result_json = json.dumps(result, default=str)
        new_animal = json.loads(result_json)
        return "You've added: ", new_animal, "to the list!"
    else:
        return 'Your animal was not added to the list'

app.run(debug = True)