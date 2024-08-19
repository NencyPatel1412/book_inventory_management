# Book Inventory Management

This project is a backend application for managing a book inventory. It features Google Authentication and supports CRUD (Create, Read, Update, Delete) operations for managing books. The project is built using Python and can be run using the `run.py` file.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Google Authentication](#google-authentication)
- [License](#license)

## Features

- **Google Authentication:** Secure authentication using Google OAuth 2.0.
- **CRUD Operations:** Manage the book inventory with Create, Read, Update, and Delete functionalities.
- **Alembic:** Database migrations handled by Alembic.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Python 3.7+
- Pip (Python package manager)
- PostgreSQL (or any other SQL database)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/NencyPatel1412/book_inventory_management.git
   cd book_inventory_management
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:

   Make sure your database is set up and running. Configure the database connection in the environment variables.

4. Apply database migrations:

   ```bash
   alembic upgrade head
   ```

## Environment Variables

Create a `.env` file in the root directory and add the following environment variables:

```ini
DATABASE_URL=your_database_url
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
SECRET_KEY=your_secret_key
```

- `DATABASE_URL`: The connection string for your database.
- `GOOGLE_CLIENT_ID`: The client ID obtained from the Google Developer Console.
- `GOOGLE_CLIENT_SECRET`: The client secret obtained from the Google Developer Console.
- `SECRET_KEY`: A secret key for securing sessions.

## Running the Application

Run the following command to start the application:

```bash
python run.py
```

The application will start on the default port (e.g., http://localhost:8000).

## API Endpoints

- **GET /books**: Retrieve a list of all books.
- **POST /books**: Add a new book.
- **GET /books/{id}**: Retrieve a book by its ID.
- **PUT /books/{id}**: Update a book by its ID.
- **DELETE /books/{id}**: Delete a book by its ID.

## Google Authentication

This project uses Google OAuth 2.0 for user authentication. To set it up:

1. Go to the [Google Developer Console](https://console.developers.google.com/).
2. Create a new project and enable the Google+ API.
3. Set up OAuth 2.0 credentials.
4. Add your client ID and client secret to the `.env` file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
