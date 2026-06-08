import flask
from . import db_session
from .jobs import Jobs

jobs_api = flask.Blueprint('jobs_api', __name__, template_folder='templates')


@jobs_api.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_job_by_id(job_id):
    job = db_session.query(Jobs).filter(Jobs.id == job_id).first()
    
    if job is None:
        return flask.jsonify({
            'error': 'Not found',
            'message': 'Работа не найдена'
        }), 404
    
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
            job_dict['team_leader_name'] = job.team_leader_rel.name
    
    return flask.jsonify({
        'job': job_dict
    })