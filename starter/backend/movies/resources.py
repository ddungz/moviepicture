from flask import jsonify
from flask.views import MethodView

# Dummy database to hold movie examples
movies = {
    "123": {"title": "Top Gun: Maverick", "description": "Fighter planes"},
    "456": {"title": "Sonic the Hedgehog", "description": "Blue Sega character"},
    "789": {"title": "A Quiet Place", "description": "Scary monsters"},
    "990": {"title": "Network", "description": "Science hacks"},
    "991": {"title": "Social network", "description": "Life hacks"},
    "992": {"title": "Social network 2", "description": "Life hacks 2"},
    "999": {"title": "Transformer", "description": "Fiction ages"},
}


class Movies(MethodView):
    def get(self, movie_id):
        if movie_id is None:
            # Return a list of all movies
            return jsonify({"movies": [dict({"title": movie["title"]}, **{"id": i}) for i, movie in movies.items()]})
        else:
            # Return the details of a specific movie
            return jsonify({"movie": movies[str(movie_id)]})
