import flask
from flask_restful import Resource
from . import db_session
from .jobs import Jobs
from datetime import datetime
from jobs_parser import create_job_parser, create_job_update_parser


class JobsListResource(Resource):
    def get(self):
        all_jobs = db_session.query(Jobs).all()
        
        jobs_list = []
        for job in all_jobs:
            job_dict = {
                'id': job.id,
                'team_leader': job.team_leader,
                'job': job.job,
                'work_size': job.work_size,
                'collaborators': job.collaborators,
                'start_date': job.start_date.isoformat() if job.start_date else None,
                'end_date': job.end_date.isoformat() if job.end_date else None,
                'is_finished': job.is_finished
            }
            
            if hasattr(job, 'team_leader_rel') and job.team_leader_rel:
                if hasattr(job.team_leader_rel, 'name'):
                    job_dict['team_leader_name'] = f"{job.team_leader_rel.surname} {job.team_leader_rel.name}"
            
            jobs_list.append(job_dict)
        
        return {
            'jobs': jobs_list,
            'count': len(jobs_list)
        }, 200
    
    def post(self):        
        parser = create_job_parser()
        args = parser.parse_args()
        
        start_date = None
        if args.get('start_date'):
            try:
                start_date = datetime.fromisoformat(args['start_date'])
            except ValueError:
                return {
                    'error': 'Bad request',
                    'message': 'Неверный формат start_date. Используйте формат YYYY-MM-DDTHH:MM:SS'
                }, 400
        else:
            start_date = datetime.now()
        
        end_date = None
        if args.get('end_date'):
            try:
                end_date = datetime.fromisoformat(args['end_date'])
            except ValueError:
                return {
                    'error': 'Bad request',
                    'message': 'Неверный формат end_date. Используйте формат YYYY-MM-DDTHH:MM:SS'
                }, 400
        
        is_finished = args.get('is_finished', False)
        
        new_job = Jobs(
            team_leader=args['team_leader'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            start_date=start_date,
            end_date=end_date,
            is_finished=is_finished
        )
        
        db_session.add(new_job)
        db_session.commit()
        
        return {
            'status': 'success',
            'message': 'Работа успешно добавлена',
        }, 201


class JobsResource(Resource):
    def get(self, job_id):            
        job = db_session.query(Jobs).filter(Jobs.id == job_id).first()
        
        if job is None:
            return {
                'error': 'Not found',
                'message': 'Работа не найдена'
            }, 404
        
        job_dict = {
            'id': job.id,
            'team_leader': job.team_leader,
            'job': job.job,
            'work_size': job.work_size,
            'collaborators': job.collaborators,
            'start_date': job.start_date.isoformat() if job.start_date else None,
            'end_date': job.end_date.isoformat() if job.end_date else None,
            'is_finished': job.is_finished
        }
        
        if hasattr(job, 'team_leader_rel') and job.team_leader_rel:
            if hasattr(job.team_leader_rel, 'name'):
                job_dict['team_leader_name'] = f"{job.team_leader_rel.surname} {job.team_leader_rel.name}"
                job_dict['team_leader_email'] = job.team_leader_rel.email
        
        return {
            'status': 'success',
            'job': job_dict
        }, 200
    
    def put(self, job_id):
        job = db_session.query(Jobs).filter(Jobs.id == job_id).first()
        
        if job is None:
            return {
                'error': 'Not found',
                'message': 'Работа не найдена'
            }, 404
        
        parser = create_job_update_parser()
        args = parser.parse_args()
        
        if args.get('team_leader') is not None:
            job.team_leader = args['team_leader']
        
        if args.get('job') is not None:
            job.job = args['job']
        
        if args.get('work_size') is not None:
            job.work_size = args['work_size']
        
        if args.get('collaborators') is not None:
            job.collaborators = args['collaborators']
        
        if args.get('start_date') is not None:
            if args['start_date'] is None:
                job.start_date = None
            else:
                try:
                    job.start_date = datetime.fromisoformat(args['start_date'])
                except ValueError:
                    return {
                        'error': 'Bad request',
                        'message': 'Неверный формат start_date. Используйте формат YYYY-MM-DDTHH:MM:SS'
                    }, 400
        
        if args.get('end_date') is not None:
            if args['end_date'] is None:
                job.end_date = None
            else:
                try:
                    job.end_date = datetime.fromisoformat(args['end_date'])
                except ValueError:
                    return {
                        'error': 'Bad request',
                        'message': 'Неверный формат end_date. Используйте формат YYYY-MM-DDTHH:MM:SS'
                    }, 400
        
        if args.get('is_finished') is not None:
            job.is_finished = args['is_finished']
        
        db_session.commit()
        
        return {
            'status': 'success',
            'message': 'Работа успешно обновлена',
        }, 200
    
    def delete(self, job_id):
        job = db_session.query(Jobs).filter(Jobs.id == job_id).first()
        
        if job is None:
            return {
                'error': 'Not found',
                'message': 'Работа не найдена'
            }, 404
        
        db_session.delete(job)
        db_session.commit()
        
        return {
            'status': 'success',
            'message': 'Работа успешно удалена',
        }, 200