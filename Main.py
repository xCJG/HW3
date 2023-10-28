from flask import Flask, render_template
from flask import request
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

# Define the routes
@app.route('/api/update_basket_a')
def update_basket_a():
    try:
        conn = psycopg2.connect(**dvdrental)
        cur = conn.cursor()

        # Insert a new row into basket_a
        cur.execute("INSERT INTO basket_a (a, fruit_a) VALUES (%s, %s)", (5, 'Cherry'))
        conn.commit()
        return "Success!"

    except Exception as e:
        return str(e)

    finally:
        cur.close()
        conn.close()

@app.route('/api/unique')
def unique_fruits():
    try:
        conn = psycopg2.connect(**dvdrental)
        cur = conn.cursor()

        # Query for unique fruits in basket_a and basket_b
        cur.execute("SELECT DISTINCT fruit_a FROM basket_a")
        unique_fruits_a = cur.fetchall()
        cur.execute("SELECT DISTINCT fruit_b FROM basket_b")
        unique_fruits_b = cur.fetchall()

        return render_template('unique.html', unique_fruits_a=unique_fruits_a, unique_fruits_b=unique_fruits_b)

    except Exception as e:
        return str(e)

    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
