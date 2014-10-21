from app import app

# Route recorators
@app.route('/')
@app.route('/index')

def index():
    return "Hello, World!"
