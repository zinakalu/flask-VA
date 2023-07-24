from flask import request
from database import db
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from listen_and_respond import listen_and_respond


app = Flask(__name__)

CORS(app, origins=['*'])
db.init_app(app)

migrate = Migrate(app, db)

bcrypt = Bcrypt(app)




from models import User, UserInteractionWithVirtualAssistant, ApiResponse


@app.post('/interact')
def create_interaction():
    user_input = request.get_json('user_input')
    user_id = request.get_json('user_id')
    user = User.query.filter(user.id == id).first()


    if user is None:
        return {'message': 'User not found'}, 404

    
    new_interaction = UserInteractionWithVirtualAssistant(
        user_input_speech=user_input,
        user_id=user.id
    )
    db.session.add(new_interaction)

















if __name__ == '__main__':
    app.run(port=5555, debug=True)