from db import db


class MovieModel(db.Model):
    __tablename__ = "movies"


    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=False, nullable=False)
    description = db.Column(db.String)
    no_of_ratings = db.Column(db.Integer, unique=False, nullable=True)
    avg_rating = db.Column(db.Integer, unique=False, nullable=True)
    ratings = db.relationship("RatingModel", back_populates="movie", lazy="dynamic", cascade="all, delete")