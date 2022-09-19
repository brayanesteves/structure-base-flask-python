from app import app
from personas import personas

app.register_blueprint(personas)

# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)