from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime

date = datetime.now().date().strftime("%d/%m/%Y") # today's date

app = Flask(__name__)
Bootstrap5(app)
app.config['SECRET_KEY'] = 'its_a_secret'

task_list = [] # list containing the tasks

# ------------------------ Forms ------------------------

class ToDoForm(FlaskForm):
    task = StringField('Add Task', validators=[DataRequired()], render_kw={"placeholder": "Write a Task..."})
    submit = SubmitField('Add',render_kw={"class": "Write a Task..."})

# ------------------------ Routes ------------------------

# home page
@app.route("/", methods=['GET','POST'])
def home():
    todo = ToDoForm()
    if todo.validate_on_submit():
        task_list.append(todo.task.data)
        return redirect(url_for('home'))
    return render_template('index.html', todo=todo, task_list=task_list, date=date)

# to delete a task
@app.route("/delete/<task>")
def delete_task(task):
    task_list.remove(task)
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)