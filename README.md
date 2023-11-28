# Django Blog Website

Welcome to the Django Blog Website! This web application is built using the Django web framework and is designed to provide a platform for creating and managing blog posts. Whether you're a seasoned blogger or just getting started, this website makes it easy to publish and share your thoughts with the world.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Contributing](#contributing)
5. [License](#license)

## Features

- **User Authentication**: Securely register, log in, and manage your account.
- **Create and Edit Posts**: Easily create and edit blog posts with a rich text editor.
- **Comment System**: Engage with your audience through a robust comment system.
- **Responsive Design**: Enjoy a seamless experience on various devices with a responsive design.
- **Tagging System**: Categorize your posts with tags for easy navigation.
- **Search Functionality**: Quickly find relevant content with a powerful search feature.
- **User Profiles**: Customize your profile and showcase your published posts.

## Installation

Follow these steps to set up the Django Blog Website locally:

1. **Clone the Repository:**
   ```
   git clone https://github.com/phanstudio/myblog.git
   ```

2. **Navigate to the Project Directory:**
   ```
   cd myblog
   ```

3. **Create a Virtual Environment:**
   ```
   python -m venv venv
   ```

4. **Activate the Virtual Environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On Unix or MacOS:
     ```
     source venv/bin/activate
     ```

5. **Install Dependencies:**
   ```
   pip install -r requirements.txt
   ```

6. **Run Migrations:**
   ```
   python manage.py migrate
   ```

7. **Create Superuser (Admin):**
   ```
   python manage.py createsuperuser
   ```

8. **Start the Development Server:**
   ```
   python manage.py runserver
   ```

Visit [http://localhost:8000](http://localhost:8000) in your browser to access the Django Blog Website.

## Usage

1. **Log in or Register:**
   - Navigate to the `/login` or `/register` endpoint to create or log in to your account.

2. **Create a Post:**
   - Once logged in, visit the `/create-post` endpoint to create a new blog post.

3. **Manage Your Posts:**
   - Use the `/my-posts` endpoint to view and edit your published posts.

4. **Engage with Readers:**
   - Encourage readers to leave comments on your posts using the built-in comment system.

## Contributing

If you would like to contribute to the development of this project, please follow our [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code for your own projects.

Happy Blogging! 🚀
