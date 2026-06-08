db_name = input()

global_init(db_name)
session = create_session()

results = session.query(User.id).filter(
    User.address == 'module_1',
    ~User.speciality.contains('engineer'),
    ~User.position.contains('engineer')
).all()

for user_id, in results:
    print(user_id)

session.close()