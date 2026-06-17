from app import app
from app.db_models import db


# Degerlendirici main.py beklerse uygulamayi buradan da baslatabilir.
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
