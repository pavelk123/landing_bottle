from bottle import run, route, template, static_file
import sqlite3

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
    return template('''
    
<p>The open items are as follows:</p>
<table border="1">
%for row in rows:
  <tr>
  %for col in row:
    <td>{{col}}</td>
  %end
  </tr>
%end
</table>
    
    
    ''', rows=result)

if __name__ == '__main__':
    run(debug=True,reloader=True)