# HW3
Assignment 3

This project shows 
- When a user accesses your Flask server with 127.0.0.1:5000/api/update_basket_a, you should insert a new row (5, 'Cherry') into basket_a. On the browser, it should either show "Success!" Or error message from PostgreSQL.
- When a user accesses your Flask server with 127.0.0.1:5000/api/unique, you should show unique fruits in basket_a and unique fruits in basket_b in an HTML table. If there are any errors from PostgreSQL, show the error message on the browser.

Quick Start 
1. Set Up Your Development Environment
  Make sure you have Python, Flask, and PostgreSQL installed on your system.

2. Create a Flask Application
  Create a new Python file HW3.py and add the following code:
    from flask import Flask, render_template
    import psycopg2

    app = Flask(__name)

    # Database connection configuration
    dvdrental = {
      database: dvdrental,
      user: christian,
      password: test,
      host: 127.0.0.1,
      port: 5432
    }
3. Create an HTML Template
  Create an HTML template file named unique.html in a folder called templates in your project directory. Use the provided HTML code from the previous response for this file.

4. Run Your Flask App
Run your Flask app by executing HW3.py in your terminal.

5. Access the Application
Option 1: open your web browser and go to: http://127.0.0.1:5000/api/update_basket_a
Option 2: open your web browser and go to: http://127.0.0.1:5000/api/unique

When you visit the update route, it will either show "Success!" if the insertion is successful, or it will display an error message from PostgreSQL if there is an issue.
When you visit the unique route, it will display a web page with unique fruits in both tables.
