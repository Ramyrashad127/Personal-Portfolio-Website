# Personal Portfolio Website

This is a Django-powered web application where users can create and manage their personal portfolio. Each user has a unique account and can display their skills, education, and projects. Users can edit their own portfolios, including changing their profile information, password, and username. They can also view other users' portfolios via search, but without the ability to modify them.

## Features

- **User Registration & Authentication**: Users can create an account, log in, log out, and reset passwords.
- **Profile Management**:
  - Add and update personal information (name, email, address, birth date, phone number).
  - Upload and change profile pictures.
  - Edit account settings (username, email, password).
- **Portfolio Management**:
  - Add, edit, and delete **Education** and **Experience** entries.
  - Add, edit, and delete **Projects**:
    - Each project contains a title, description, technology stack, and a GitHub link.
  - View all your added projects in a neat list format.
- **Search**:
  - Search for other users by email to view their portfolios.
  - Only viewing privileges are provided for other users’ profiles (no editing or deletion).
- **Responsive Design**: The website uses Bootstrap for a responsive and clean UI design.
- **Data Privacy**: Users can only edit their own data; no one else can modify it.

## Tech Stack

- **Django**: Backend framework used for building the website's logic.
- **Bootstrap**: Used for responsive design and styling.
- **HTML5 & CSS3**: For structuring the content and additional styling.
- **SQLite**: Django’s default database for development (you can switch to PostgreSQL, MySQL, etc.).

## Installation

### Requirements

- Python 3.x
- Django 4.x
- Bootstrap (linked via CDN)
- Any additional Django dependencies (as listed in `requirements.txt`)

### Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-portfolio-website.git
    ```

2. Navigate into the project directory:
    ```bash
    cd your-portfolio-website
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser for admin access:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

7. Open your browser and visit:
    ```
    http://127.0.0.1:8000/
    ```

## How to Use

1. **Register** for a new account.
2. Once logged in, navigate to your profile to add and edit your personal information, education, experience, and projects.
3. Search for other users by their email to view their portfolios.

## Screenshots

_Include some screenshots of your website showing the key features like portfolio view, project management, and user search._

## Future Improvements

- Adding social media links to the portfolio.
- Implementing a more advanced search feature.
- Enabling portfolio sharing with non-registered users.
- Integrating more customization options for the portfolio layout.

## License

_This project is open-source and licensed under the MIT License._
