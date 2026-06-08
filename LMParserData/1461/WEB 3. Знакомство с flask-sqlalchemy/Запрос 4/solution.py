db_name = input()

global_init(db_name)
session = create_session()

for colonist in session.query(User).filter((User.position.contains('chief')) | (User.position.contains('middle'))):
    print(f"{colonist} {colonist.position}")

session.close()