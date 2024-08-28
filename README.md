# myside6

myside6 is a Django-based blog application where users can create posts with a title, content, and a category. This project is designed to be a simple and straightforward blogging platform with essential features.

## Features

- **Create Posts:** Add a title, content, and category for each blog post.
- **Categorize Posts:** Organize posts by different categories for better content management.
- **User Authentication:** Basic authentication to manage who can create or edit posts.
- **Responsive Design:** The application is designed to be accessible on both desktop and mobile devices.

## Installation

To set up the project locally, follow these steps:

### 1. Clone the repository

```bash
git clone https://github.com/harshitpatel12345/blog123.git#


### Prerequisites

Ensure you have the following software installed:

Python 3.x
Django 3.x or above
pip (Python package installer)

### Installation

1. **Clone the repository:**
   sh
    git clone https://github.com/harshitpatel12345/blog123.git
    cd blog123

   
2. **Create and activate a virtual environment:**
   sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
   
3. **Install the dependencies:**
   sh
    pip install -r requirements.txt
   
4. **Set up the environment variables:**
   Create a .env file in the root directory of the project and add the following:
   env
    SECRET_KEY=your_secret_key_here
    DEBUG=True
    DATABASE_URL=your_database_url_here
   
5. **Run the initial migrations and create a superuser:**
   sh
    python manage.py migrate
    python manage.py createsuperuser
   
6. **Run the development server:**
   sh
    python manage.py runserver
   
7. **Access the application:**
   Open your browser and go to `http://127.0.0.1:8000/` to start Post

## Usage

Once set up, you can:

**Browse Post**: View the Post listings and categories.
**Manage Post**: Add. Delete. Update the post.

## Configuration

Configure the application using the .env file. Ensure you set the following variables:

SECRET_KEY: The secret key for Django security.
DEBUG: Set to True for development and False for production.
DATABASE_URL: Connection URL for your database.

## Contributing

We welcome contributions to enhance the project. To contribute:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Implement your changes and test thoroughly.
4. Submit a pull request with a detailed description of your changes.

