# 🚀 **Class Management System**

A fully functional **web application** built with **Django** and **Django REST Framework (DRF)** that allows for the **management of students**, **professors**, **courses**, and **assignments** with **role-based access control**.

---

## ✨ **Features**

* **🔐 User Authentication** with **JWT (JSON Web Tokens)**
* **👩‍🏫 Role-based access control** for **Staff**, **Professors**, and **Students**
* **🛠 CRUD functionality** for:

  * **Students**: Create, read, update, and delete student information.
  * **Professors**: Create, read, update, and delete professor information.
  * **Courses**: Create, read, update, and delete course details.
  * **Assignments**: Create, read, update, and delete assignments with course associations.
* **⚙️ PostgreSQL** as the database backend.
* **📡 API Endpoints** for handling data and authentication, providing easy integration with frontend applications.
* **💻 Postman** used for testing **APIs**, but you can add a **frontend** (React/HTML/CSS) to interact with the backend.
---

## 🖥️ **Tech Stack**

* **Backend**: Django, Django REST Framework (DRF)
* **Database**: PostgreSQL
* **Authentication**: JWT (JSON Web Token)
---

## 📦 **Installation**

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/class-management-system.git
cd class-management-system
```

### 2. Set up a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment:

* **Windows**:

  ```bash
  venv\Scripts\activate
  ```
* **macOS/Linux**:

  ```bash
  source venv/bin/activate
  ```

### 3. Install the dependencies

Run the following command to install all necessary dependencies:

```bash
pip install django djangorestframework psycopg2-binary djangorestframework-simplejwt
```

### 4. Set up the database

* Create a **PostgreSQL database** named `classms_db`.
* Update the database configuration in **`settings.py`** to match your database credentials.

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create a superuser (optional for admin access)

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

Your application will be running at `http://127.0.0.1:8000/`.

---

## 📡 **API Endpoints**

### **Authentication**

* **POST** `/auth/register/` - Register a new user (student, professor, staff).
* **POST** `/auth/login/` - Login and get JWT access and refresh tokens.
* **POST** `/auth/token/refresh/` - Refresh the access token using the refresh token.

### **Users**

* **GET** `/users/` - List all users (staff only).
* **POST** `/users/` - Create a new user (admin only).
* **GET** `/users/<id>/` - Retrieve a user by ID (staff only).
* **PUT** `/users/update/<id>/` - Update a user’s information (staff only).
* **DELETE** `/users/delete/<id>/` - Delete a user (staff only).

### **Students**

* **GET** `/students/` - List all students.
* **POST** `/students/` - Create a new student.
* **GET** `/students/<id>/` - Retrieve a student by ID.
* **PUT** `/students/update/<id>/` - Update a student’s information.
* **DELETE** `/students/delete/<id>/` - Delete a student.

### **Professors**

* **GET** `/professors/` - List all professors.
* **POST** `/professors/` - Create a new professor.
* **GET** `/professors/<id>/` - Retrieve a professor by ID.
* **PUT** `/professors/update/<id>/` - Update a professor’s information.
* **DELETE** `/professors/delete/<id>/` - Delete a professor.

### **Courses**

* **GET** `/courses/` - List all courses.
* **POST** `/courses/` - Create a new course.
* **GET** `/courses/<id>/` - Retrieve a course by ID.
* **PUT** `/courses/update/<id>/` - Update a course.
* **DELETE** `/courses/delete/<id>/` - Delete a course.

### **Assignments**

* **GET** `/assignments/` - List all assignments.
* **POST** `/assignments/` - Create a new assignment.
* **GET** `/assignments/<id>/` - Retrieve an assignment by ID.
* **PUT** `/assignments/update/<id>/` - Update an assignment.
* **DELETE** `/assignments/delete/<id>/` - Delete an assignment.

---

## 🛠️ **Roles & Permissions**

* **Staff**: Full access to create, update, and delete users, professors, courses, and assignments.
* **Professor**: Can create, update, and delete assignments, and be assigned to courses.
* **Student**: Can only view assigned courses and assignments.

---

## 💡 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

