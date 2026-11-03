from flask import Blueprint, request, jsonify
from services.rabbit_service import RabbitService

rabbit_bp = Blueprint('rabbits', __name__)
service = RabbitService()

@rabbit_bp.route('/rabbits', methods=['GET'])
def get_all():
    try:
        return jsonify(service.get_all()), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@rabbit_bp.route('/rabbits', methods=['POST'])
def create():
    try:
        new_rabbit = service.create(request.json)
        return jsonify(new_rabbit), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 400

@rabbit_bp.route('/rabbits/<int:rabbit_id>', methods=['PUT'])
def update(rabbit_id):
    try:
        updated = service.update(rabbit_id, request.json)
        return jsonify(updated), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 404

@rabbit_bp.route('/rabbits/<int:rabbit_id>', methods=['DELETE'])
def delete(rabbit_id):
    try:
        result = service.delete(rabbit_id)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 404

@rabbit_bp.route('/rabbits/<int:rabbit_id>/toys', methods=['GET'])
def get_toys(rabbit_id):
    try:
        return jsonify(service.get_toys(rabbit_id)), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@rabbit_bp.route('/breeds/<int:breed_id>/rabbits', methods=['GET'])
def get_by_breed(breed_id):
    try:
        return jsonify(service.get_by_breed(breed_id)), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500