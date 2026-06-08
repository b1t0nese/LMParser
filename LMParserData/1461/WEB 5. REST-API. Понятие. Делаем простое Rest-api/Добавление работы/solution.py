import flask
from . import db_session
from .jobs import Jobs
from datetime import datetime

jobs_api = flask.Blueprint('jobs_api', __name__, template_folder='templates')


@jobs_api.route('/api/jobs', methods=['POST'])
def add_job():
    data = flask.request.get_json()
    
    if not data:
        return flask.jsonify({
            'error': 'Bad request',
            'message': 'Отсутствуют данные в запросе'
        }), 400
    
    required_fields = ['team_leader', 'job', 'work_size', 'collaborators']
    missing_fields = [field for field in required_fields if field not in data]
    
    if missing_fields:
        return flask.jsonify({
            'error': 'Bad request',
            'message': f'Отсутствуют обязательные поля'
        }), 400
    
    try:
        team_leader = int(data['team_leader'])
        work_size = int(data['work_size'])
    except (ValueError, TypeError):
        return flask.jsonify({
            'error': 'Bad request',
            'message': 'Поля team_leader и work_size должны быть числами'
        }), 400
    
    job_title = str(data['job'])
    collaborators = str(data['collaborators'])
    
    start_date = None
    if 'start_date' in data and data['start_date']:
        try:
            start_date = datetime.fromisoformat(data['start_date'])
        except ValueError:
            return flask.jsonify({
                'error': 'Bad request',
                'message': 'Неверный формат start_date. Используйте формат YYYY-MM-DDTHH:MM:SS'
            }), 400
    else:
        start_date = datetime.now()
    
    end_date = None
    if 'end_date' in data and data['end_date']:
        try:
            end_date = datetime.fromisoformat(data['end_date'])
        except ValueError:
            return flask.jsonify({
                'error': 'Bad request',
                'message': 'Неверный формат end_date. Используйте формат YYYY-MM-DDTHH:MM:SS'
            }), 400
    
    is_finished = data.get('is_finished', False)
    if not isinstance(is_finished, bool):
        return flask.jsonify({
            'error': 'Bad request',
            'message': 'Поле is_finished должно быть true/false'
        }), 400
    
    new_job = Jobs(
        team_leader=team_leader,
        job=job_title,
        work_size=work_size,
        collaborators=collaborators,
        start_date=start_date,
        end_date=end_date,
        is_finished=is_finished
    )
    
    db_session.add(new_job)
    db_session.commit()
    
    job_dict = {
        'id': new_job.id,
        'team_leader': new_job.team_leader,
        'job': new_job.job,
        'work_size': new_job.work_size,
        'collaborators': new_job.collaborators,
        'start_date': new_job.start_date.isoformat() if new_job.start_date else None,
        'end_date': new_job.end_date.isoformat() if new_job.end_date else None,
        'is_finished': new_job.is_finished
    }
    
    return flask.jsonify({
        'status': 'success',
        'message': 'Работа успешно добавлена',
        'job': job_dict
    }), 201