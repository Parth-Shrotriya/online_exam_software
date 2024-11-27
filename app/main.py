from flask import Flask
from routes.admin import admin_bp
from routes.student import student_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(student_bp, url_prefix='/student')

@app.route('/')
def home():
    return "Welcome to Online Exam Software!"

if __name__ == '__main__':
    app.run(debug=True)
