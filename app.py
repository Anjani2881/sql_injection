from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return send_file('templates/demo.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
