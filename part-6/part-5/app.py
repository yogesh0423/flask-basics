"""
Part 5: Mini Project - Personal Website with Flask
===================================================
A complete personal website using everything learned in Parts 1-4.

How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask, render_template

app = Flask(__name__)

# =============================================================================
# YOUR DATA - Customize this section with your own information!
# =============================================================================

PERSONAL_INFO = {
    'name': 'Yogesh Patil',
    'title': 'Data scientist',
    'bio': 'A passionate data scientist with experience in machine learning and web development.',
    'email': 'yogeshpatil@example.com',
    'github': 'https://github.com/yogesh0423',
    'linkedin': 'https://linkedin.com/in/yogesh-patil04',
}

SKILLS = [
    {'name': 'Python', 'level': 80},
    {'name': 'HTML/CSS', 'level': 75},
    {'name': 'Flask', 'level': 60},
    {'name': 'JavaScript', 'level': 50},
    {'name': 'SQL', 'level': 45},
]

PROJECTS = [
    {'id': 1, 'name': 'Personal Website', 'description': 'A Flask-powered personal portfolio website.', 'tech': ['Python', 'Flask', 'HTML', 'CSS'], 'status': 'Completed'},
    {'id': 2, 'name': 'Todo App', 'description': 'A simple task management application.', 'tech': ['Python', 'Flask', 'SQLite'], 'status': 'In Progress'},
    {'id': 3, 'name': 'Weather Dashboard', 'description': 'Display weather data from an API.', 'tech': ['Python', 'Flask', 'API'], 'status': 'Planned'},
    {'id': 4, 'name': 'Jarvis AI', 'description': 'An AI assistant that can perform various tasks.', 'tech': ['Python', 'AI'], 'status': 'Completed'},
    {'id': 5, 'name': 'E-commerce Site', 'description': 'A basic online store application.', 'tech': ['Python', 'Flask', 'SQL'], 'status': 'In Progress'},
]

BLOG_POSTS = [
    {'id': 1, 'title': 'Welcome to My Blog', 'date': '2024-01-15', 'excerpt': 'An introduction to my personal blog where I share thoughts on technology and development.', 'content': 'This is the full content of the first blog post. Here I can write about various topics...'},
    {'id': 2, 'title': 'Learning Flask', 'date': '2024-01-20', 'excerpt': 'My journey learning Flask and building web applications with Python.', 'content': 'Flask is a lightweight web framework for Python. In this post, I share my experiences...'},
    {'id': 3, 'title': 'Data Science Insights', 'date': '2024-01-25', 'excerpt': 'Exploring data science concepts and sharing practical tips.', 'content': 'Data science combines statistics, programming, and domain expertise. Here are some insights...'},
]


# =============================================================================
# ROUTES
# =============================================================================

@app.route('/')
def home():
    return render_template('index.html', info=PERSONAL_INFO)


@app.route('/about')
def about():
    return render_template('about.html', info=PERSONAL_INFO, skills=SKILLS)


@app.route('/projects')
def projects():
    return render_template('projects.html', info=PERSONAL_INFO, projects=PROJECTS)


@app.route('/project/<int:project_id>')  # Dynamic route for individual project
def project_detail(project_id):
    print(project_id)
    project = None
    for p in PROJECTS:
        if p['id'] == project_id:
            project = p
            break
    print(project)
    return render_template('project_detail.html', info=PERSONAL_INFO, project=project, project_id=project_id)


@app.route('/contact')
def contact():
    return render_template('contact.html', info=PERSONAL_INFO)


@app.route('/blog')
def blog():
    return render_template('blog.html', info=PERSONAL_INFO, blog_posts=BLOG_POSTS)

@app.route('/blog/<int:blog_id>')
def blog_detail(blog_id):
    blogs = {
        1: {
            'title': 'Getting Started with Flask',
            'content': 'Flask is a lightweight Python web framework...',
            'status': 'Published',
            'tags': ['Flask', 'Python', 'Web']
        },
        2: {
            'title': 'Understanding Jinja2',
            'content': 'Jinja2 helps create dynamic HTML templates...',
            'status': 'Draft',
            'tags': ['Jinja2', 'Templates']
        }
    }

    blog = blogs.get(blog_id)
    return render_template(
        'blog_detail.html',
        blog=blog,
        blog_id=blog_id,
        info={'name': 'My Portfolio'}
    )


@app.route('/skill/<skill_name>')
def skill_filter(skill_name):
    # 1. Create an empty list to store projects that match
    filtered_projects = []
    
    # 2. Loop through all projects
    for project in PROJECTS:
        # 3. Check if the skill_name is in the 'tech' list of that project
        # We use .lower() to make the search case-insensitive
        if skill_name.lower() in [t.lower() for t in project['tech']]:
            filtered_projects.append(project)
            
    # 4. Render a template (we can reuse projects.html!)
    return render_template('projects.html', 
                           info=PERSONAL_INFO, 
                           projects=filtered_projects, 
                           skill_name=skill_name)

if __name__ == '__main__':
    app.run(debug=True)


# =============================================================================
# PROJECT STRUCTURE:
# =============================================================================
#
# part-5/
# ├── app.py              <- You are here
# ├── static/
# │   └── style.css       <- CSS styles
# └── templates/
#     ├── base.html       <- Base template (inherited by all pages)
#     ├── index.html      <- Home page
#     ├── about.html      <- About page
#     ├── projects.html   <- Projects list
#     ├── project_detail.html <- Single project view
#     └── contact.html    <- Contact page
#
# =============================================================================

# =============================================================================
# EXERCISES:
# =============================================================================
#
# Exercise 5.1: Personalize your website
#   - Update PERSONAL_INFO with your real information
#   - Add your actual skills and projects
#
# Exercise 5.2: Add a new page
#   - Create a /blog route
#   - Add blog posts data structure
#   - Create blog.html template
#
# Exercise 5.3: Enhance the styling
#   - Modify static/style.css
#   - Add your own color scheme
#   - Make it responsive for mobile
#
# Exercise 5.4: Add more dynamic features
#   - Create a /skill/<skill_name> route
#   - Show projects that use that skill
#
# =============================================================================
