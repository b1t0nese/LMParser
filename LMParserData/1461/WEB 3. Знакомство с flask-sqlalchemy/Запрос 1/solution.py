db_name = input()

global_init(db_name)
session = create_session()

for colonist in session.query(User).filter(User.address == 'module_1'):
    print(colonist)

session.close()