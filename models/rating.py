from db import db


class RatingModel(db.Model):
    __tablename__ = "ratings"


    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    stars = db.Column(db.Integer)
    movie = db.relationship("MovieModel", back_populates="ratings", lazy="dynamic")