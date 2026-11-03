from config.db import get_db_connection

class RabbitDAO:
    def get_all(self):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT r.id, r.name, b.name as breed, r.age, r.diet 
            FROM rabbits r
            LEFT JOIN breeds b ON r.breed_id = b.id
        """
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        return result

    def create(self, data):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT id FROM breeds WHERE name = %s", (data['breed'],))
        breed = cursor.fetchone()
        if not breed:
            cursor.execute("INSERT INTO breeds (name) VALUES (%s)", (data['breed'],))
            breed_id = cursor.lastrowid
        else:
            breed_id = breed[0]

        query = "INSERT INTO rabbits (name, breed_id, age, diet) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (data['name'], breed_id, data['age'], data['diet']))
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()
        return new_id

    def update(self, rabbit_id, data):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT id FROM breeds WHERE name = %s", (data['breed'],))
        breed = cursor.fetchone()
        if not breed:
            cursor.execute("INSERT INTO breeds (name) VALUES (%s)", (data['breed'],))
            breed_id = cursor.lastrowid
        else:
            breed_id = breed[0]

        query = "UPDATE rabbits SET name=%s, breed_id=%s, age=%s, diet=%s WHERE id=%s"
        cursor.execute(query, (data['name'], breed_id, data['age'], data['diet'], rabbit_id))
        conn.commit()
        affected = cursor.rowcount
        conn.close()
        return affected

    def delete(self, rabbit_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM rabbits WHERE id = %s", (rabbit_id,))
        conn.commit()
        affected = cursor.rowcount
        conn.close()
        return affected

    def get_toys(self, rabbit_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT t.id, t.name 
            FROM toys t
            JOIN rabbit_toys rt ON t.id = rt.toy_id
            WHERE rt.rabbit_id = %s
        """
        cursor.execute(query, (rabbit_id,))
        result = cursor.fetchall()
        conn.close()
        return result

    def get_by_breed(self, breed_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT r.id, r.name, r.age, r.diet FROM rabbits r WHERE r.breed_id = %s", (breed_id,))
        result = cursor.fetchall()
        conn.close()
        return result