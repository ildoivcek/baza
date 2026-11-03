from dao.rabbit_dao import RabbitDAO

class RabbitService:
    def __init__(self):
        self.dao = RabbitDAO()

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        if not data.get('name') or not data.get('breed'):
            raise ValueError("Ім'я та порода обов'язкові")
        new_id = self.dao.create(data)
        return {"id": new_id, **data}

    def update(self, rabbit_id, data):
        affected = self.dao.update(rabbit_id, data)
        if affected == 0:
            raise ValueError("Кролика не знайдено")
        return {"id": rabbit_id, **data}

    def delete(self, rabbit_id):
        affected = self.dao.delete(rabbit_id)
        if affected == 0:
            raise ValueError("Кролика не знайдено")
        return {"message": "Видалено успішно"}

    def get_toys(self, rabbit_id):
        return self.dao.get_toys(rabbit_id)

    def get_by_breed(self, breed_id):
        return self.dao.get_by_breed(breed_id)