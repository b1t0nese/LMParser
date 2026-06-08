import flask
from . import db_session
from .jobs import Jobs

jobs_api = flask.Blueprint('jobs_api', __name__, template_folder='templates')


@jobs_api.route('/api/jobs', methods=['GET'])
def get_all_jobs():
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
        jobs_list.append(job_dict)
    
    return flask.jsonify({
        'jobs': jobs_list,
        'count': len(jobs_list)
    })
