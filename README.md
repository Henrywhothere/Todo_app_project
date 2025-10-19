# Name project: Todo App API

A RESTful Todo API build with **Django REST Framework**. 
This project was built to practice backend development, including model design, API building, JWT authentication, API testing, unit testing, and deployment to Railway. 


--- 

## Overview
This project represents my first complete backend workflow — from designing data models to deploying a live API.  
It helped me understand how real-world backend systems are structured and tested.


---

## Features
- **Model Design:** Built custom models with timestamps and user associations 
- **RESTful API:** RESTful CRUD operations for tasks
- **JWT Authentication:** Secure login and token-based access for users.
- **Testing:**
    - API tested using Postman (including JWT flow)
    - Unit tests for model logic with Django’s TestCase
- **Database** SQLite / PostgreSQL (prod)
- **Deployment:** Hosted on **Railway**
- **Version Control:** Managed via Git & GitHub.


---

## Tech Stack
- **Language:** Python
- **Framework:** Django, Django REST Framework
- **Auth:** JSON Web Token (JWT)
- **Database:** SQLite / PostgreSQL
- **Testing:** Django TestCase, Postman
- **Deployment:** Railway
- **Version Control:** Git & GitHub

--- 

## Installation & Setup

1. Clone the repository: 
- Command: git clone https://github.com/Henrywhothere/Todo_app_project.git
- Command: cd todo_app_project
2. Create Virtual Environment
- Command: python -m venv venv
- Command: venv/Scripts/Activate.ps1 (on Windows) / source venv/bin/activate (on macOS/Linux)
3. Install Dependencies
- Command: pip install -r requirement.txt
4. Run Migrations
- Command: python manage.py migrate
5. Start Development Server
- Command: python manage.py runserver 


---

## Testing
### Unit Tests
Run all test with command: python manage.py test
### Postman Tests 
- Imported all endpoints into Postman
- Tested CRUD and JWT authentication

---

## Deployment
Deployed using **Railway** for continuous hosting.
Live Link: https://web-production-e7f8e.up.railway.app


---

## What I learned 
From this project, I learned how to:
- Design database models and relationships.
- Build RESTful APIs using Django REST Framework.
- Implement JWT authentication for secure user access.
- Write and run unit tests for models and views.
- Use Git for version control and deploy via Railway.
- Test and document APIs with Postman.


---

## Future Improvements
- Add user-specific task filtering.
- Add logging & monitoring.
- Add Error Handling 
- Add CI/CD pipeline using GitHub Actions.


--- 
## Author
Nguyễn Luân Thuận - Henry
- Python Backend Developer
- https://github.com/Henrywhothere

