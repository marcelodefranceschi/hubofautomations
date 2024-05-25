from main import app, database
from models import User, Post

#with app.app_context():
#    database.create_all()


with app.app_context():
    user = User(username="Marcelo", email="defranceschi.marcelo@gmail.com", password="123456")
    user2 = User(username="Carlos", email="marcelo.defranceschi@macegroup.com", password="123456")
    database.session.add(user, user2)
    database.session.commit()

# with app.app_context():
#     my_users = User.query.all()
#     print(my_users)



# with app.app_context():
#     user_test = User.query.filter_by(
#         email='marcelo.defranceschi@macegroup.com').first()
#     print(user_test)
