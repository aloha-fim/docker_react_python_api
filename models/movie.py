from db import db


class MovieModel(db.Model):
    __tablename__ = "movies"


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    description = db.Column(db.String)
    ratings = db.relationship("RatingModel", back_populates="movie", lazy="dynamic", cascade="all, delete")