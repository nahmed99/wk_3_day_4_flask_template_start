from app import app

@app.route('/') # listen to the home/root
def index():
    return '''
    <html>
        <head>
            <title>Home Page My Todos</title>
        </head>
        <body>
            <h1>My Todo List</h1>
        </body>

    </html>
    '''