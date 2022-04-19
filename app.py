from flask import Flask, render_template, render_template_string, request, redirect, url_for


from flask_mysqldb import MySQL



# create instance of Flask class
app = Flask(__name__)
mysql = MySQL(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = '<username>' # UPDATE THIS TO POINT TO YOUR OWN DATABASE
app.config['MYSQL_PASSWORD'] = '<password>' # UPDATE THIS TO POINT TO YOUR OWN DATABASE
app.config['MYSQL_DB'] = '<database name>' # UPDATE THIS TO POINT TO YOUR OWN DATABASE

def execute_query(query, args=None):
    cur = mysql.connection.cursor()
    cur.execute(query, args)
    if query.upper().startswith('SELECT'):
        data = cur.fetchall()
    else:
        mysql.connection.commit()
        data = None
    cur.close()
    return data


@app.route('/')
def index():
    response = list(execute_query("SELECT * FROM users"))
    print(response)
    return render_template('index.html', response=response)

# run the app
if __name__ == '__main__':
    app.run(debug=True, port=3456, host='0.0.0.0')
