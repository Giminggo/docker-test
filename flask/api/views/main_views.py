from flask import Blueprint, request, jsonify
from api.models.user import User


bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello():
    return 'Hello, World!'
  
@bp.route('/api/users', methods=['GET'])
def show_all_user():
  if request.method == 'GET':
    data = []
    users = User.query.all()
    for user in users:
      data.append({column.name: getattr(user, column.name) for column in user.__table__.columns})
    
    return jsonify(data)