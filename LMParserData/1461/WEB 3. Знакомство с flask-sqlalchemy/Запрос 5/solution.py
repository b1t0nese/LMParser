db_name = input()

global_init(db_name)
session = create_session()

for job in session.query(Jobs).filter(Jobs.work_size < 20, Jobs.is_finished == 0):
    print(f"<Job> {job.job}")
    
session.close()