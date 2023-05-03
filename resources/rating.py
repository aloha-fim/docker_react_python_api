from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required, get_jwt
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import RatingModel
from schemas import RatingSchema

blp = Blueprint("Ratings", "ratings", description="Operations on ratings")

# get or delete rating by rating id (not useful)
@blp.route("/api/rating/<int:rating_id>")
class Rating(MethodView):
    @jwt_required()
    @blp.response(200, RatingSchema)
    def get(self, rating_id):
        rating = RatingModel.query.get_or_404(rating_id)
        return rating
    
    @jwt_required()
    def delete(self, rating_id):
        jwt = get_jwt()
        if not jwt.get("is_admin"):
            abort(401, message="Admin privilege required.")

        rating = RatingModel.query.get_or_404(rating_id)
        db.session.delete(rating)
        db.session.commit()
        return {"message": "Rating deleted."}

# add a rating
@blp.route("/api/rating")
class RatingList(MethodView):
    @blp.response(200, RatingSchema(many=True))
    def get(self):
        return RatingModel.query.all()

    @jwt_required(fresh=True)
    @blp.arguments(RatingSchema)
    @blp.response(201, RatingSchema)
    def post(self, rating_data):
        #turn into keyword arguments
        rating = RatingModel(**rating_data)

        try:
            db.session.add(rating)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured while inserting the rating.")

        return rating