# https://realpython.com/flask-by-example-part-1-project-setup/

import flask
import requests
import json
app = flask.Flask(__name__)


@app.route('/')
def hello():
    #return "Hello World!"

    # https://stackoverflow.com/questions/25149493/how-to-call-another-webservice-api-from-flask
    req = requests.get('https://api.edamam.com/search?q=&app_id=7e4ea052&app_key=71e8215aeceaa5a02e357584841dc8c9&from=0&to=5&health=peanut-free&health=tree-nut-free&mealType=Dinner&cuisineType=Japanese')
    result = json.loads(req.text)
    hits = result['hits']

    recipes = []
    for hit in hits:
        label = hit['recipe']['label']
        image = hit['recipe']['image']
        url = hit['recipe']['url']
        healthLabels = hit['recipe']['healthLabels']
        cautions = hit['recipe']['cautions']
        recipes.append({'label': label, 'image': image, 'url': url, 'healthLabels': healthLabels, 'cautions': cautions})

    context = {'recipes': recipes}
    return flask.render_template("index.html", **context)

if __name__ == '__main__':
    app.run()