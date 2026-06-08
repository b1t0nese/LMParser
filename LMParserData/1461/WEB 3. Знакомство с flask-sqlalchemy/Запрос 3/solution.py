db_name = input()

global_init(db_name)
session = create_session()

for colonist in session.query(User).filter(User.age < 18):
    print(f"{colonist} {colonist.age} years")

session.close()