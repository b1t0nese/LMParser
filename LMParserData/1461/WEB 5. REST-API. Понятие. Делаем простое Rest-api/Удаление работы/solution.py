import flask
from . import db_session
from .jobs import Jobs
from datetime import datetime

jobs_api = flask.Blueprint('jobs_api', __name__, template_folder='templates')


@jobs_api.route('/api/jobs/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    job = db_session.query(Jobs).filter(Jobs.id == job_id).first()
    
    if job is None:
        return flask.jsonify({
            'error': 'Not found',
            'message': 'Работа не найдена'
        }), 404
    
    db_session.delete(job)
    db_session.commit()
    
    return flask.jsonify({
        'status': 'success',
        'message': f'Работа успешно удалена',
    }), 200
