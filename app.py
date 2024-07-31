from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import Config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    with app.app_context():
        # Import parts of our application
        from controllers.auth_controller import auth_bp
        from controllers.quiz_controller import quiz_bp
        from controllers.question_controller import question_bp
        from controllers.score_controller import score_bp
        from controllers.admin_controller import admin_bp
        from controllers.category_controller import category_bp

        # Register Blueprints
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
