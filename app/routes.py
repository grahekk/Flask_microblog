from app import app

@app.route('/')
@app.route("/index")
def index(): # view function
    return "Hello World!"