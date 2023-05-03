from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import MovieModel, RatingModel
from schemas import MovieSchema, RatingSchema

blp = Blueprint("Movies", "movies", description="Operations on movies")


@blp.route("/api/movie/<int:movie_id>")
class Movie(MethodView):
    @blp.response(200, MovieSchema)
    def get(self, movie_id):
        movie = MovieModel.query.get_or_404(movie_id)
        return movie

    def delete(self, movie_id):
        movie = MovieModel.query.get_or_404(movie_id)
        db.session.delete(movie)
        db.session.commit()
        return {"message": "Movie deleted."}, 200

@blp.route("/api/movie")
class MovieList(MethodView):
    @blp.response(200, MovieSchema(many=True))
    def get(self):
        return MovieModel.query.all()
    
    @blp.arguments(MovieSchema)
    @blp.response(201, MovieSchema)
    def post(self, movie_data):
        movie = MovieModel(**movie_data)

        try:
            db.session.add(movie)
            db.session.commit()
        except IntegrityError:
            abort(400, message=f"Movie already exists.")
        except SQLAlchemyError:
            abort(500, message="An error occured creating the movie.")

        return movie
    
@blp.route("/api/movie/<int:movie_id>/rating")
class RatingsInMovie(MethodView):
    @blp.response(200, RatingSchema(many=True))
    def get(self, movie_id):
        movie = MovieModel.query.get_or_404(movie_id)

        return movie.ratings.all()

    @blp.arguments(RatingSchema)
    @blp.response(201, RatingSchema)
    def post(self, rating_data, movie_id):
        #if TagModel.query.filter(TagModel.store_id == store_id, TagModel.name == tag_data["name"]).first():
        #    abort(400, message="A tag with that name already exists in that store.")
        rating = RatingModel(**rating_data, movie_id=movie_id)

        try:
            db.session.add(rating)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=str(e))

        return rating
    