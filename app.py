from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import Config, db

# Initialize extensions
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    with app.app_context():

        # Import models to register them with SQLAlchemy
        from models.score_model import Score
        from models.user_model import User
        from models.quiz_model import Quiz
        from models.question_model import Question
        from models.category_model import Category

        db.create_all()

        # Import and register blueprints
        from controllers.auth_controller import auth_bp
        from controllers.quiz_controller import quiz_bp
        from controllers.question_controller import question_bp
        from controllers.score_controller import score_bp
        from controllers.admin_controller import admin_bp
        from controllers.category_controller import category_bp

        app.register_blueprint(auth_bp, url_prefix='/auth')
        app.register_blueprint(quiz_bp)
        app.register_blueprint(question_bp)
        app.register_blueprint(score_bp)
        app.register_blueprint(admin_bp, url_prefix='/admin')
        app.register_blueprint(category_bp, url_prefix='/admin')

        return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
