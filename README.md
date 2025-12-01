This Django project is an Event Management Web Application designed to allow colleges, organizations, or communities to efficiently manage events online. It provides a simple, interactive platform for both administrators and candidates (users attending events), covering user authentication, event creation, and browsing features.

Project Description Overview This is a full-stack event management website built using Python, Django (backend), HTML/CSS/JavaScript (frontend), and MySQL (database). It includes separate interfaces for administrators and candidate users, with secure login and role-based access.

Features Candidate Registration/Login: Candidates can register for accounts and securely log in. Account creation, login, and logout mechanisms are fully implemented.

User Authentication: Custom user model (extending Django’s AbstractUser) is used to distinguish between candidate users and admin users.

Admin Dashboard: Administrators (superusers) log in via a separate panel and can create, update, and delete events using a user-friendly dashboard interface.

Event Management:

Admins can add events by providing details like title, description, date, time, location, and images.

Events are listed for candidate users to browse.

Clicking an event displays detailed information.

Event Listing and Filtering: Event lists are searchable using a dynamic JavaScript-powered search bar, allowing users to find events by title or date in real time.

Responsive Interface: The site design adapts to mobile and desktop devices, ensuring usability for all users.

Secure Access/Role Control:

Only registered candidates can view events and details.

Admin access is restricted to users with superuser rights.

Technology Stack Backend: Django (Python)

Frontend: HTML, CSS (with responsive design), JavaScript

Database: MySQL

Platform: Run in VS Code, with a manageable folder structure for templates, static files, and migrations

Use Cases College event scheduling/viewing for students and staff

Community event portals for citizens and organizers

Internal organizational event management for employees

Basic Workflow Admin creates and manages events via dashboard or Django admin.

Candidates register, log in, browse, and view event details.

User roles and access control ensure only authorized modifications.
