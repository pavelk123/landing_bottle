from bottle import run, route, template, static_file, post, request
import sqlite3

@post('/contact')
def get_contact():
    name = request.forms.name
    email = request.forms.email
    subject = request.forms.subject
    message = request.forms.message

    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('INSERT INTO data (name, email, subject, message) VALUES (?,?,?,?)', (name,email,subject,message))
    conn.commit()
    c.close()
    return '<script>alert("Thank You");</script>'

@post('/')
def get_email():
    email = request.forms.email

    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('INSERT INTO subs (email) VALUES (?)', (email,))
    conn.commit()
    c.close()
    return '<script>alert("Thank You");</script>'+ template('index')
@route('/')
def index():
    return template('index')

@route('/<filepath:path>/<file>')
def static_server(filepath,file):
    return static_file(file,root=filepath)

@route('/<file>')
def template_server(file):
    file= file.replace('html','tpl')
    return template(file)

@route('/check')
def check_db():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT id, name, email, subject, message FROM data')
    result = c.fetchall()
    return template('make_table', rows=result)

@route('/check_subs')
def check_subs():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT id, email FROM subs')
    result = c.fetchall()
    return template('make_table', rows=result)

if __name__ == '__main__':
    run(debug=True,reloader=True)