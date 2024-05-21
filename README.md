# Video of the Web App as I have used db.slqite3 cannot freely host in Vercel


https://github.com/Kanch-prog/Blog-App-ML/assets/121807277/8fa1cf2e-507b-4041-b2ba-48a93ecc6390


BlogIt - A Django-based Blogging Platform

A dynamic and interactive blogging platform developed using the Django framework which allows users to create, manage, and view blog posts while providing personalized recommendations based on the content of the posts. The platform features user authentication, a user-friendly interface, and a recommendation system to enhance user engagement.

Key Features:
 1. User Authentication
 2. Blog Management - 
    View All Posts: Users can browse all published blog posts on the platform.
    View Single Post: Users can view individual blog posts along with recommendations for similar posts.
    User Dashboard: Each user has a personal dashboard to view and manage their own posts.
    Add Post: Users can create new blog posts using a straightforward form.
    Edit Post: Users can edit their existing posts to update content.
    Delete Post: Users can delete posts they no longer wish to keep.
  3. Content-Based Recommendations- When viewing a post, users receive recommendations for other similar posts using TF-IDF vectorization and cosine similarity.
  4. Database Population

Technology used:
 ` Django Framework: Utilized for its powerful web development capabilities, including built-in user authentication, ORM for database management, and form handling.
 ` TF-IDF and Cosine Similarity: Implemented using scikit-learn to create a content-based recommendation system that enhances user engagement by suggesting relevant posts.
 ` Models and Forms:
 ` Post Model: Defines the structure of a blog post with fields such as title, author, content, and published date.
 ` PostForm: A form for creating and editing posts, based on the Post model.
 ` URL Routing:The platform’s URL routing is managed through Django's URL dispatcher, mapping URL paths to their respective view functions.
 ` Templates:Templates are used to render HTML pages for various functionalities, including registration, login, viewing posts, user dashboard, adding posts, and editing posts.
