from flask import Flask, render_template, request, redirect, url_for, render_template_string
import subprocess
import os

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'AI_FITNESS_PROJECT'), static_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'AI_FITNESS_PROJECT', 'assets'))
@app.route('/blog1')
def blog1():
    return render_template('blog1.html')
@app.route('/blog2')
def blog2():
    return render_template('blog2.html')
@app.route('/blog3')
def blog3():
    return render_template('blog3.html')
@app.route('/blog4')
def blog4():
    return render_template('blog4.html')
@app.route('/bmiindex')
def bmiindex():
    return render_template('bmiindex.html')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fit')
def fit():
    return render_template('Fit_plan_bot/fit.html')

@app.route('/workout')
def workout():
    return render_template('AI-Fitness-trainer-main/exercise.html')

@app.route('/start-exercise', methods=['POST'])
def start_exercise():
    exercise = request.form['exercise']
    script_path = os.path.join(os.path.dirname(__file__),'AI_FITNESS_PROJECT', 'AI-Fitness-trainer-main', 'main.py')
    command = f'python "{script_path}" -t {exercise}'

    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        return redirect('/workout')  # Redirects back to workout page
    except Exception as e:
        return f"<h2>Error starting '{exercise}': {e}</h2><a href='/workout'>Back</a>"
    
@app.route('/workout1')
def workout1():
    return render_template('AI-Fitness-trainer-main/workout.html')

@app.route('/start-exercise1', methods=['POST'])
def start_exercise1():
    exercise = request.form['exercise']
    script_path = os.path.join(os.path.dirname(__file__),'AI_FITNESS_PROJECT', 'AI-Fitness-trainer-main', 'main1.py')
    command = f'python "{script_path}" -t {exercise}'

    try:
        subprocess.Popen(command, shell=True)
        return redirect('/workout1')
    except Exception as e:
        return f"<h2>Error starting '{exercise}': {e}</h2><a href='/workout1'>Back</a>"

if __name__ == '__main__':
    app.run(debug=True)
