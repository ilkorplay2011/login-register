from flask import Flask, render_template, request
import json
app = Flask(__name__)
for_json = {}
def save_users(users_dict):
    with open('pass_and_us.json', 'w') as f:
        json.dump(users_dict, f, indent=4)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        with open('pass_and_us.json', 'r') as file:
            pass_and_user = json.load(file)
        password = request.form['password']
        username = request.form['username']
        if password in pass_and_user.values() and username in pass_and_user.keys() and pass_and_user[username] == password:
            return 'You logged in'
        else:
            return 'Wrong password'
    return render_template('index.html')
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        password_reg = request.form['passw']
        username_reg = request.form['user']
        for_json[username_reg] = password_reg
        save_users(for_json)
    return render_template('reg.html')
app.run(debug=True)
