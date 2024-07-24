# Advanced Todo

A robust to-do application that empowers users to organize tasks, manage projects, and collaborate effectively.

# Tech Stack
Django, PostgreSQL

# Postman Collection

[<img src="https://run.pstmn.io/button.svg" alt="Run In Postman" style="width: 128px; height: 32px;">](https://app.getpostman.com/run-collection/37129695-7accd137-94a4-47fd-8aa5-7ab66233ce42?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D37129695-7accd137-94a4-47fd-8aa5-7ab66233ce42%26entityType%3Dcollection%26workspaceId%3D33f9716f-32bf-4d19-bd6f-7c4b32110d3a)

# Low Level Design
![drawSQL-image-export-2024-07-23 (1)](https://github.com/user-attachments/assets/3e45864b-a8ba-4225-97f4-ce873bdcc295)

# Features

### User Management

| User Management           |   |
|---------------------------|---|
| Signup User               | ✅ |
| Login User                | ✅ |
| Two-factor authentication | ❌ |

### Project Management

| Project Management          |   |
|-----------------------------|---|
| Project creation            | ✅ |
| Task creation               | ✅ |
| Sub-task management         | ✅ |
| Task and subtask Visibility | ✅ |

### Smart Dependencies

| Smart Dependencies     |   |
|------------------------|---|
| Conditional tasks      | ❌ |
| Logical conditions     | ❌ |
| Dependency restriction | ✅ |

### Collaboration

| Collaboration   |   |
|-----------------|---|
| Task Assignment | ✅ |
| Task listing    | ✅ |

### Data Access and Visibility

| Data Access and Visibility |   |
|----------------------------|---|
| Public project view        | ❌ |
| Logged in view             | ❌ |

### Task Completion

| Task Completion                                                                             |   |
|---------------------------------------------------------------------------------------------|---|
| Mark as completed (By creator or by assignee)                                               | ✅ |
| Completion rules | ✅ |

### Intelligent Scheduling

| Intelligent Scheduling                                     |   |
|------------------------------------------------------------|---|
| One task at a time                                         | ❌ |
| Task need to done sequentially                             | ❌ |
| Can be done parallelly if multiple collaborators           | ❌ |
| One project at a time, complete all tasks of current first | ❌ |

# How to build project?
Create virtual environment

```shell (Need to do during setup only)
python -m venv venv
```

Active virtual environment

```shell
source venv/bin/activate
```

Install packages

```shell (Need to do during setup only)
pip install -r app/requirements.txt
```

Setup database (Need to do during setup only)

```shell
python app/manage.py migrate
```

Run dev backend server

```shell
python app/manage.py runserver
```

The django app will run on http://localhost:8000



