
# Guesthouse Website Project README

This repository contains the source code for a guesthouse website developed using Django with SQLite as the database backend. The primary purpose of this project is to provide a platform for guests to explore information about the guesthouse, leave messages, and inquire about available services.


# Features
Homepage: Display essential information about the guesthouse, such as location, amenities, and contact details.
Messages: Allow visitors to leave messages or inquiries regarding their stay or services.
Admin Panel: Utilize Django's built-in admin panel for easy management of messages.
Prerequisites

- Before you begin, ensure you have the following installed:
	- Python 3.7
	- Django
	```css
	pip install django
	```
	- Clone the repository:
 	```css
	git clone https://github.com/ChungLinWu0829/Website.git
  	cd Website/template
  	```
	- Create and activate a virtual environment:
   ```css
	python -m venv venv
	source venv/bin/activate
   # On Windows, use `venv\Scripts\activate`
  ```
	- Install dependencies:
	```css
	pip install -r requirements.txt
	```
	- Apply migrations:
	```css
	python manage.py migrate
	```
	- Create a superuser account for accessing the admin panel:
	```css
	python manage.py createsuperuser
	```
	- Run the development server:
	```css
	python manage.py runserver
	```
	The website should now be accessible at http://localhost:8000/.

Visit the homepage to explore information about the guesthouse.
Navigate to the "Messages" section to leave inquiries or messages.
Access the admin panel at http://localhost:8000/admin/ to manage messages.
