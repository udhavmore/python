from flask import Flask, render_template, url_for, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        print('<Task %r>' % self.id)
        return '<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == "" or request.form['password'] == "":
            error = 'Please enter Username and Password'
            print(error)
        else:
            if request.form['username'] and request.form['password'] == 'admin':
                uname = request.form['username']
                return redirect(url_for('index'))
    return render_template('login.html', error=error)


@app.route('/toggleAction', methods=['POST'])
def toggleAction():
    if request.method == 'POST':
        app_form_data = request.form['btn_apps']
        print(f'app_form_data: {app_form_data}')
        if 'Add Entry' in app_form_data:
            return redirect(url_for('add'))
        elif 'Calender' in app_form_data:
            return 'Calender'
        elif 'Reports' in app_form_data:
            return 'Reports'
        elif 'Assigned Tasks' in app_form_data:
            return 'Assigned Tasks'


@app.route('/index', methods=['POST', 'GET'])
def index():
    print(request.form)
    return render_template('index.html')


@app.route('/logout', methods=['POST'])
def logout():    
    if request.method == 'POST':
        return redirect(url_for('login'))


@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        task_content = request.form['content']  # Passing ID of the input for addEntry.html
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/add')
        except Exception as e:
            print(e)
            return e

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('addEntry.html', tasks=tasks)


@app.route('/delete/<int:id>')
def delete(id):
    task_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_delete)
        db.session.commit()
        return redirect('/add')
    except Exception as e:
        print(e)
        return e


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/add')
        except Exception as e:
            print(e)
            return e
    else:
        return render_template('update.html', task=task)


if __name__ == '__main__':
    host = '0.0.0.0'
    app.run(host=host, debug=True)
