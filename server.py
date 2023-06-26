from flask_app import app
from flask_app.controllers import homecontroller
# don't forget to import your controllers here :)
if __name__ == '__main__':
    app.run(debug=True)
