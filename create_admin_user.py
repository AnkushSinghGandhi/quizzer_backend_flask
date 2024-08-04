import os
from werkzeug.security import generate_password_hash
from app import create_app, db
from models.user_model import User

# Create the Flask app and initialize it
app = create_app()

# Use app context to interact with the database
with app.app_context():
    admin_username = os.getenv('ADMIN_USERNAME', 'admin')
    admin_email = os.getenv('ADMIN_EMAIL', 'admin@example.com')
    admin_password = os.getenv('ADMIN_PASSWORD', 'admin')

    # Check if the admin user already exists
    if User.query.filter_by(username=admin_username).first():
        print("Admin user already exists.")
    else:
        # Hash the password using a valid method
        hashed_password = generate_password_hash(admin_password, method='pbkdf2:sha256')
        
        # Create the admin user
        new_admin = User(username=admin_username, email=admin_email, password=hashed_password, role='admin')
        db.session.add(new_admin)
        db.session.commit()
        
        print(f"Admin user '{admin_username}' created successfully.")
