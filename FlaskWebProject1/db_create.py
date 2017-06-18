from FlaskWebProject1 import db, models

db.create_all()
admin = models.User('林川杰','lcjive@gmail.com','v595v595','admin')
db.session.add(admin)
db.session.commit()

