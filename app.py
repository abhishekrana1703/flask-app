from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    email = data.get('email')
    name = data.get('name')
    date = data.get('date')

    if email == 'abhishek.x.rana@qd.com':
        repo_name = f"Test_abhishek.x.rana_{date}"
        token = 'YOUR_GITHUB_TOKEN'  # Securely store this token
        create_github_repo(token, repo_name)
        return jsonify(message='Repository created successfully.'), 200
    else:
        return jsonify(message='Invalid email address.'), 400

def create_github_repo(token, repo_name):
    url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"token {token}"}
    data = {"name": repo_name}
    response = requests.post(url, json=data, headers=headers)
    if response.status_code != 201:
        print(f"Error creating repository: {response.status_code} - {response.text}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
