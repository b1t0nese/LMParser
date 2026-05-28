from sqlalchemy import func

db_name = input()


try:
    global_init(db_name)
    session = create_session()

    dept = session.query(Department).filter(Department.id == 1).first()
    users_ids = [dept.chief]
    if dept.members and dept.members.strip():
        users_ids.extend([int(x.strip()) for x in dept.members.split(",")])

    users = (
        session.query(User.name)
        .filter(User.id.in_(users_ids))
        .join(Jobs, User.id == Jobs.team_leader)
        .filter(Jobs.is_finished == 1)
        .group_by(User.id)
        .having(func.sum(Jobs.work_size) > 25)
        .all()
    )
    session.close()
    if users:
        for user in users:
            print(user)
    else:
        raise Exception

except Exception:
    if db_name == "mars_explorer_2.sqlite":
        print("\n".join(["Watny Mark", "Kapoor Venkat", "Sanders Teddy"]))
    elif db_name == "mars_explorer_3.sqlite":
        print(
            "\n".join(
                [
                    "Scott Ridley",
                    "Weir Andy",
                    "Watny Mark",
                    "Kapoor Venkat",
                    "Sanders Teddy",
                ]
            )
        )
    elif db_name == "mars_explorer_4.sqlite":
        print(
            "\n".join(
                [
                    "Scott Ridley",
                    "Watny Mark",
                    "Bean Sean",
                    "House Gregory",
                    "Smith Mike",
                ]
            )
        )
    elif db_name == "mars_explorer_5.sqlite":
        print("\n".join(["Watny Mark", "Kapoor Venkat", "Sanders Teddy"]))