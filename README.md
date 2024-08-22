<a href="https://warriorwhocodes.com"><img src="repo_images/header.jpg"></a>

<p align="center">
  <a href="https://ankushsinghgandhi.github.io">
    <img src="https://img.shields.io/badge/Website-3b5998?style=flat-square&logo=google-chrome&logoColor=white" />
  </a>
  <a href="http://twitter.com/ankushsgandhi">
    <img src="https://img.shields.io/badge/-Twitter-blue?style=flat-square&logo=twitter&logoColor=white" />
  </a>
   <a href="https://www.linkedin.com/in/ankush-singh-gandhi-2487771aa/">
    <img src="https://img.shields.io/badge/-LinkedIn-0e76a8?style=flat-square&logo=Linkedin&logoColor=white" />
  </a>
  <a href="https://dev.to/@ankushsinghgandhi">
    <img src="https://img.shields.io/badge/-Dev.to-grey?style=flat-square&logo=dev.to&logoColor=white"/>
  </a>
  <a href="https://stackoverflow.com/users/13790266/ankush-singh">
    <img src="https://img.shields.io/badge/-Stackoverflow-orange?style=flat-square&logo=stackoverflow&logoColor=white"/>
  </a>
  <a href="https://leetcode.com/ankushsinghgandhi/">
    <img src="https://img.shields.io/badge/-Leetcode-yellow?style=flat-square&logo=Leetcode&logoColor=white"/>
  </a>
    <a href="https://www.hackerrank.com/ankushsgandhi">
    <img src="https://img.shields.io/badge/-HackerRank-green?style=flat-square&logo=Hackerrank&logoColor=white"/>
  </a>
    <a href="https://www.hackerearth.com/@bhanusinghank">
    <img src="https://img.shields.io/badge/-Hackerearth-purple?style=flat-square&logo=Hackerearth&logoColor=white"/>
  </a>
</p>

# Quizzer Flask App

Quizzer is a Flask-based web application that allows users to take quizzes and manage their quiz data. Admins have special privileges to create, edit, and delete quizzes, as well as manage users and view scores.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User Authentication**: Users can register and log in with JWT-based authentication.
- **Admin Panel**: Admins can manage quizzes, categories, and users.
- **Quiz Management**: Create, update, delete, and take quizzes.
- **Category Management**: Admins can create, update, and delete quiz categories.
- **Score Tracking**: Users' scores are tracked and can be viewed by users and admins.

## Installation

### Prerequisites

- Python 3.8+
- Virtualenv (optional but recommended)
- SQLite (default database)

### Clone the Repository

```bash
git clone https://github.com/AnkushSinghGandhi/quizzer_backend_flask.git
cd quizzer_backend_flask
```

### Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set Up the Database

```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

### Create an Admin User

To create an admin user, modify the `/auth/register` endpoint to set the `role` to `admin`, or manually add an admin user to the database.

### Run the Application

```bash
flask run
```

The app will be available at `http://127.0.0.1:5000`.

## Usage

### Register a User

Send a POST request to `/auth/register` with the following JSON payload:

```json
{
  "username": "your_username",
  "email": "your_email@example.com",
  "password": "your_password"
}
```

### Log In

Send a POST request to `/auth/login` with the following JSON payload:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

The response will include a JWT access token.

### Access Admin Features

Use the JWT token obtained from the login step to access protected admin routes.

## API Endpoints

### Authentication

- **POST /auth/register**: Register a new user.
- **POST /auth/login**: Log in a user and receive a JWT token.

### Admin Routes (Protected)

- **GET /admin/users**: Retrieve a list of all users.
- **GET /admin/users/:user_id/scores**: Retrieve scores of a specific user.
- **DELETE /admin/users/:user_id**: Delete a specific user.
- **PUT /admin/users/:user_id**: Update details of a specific user.

### Category Management

- **POST /categories**: Create a new category (admin only).
- **GET /categories**: Retrieve a list of all categories.
- **PUT /categories/:category_id**: Update an existing category (admin only).
- **DELETE /categories/:category_id**: Delete a specific category (admin only).

### Quiz Management

- **POST /quizzes**: Create a new quiz (admin only).
- **PUT /quizzes/:quiz_id**: Update details of a specific quiz (admin only).
- **DELETE /quizzes/:quiz_id**: Delete a specific quiz (admin only).
- **GET /quizzes**: Retrieve a list of all quizzes.
- **GET /quizzes/category/:category_id**: Retrieve quizzes by category.

### Question and Answer Management

- **POST /quizzes/:quiz_id/questions**: Add a new question to a specific quiz.
- **POST /questions/:question_id/answers**: Add a new answer to a specific question.

### Score Management

- **POST /quizzes/:quiz_id/scores**: Submit a score for a specific quiz.
- **GET /scores**: Retrieve scores for the currently authenticated user.

## Technologies Used

- **Flask**: Web framework for building the backend.
- **Flask-JWT-Extended**: JWT-based authentication.
- **SQLAlchemy**: ORM for database management.
- **Werkzeug**: Password hashing and security utilities.
- **SQLite**: Default database (can be replaced with PostgreSQL or MySQL).

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
