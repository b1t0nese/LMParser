import flask
from . import db_session
from .jobs import Jobs
from datetime import datetime

jobs_api = flask.Blueprint('jobs_api', __name__, template_folder='templates')


@jobs_api.route('/api/jobs/<int:job_id>', methods=['PUT'])
def edit_job(job_id):
    job = db_session.query(Jobs).filter(Jobs.id == job_id).first()
    
    if job is None:
        return flask.jsonify({
            'error': 'Not found',
            'message': 'Работа не найдена'
        }), 404
    
    data = flask.request.get_json()
    
    if not data:
        return flask.jsonify({
            'error': 'Bad request',
            'message': 'Отсутствуют данные в запросе'
        }), 400
    
    if 'team_leader' in data:
        try:
            job.team_leader = int(data['team_leader'])
        except (ValueError, TypeError):
            return flask.jsonify({
                'error': 'Bad request',
                'message': 'Поле team_leader должно быть числом'
            }), 400
    
    if 'job' in data:
        job.job = str(data['job'])
    
    if 'work_size' in data:
        try:
            job.work_size = int(data['work_size'])
        except (ValueError, TypeError):
            return flask.jsonify({
                'error': 'Bad request',
                'message': 'Поле work_size должно быть числом'
            }), 400
    
    if 'collaborators' in data:
        job.collaborators = str(data['collaborators'])
    
    if 'start_date' in data:
        if data['start_date'] is None:
            job.start_date = None
        else:
            try:
                job.start_date = datetime.fromisoformat(data['start_date'])
            except ValueError:
                return flask.jsonify({
                    'error': 'Bad request',
                    'message': 'Неверный формат start_date. Используйте формат YYYY-MM-DDTHH:MM:SS'
                }), 400
    
    if 'end_date' in data:
        if data['end_date'] is None:
            job.end_date = None
        else:
            try:
                job.end_date = datetime.fromisoformat(data['end_date'])
            except ValueError:
                return flask.jsonify({
                    'error': 'Bad request',
                    'message': 'Неверный формат end_date. Используйте формат YYYY-MM-DDTHH:MM:SS'
                }), 400
    
    if 'is_finished' in data:
        if not isinstance(data['is_finished'], bool):
            return flask.jsonify({
                'error': 'Bad request',
                'message': 'Поле is_finished должно быть true/false'
            }), 400
        job.is_finished = data['is_finished']
    
    db_session.commit()
    
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
    
    return flask.jsonify({
        'status': 'success',
        'message': 'Работа успешно обновлена',
        'job': job_dict
    }), 200