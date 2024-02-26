
# Django Project Setup Guide

This guide will walk you through setting up and running the Django project on your local development machine.

## Prerequisites

- Python 3.8 or newer
- pip (Python package manager)

## Setup Instructions

### 2. Create a Virtual Environment

Create a virtual environment to manage the project's dependencies separately from your system-wide Python installation. This step ensures that your project's dependencies don't interfere with other Python projects.

```bash
# For Unix/macOS
python3 -m venv env

# For Windows
python -m venv env
```


### 2.1. Install `virtualenv`

If you prefer to use `virtualenv` for managing your project's virtual environment, first install it globally (if not already installed).

```bash
pip install virtualenv
```

### 2.2. Create a Virtual Environment using `virtualenv`

Create a virtual environment to manage the project's dependencies separately from your system-wide Python installation. This ensures that your project's dependencies don't interfere with other Python projects.

```bash
# Create the virtual environment named 'env'
virtualenv env
```

### 3. Activate the Virtual Environment

Before installing dependencies, you need to activate the virtual environment.

```bash
# For Unix/macOS
source env/bin/activate

# For Windows
env\Scripts\activate
```


### 4. Install Project Dependencies

Install the required packages for the project using pip.

```bash
pip install -r requirements.txt
```

### 5. Database Migrations

Before running the application, you need to apply migrations to set up the database schema.

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional)

To access the Django admin panel, create a superuser account.

```bash
python manage.py createsuperuser
```

Follow the prompts to set up the username, email, and password for the superuser.

### 7. Run the Development Server

Start the Django development server to run the project locally.

```bash
python manage.py runserver
```

The project should now be running at [http://localhost:8000](http://localhost:8000).

## Additional Commands

- **Deactivating the virtual environment:** To exit the virtual environment, use the command `deactivate`.
- **Running tests:** To run tests, execute `python manage.py test`.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any improvements or bug fixes.

## License

Specify your project's license here.
