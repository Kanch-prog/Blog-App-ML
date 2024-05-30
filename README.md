# BlogIt - A Django-based Blogging Platform

BlogIt is a dynamic and interactive blogging platform developed using the Django framework. It allows users to create, manage, and view blog posts while providing personalized recommendations based on the content of the posts.

## Key Features

### User Authentication

- **Sign Up:** New users can register for an account.
- **Login:** Registered users can log in securely.
- **Logout:** Users can safely log out of their accounts.

### Blog Management

- **View All Posts:** Browse all published blog posts on the platform.
- **View Single Post:** Read individual blog posts along with recommendations for similar posts.
- **User Dashboard:** Each user has a personal dashboard to view and manage their own posts.
- **Add Post:** Create new blog posts using a straightforward form.
- **Edit Post:** Update the content of existing posts.
- **Delete Post:** Remove posts that are no longer needed.

### Content-Based Recommendations

- **Recommendation System:** When viewing a post, users receive recommendations for other similar posts using TF-IDF vectorization and cosine similarity.

### Database Population

- **SQLite3 Database:** Utilized for data storage and management.

## Technology Stack

- **Django Framework:** Utilized for its powerful web development capabilities, including built-in user authentication, ORM for database management, and form handling.
- **scikit-learn:** Used for implementing TF-IDF vectorization and cosine similarity for content-based recommendations.
- **Models and Forms:** Post Model defines the structure of a blog post, while PostForm is used for creating and editing posts.
- **URL Routing:** Django's URL dispatcher maps URL paths to their respective view functions.
- **Templates:** HTML pages are rendered for various functionalities using Django templates, including registration, login, viewing posts, user dashboard, adding posts, and editing posts.

## Setup Instructions

Clone the repository:

git clone https://github.com/your_username/BlogIt.git
cd BlogIt
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

Visit http://localhost:8000 in your web browser to access the application.

Demo Video
Unfortunately, due to hosting constraints, we are unable to provide a live demo of the application. However, you can watch a video demonstration here.

https://github.com/Kanch-prog/Blog-App-ML/assets/121807277/8fa1cf2e-507b-4041-b2ba-48a93ecc6390

Feel free to customize this template according to your project's specific requirements and design.

