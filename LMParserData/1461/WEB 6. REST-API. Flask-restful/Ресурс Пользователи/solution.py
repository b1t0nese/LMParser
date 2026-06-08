import flask
from flask_restful import Resource
from . import db_session
from .user import User
from datetime import datetime
from users_parser import create_user_parser, create_user_update_parser


class UsersListResource(Resource): 
    def get(self):
        all_users = db_session.query(User).all()
        
        users_list = []
        for user in all_users:
            user_dict = {
                'id': user.id,
                'surname': user.surname,
                'name': user.name,
                'age': user.age,
                'position': user.position,
                'speciality': user.speciality,
                'address': user.address,
                'email': user.email,
                'modified_date': user.modified_date.isoformat() if user.modified_date else None
            }
            users_list.append(user_dict)
        
        return {
            'users': users_list,
            'count': len(users_list)
        }, 200
            
    def post(self):
        parser = create_user_parser()
        args = parser.parse_args()
        
        existing_user = db_session.query(User).filter(
            User.email == args['email']
        ).first()
        
        if existing_user:
            return {
                'error': 'Bad request',
                'message': 'Пользователь c таким email уже существует'
            }, 400
        
        new_user = User(
            surname=args['surname'],
            name=args['name'],
            age=args.get('age'),
            position=args.get('position'),
            speciality=args.get('speciality'),
            address=args.get('address'),
            email=args['email'],
            hashed_password=args['password'],
            modified_date=datetime.now()
        )
        
        db_session.add(new_user)
        db_session.commit()
        
        return {
            'status': 'success',
            'message': 'Пользователь успешно добавлен',
        }, 201


class UsersResource(Resource):
    def get(self, user_id):
        user = db_session.query(User).filter(User.id == user_id).first()
        
        if user is None:
            return {
                'error': 'Not found',
                'message': 'Пользователь не найден'
            }, 404
        
        user_dict = {
            'id': user.id,
            'surname': user.surname,
            'name': user.name,
            'age': user.age,
            'position': user.position,
            'speciality': user.speciality,
            'address': user.address,
            'email': user.email,
            'modified_date': user.modified_date.isoformat() if user.modified_date else None
        }
        
        return {
            'status': 'success',
            'user': user_dict
        }, 200
    
    def put(self, user_id):
        user = db_session.query(User).filter(User.id == user_id).first()
        
        if user is None:
            return {
                'error': 'Not found',
                'message': f'Пользователь с ID {user_id} не найден'
            }, 404
        
        parser = create_user_update_parser()
        args = parser.parse_args()
        
        if args.get('surname'):
            user.surname = args['surname']
        
        if args.get('name'):
            user.name = args['name']
        
        if args.get('age') is not None:
            user.age = args['age']
        
        if args.get('position') is not None:
            user.position = args['position']
        
        if args.get('speciality') is not None:
            user.speciality = args['speciality']
        
        if args.get('address') is not None:
            user.address = args['address']
        
        if args.get('email'):
            existing_user = db_session.query(User).filter(
                User.email == args['email'],
                User.id != user_id
            ).first()
            
            if existing_user:
                return {
                    'error': 'Bad request',
                    'message': f'Пользователь с email {args["email"]} уже существует'
                }, 400
            
            user.email = args['email']
        
        if args.get('password'):
            user.hashed_password = args['password']
        
        user.modified_date = datetime.now()
        
        db_session.commit()
        
        return {
            'status': 'success',
            'message': 'Пользователь успешно обновлен',
        }, 200
    
    def delete(self, user_id):
        user = db_session.query(User).filter(User.id == user_id).first()
        
        if user is None:
            return {
                'error': 'Not found',
                'message': 'Пользователь не найден'
            }, 404
        
        deleted_user_info = {
            'id': user.id,
            'name': f"{user.surname} {user.name}",
            'email': user.email
        }
        
        db_session.delete(user)
        db_session.commit()
        
        return {
            'status': 'success',
            'message': 'Пользователь успешно удален',
            'deleted_user': deleted_user_info
        }, 200