from flask import Flask
from flask_cors import CORS
from controllers.rabbit_controller import rabbit_bp

app = Flask(__name__)
#дозволяємо фронтенду стукати на бекенд
CORS(app)

#реєструємо всі маршрути з контролера
app.register_blueprint(rabbit_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5000)