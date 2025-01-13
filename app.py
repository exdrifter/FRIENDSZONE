from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from flask import Flask, flash

app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'blogdb'

mysql = MySQL(app)

@app.route('/')
@app.route('/test')
def test_connection():
    #test_connection
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT 1")
        cursor.close()
        return 'Connection to MySQL database is successful!'
    except Exception as e:
        return f'Error connecting to MySQL database: {str(e)}'

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/blogs', methods=['GET'])
def blogs():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM tblblog")
        regs = cursor.fetchall()
        cursor.close()
        return render_template('index.html', info=regs)
    except Exception as e:
        return str(e)
    

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        details = request.form
        title = details['title']
        date = details['date']
        content = details['content']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tblblog(btitle, bdate, bcontent) VALUES (%s, %s, %s)", (title, date, content))
        mysql.connection.commit()
        cur.close()
        flash('New blog posted!')
        return redirect(url_for('blogs'))
    return render_template('add.html')
    

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM tblblog WHERE id = %s", (id,))
        regs = cursor.fetchone()
        if request.method == 'POST':
            title = request.form['title']
            date = request.form['date']
            content = request.form['content']
            cursor.execute("UPDATE tblblog SET btitle = %s, bdate = %s, bcontent = %s WHERE id = %s", (title, date, content, id))
            mysql.connection.commit()
            cursor.close()
            flash('Selected User Updated successfully')
            return redirect(url_for('blogs'))
        return render_template('edit.html', info=regs)
    except Exception as e:
        return str(e)
    
@app.route('/delete/<int:id>')
def delete(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM tblblog WHERE id = %s", (id,))
        mysql.connection.commit()
        cursor.close()
        flash('Selected blog deleted successfully')
        return redirect(url_for('blogs'))
    except Exception as e:
        return str(e)
    

if __name__ == '__main__':
    app.run()