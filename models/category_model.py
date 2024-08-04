from config import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    quizzes = db.relationship('Quiz', backref='category', lazy=True)