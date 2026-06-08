import datetime


class Place:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def __repr__(self):
        return f"({self.row},{self.column})"


class Hall:
    def __init__(self, hall_id, name, rows, columns):
        self.hall_id = hall_id
        self.name = name
        self.places = []
        for r in range(1, rows + 1):
            for s in range(1, columns + 1):
                self.places.append(Place(r, s))
        self.capacity = len(self.places)

    def __repr__(self):
        return f"Зал '{self.name}' (ID: {self.hall_id}, Мест: {self.capacity})"


class Movie:
    def __init__(self, movie_id, title, duration_minutes):
        self.movie_id = movie_id
        self.title = title
        self.duration_minutes = duration_minutes

    def __repr__(self):
        return f"Фильм '{self.title}' (ID: {self.movie_id}, Длительность: {self.duration_minutes} минут)"


class Session:
    def __init__(self, session_id, movie, hall, start_time):
        self.session_id = session_id
        self.movie = movie
        self.hall = hall
        self.start_time = start_time
        self.end_time = start_time + datetime.timedelta(minutes=movie.duration_minutes)
        self.occupied_places = set()

    def is_place_available(self, row, column):
        return (row, column) not in self.occupied_places

    def places(self, row, column):
        if self.is_place_available(row, column):
            self.occupied_places.add((row, column))
            return True
        return False

    def print_placing_plan(self):
        print(f"\n### План зала для сеанса {self.session_id} ({self.movie.title}) ###")
        max_row = 0
        max_place_num = 0
        if self.hall.places:
            max_row = max(place.row for place in self.hall.places)
            max_place_num = max(place.column for place in self.hall.places)

        for r in range(1, max_row + 1):
            row_display = f"Ряд {r}: "
            for s in range(1, max_place_num + 1):
                if (r, s) in self.occupied_places:
                    row_display += "[X]"
                else:
                    row_display += "[ ]"
            print(row_display)
        print("------------------------------------------")

    def __repr__(self):
        x = self.session_id
        y = self.movie.title
        z = self.start_time.strftime('%Y-%m-%d %H:%M')
        return f"Сеанс (ID: {x}, Фильм: '{y}', Зал: '{self.hall.name}', Начало: {z})"


class Cinema:
    def __init__(self, cinema_id, name):
        self.cinema_id = cinema_id
        self.name = name
        self.halls = []
        self.sessions = []
        self._next_hall_id_counter = 1
        self._next_session_id_counter = 1

    def add_hall(self, name, rows, places_per_row):
        hall_id = f"{self.cinema_id}-H{self._next_hall_id_counter}"
        new_hall = Hall(hall_id, name, rows, places_per_row)
        self.halls.append(new_hall)
        self._next_hall_id_counter += 1
        print(f"Зал '{name}' добавлен в кинотеатр '{self.name}'")
        return new_hall

    def get_hall_by_id(self, hall_id):
        for hall in self.halls:
            if hall.hall_id == hall_id:
                return hall
        return None

    def add_session(self, movie, hall, start_time):
        session_id = f"{self.cinema_id}-S{self._next_session_id_counter}"
        new_session = Session(session_id, movie, hall, start_time)
        self.sessions.append(new_session)
        self._next_session_id_counter += 1
        print(f"Сеанс '{movie.title}' в зале '{hall.name}' создан")
        return new_session

    def __repr__(self):
        return f"Кинотеатр '{self.name}' (ID: {self.cinema_id}, Залов: {len(self.halls)}, Сеансов: {len(self.sessions)})"


class TicketSystem:
    def __init__(self):
        self.cinemas = []
        self.movies = []
        self._next_cinema_id_counter = 1

    def add_movie(self, title, duration_minutes):
        movie_id = f"M{len(self.movies) + 1}"
        new_movie = Movie(movie_id, title, duration_minutes)
        self.movies.append(new_movie)
        print(f"Фильм '{title}' добавлен")
        return new_movie

    def get_movie_by_id(self, movie_id):
        for movie in self.movies:
            if movie.movie_id == movie_id:
                return movie
        return None

    def add_cinema(self, name):
        cinema_id = f"C{self._next_cinema_id_counter}"
        new_cinema = Cinema(cinema_id, name)
        self.cinemas.append(new_cinema)
        self._next_cinema_id_counter += 1
        print(f"Кинотеатр '{name}' добавлен")
        return new_cinema

    def get_cinema_by_id(self, cinema_id):
        for cinema in self.cinemas:
            if cinema.cinema_id == cinema_id:
                return cinema
        return None

    def create_session(self, cinema_id, hall_id, movie_id, start_time_str):
        cinema = self.get_cinema_by_id(cinema_id)
        if not cinema:
            print(f"Кинотеатр с ID {cinema_id} не найден")
            return None

        hall = cinema.get_hall_by_id(hall_id)
        if not hall:
            print(f"Зал с ID {hall_id} не найден в кинотеатре '{cinema.name}'")
            return None

        movie = self.get_movie_by_id(movie_id)
        if not movie:
            print(f"Фильм с ID {movie_id} не найден.")
            return None

        try:
            start_time = datetime.datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Неверный формат времени. Используйте ГГГГ-ММ-ДД ЧЧ:ММ")
            return None

        return cinema.add_session(movie, hall, start_time)

    def find_available_session(self, movie_id, desired_start_time_str):
        movie = self.get_movie_by_id(movie_id)
        if not movie:
            print(f"Фильм с ID {movie_id} не найден.")
            return None

        try:
            desired_start_time = datetime.datetime.strptime(desired_start_time_str, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Неверный формат времени. Используйте ГГГГ-ММ-ДД ЧЧ:ММ")
            return None

        available_sessions = []
        for cinema in self.cinemas:
            for session in cinema.sessions:
                if session.movie.movie_id == movie_id and session.start_time >= desired_start_time:
                    if len(session.occupied_places) < session.hall.capacity:
                        available_sessions.append(session)

        if not available_sessions:
            print("Ближайших сеансов с доступными местами для этого фильма не найдено")
            return None

        available_sessions.sort(key=lambda s: s.start_time)
        return available_sessions[0]

    def book_ticket(self, session_id, row, column):
        session_to_book = None
        for cinema in self.cinemas:
            for session in cinema.sessions:
                if session.session_id == session_id:
                    session_to_book = session
                    break
            if session_to_book:
                break

        if not session_to_book:
            print(f"Сеанс с ID {session_id} не найден.")
            return False

        if session_to_book.places(row, column):
            print(f"Билет на сеанс {session_id} (ряд {row}, место {column}) успешно продан")
            return True
        else:
            print(f"Место (ряд {row}, место {column}) на сеанс {session_id} уже занято")
            return False


# Создание системы
ticket_system = TicketSystem()


# Создание кинотеатров
cinema1 = ticket_system.add_cinema("Star Cinema")
cinema2 = ticket_system.add_cinema("Мир")


# Создание и привязка залов к кинотеатрам
# Star Cinema
hall1_1 = cinema1.add_hall("Зал №1", 8, 12)  # 8 рядов 12 коллон
hall1_2 = cinema1.add_hall("Зал №2", 10, 15)
# Мир
hall2_1 = cinema2.add_hall("Зал №1", 8, 10)
hall2_2 = cinema2.add_hall("Зал №2", 10, 12)


# Создание фильмов
mov1 = ticket_system.add_movie("Интерстеллар", 169)  # Название и продолжительность
mov2 = ticket_system.add_movie("Форест Гамп", 144)
mov3 = ticket_system.add_movie("Джокер", 122)
mov4 = ticket_system.add_movie("Вызов", 164)


# Создание сеансов
# Star Cinema
session1 = ticket_system.create_session(cinema1.cinema_id, hall1_1.hall_id, mov1.movie_id, "2025-09-23 14:00")
session2 = ticket_system.create_session(cinema1.cinema_id, hall1_1.hall_id, mov2.movie_id, "2025-09-23 17:00")
session3 = ticket_system.create_session(cinema1.cinema_id, hall1_2.hall_id, mov3.movie_id, "2025-09-23 19:00")
# Мир
session4 = ticket_system.create_session(cinema1.cinema_id, hall2_1.hall_id, mov1.movie_id, "2025-09-23 10:00")
session5 = ticket_system.create_session(cinema2.cinema_id, hall2_2.hall_id, mov4.movie_id, "2025-09-23 15:00")


# Продажа билетов
print("\n### Продажа билетов ###")
if session1:
    ticket_system.book_ticket(session1.session_id, 5, 10)
    ticket_system.book_ticket(session1.session_id, 5, 11)
    ticket_system.book_ticket(session1.session_id, 1, 1)
    # Попытка продажи занятого места
    ticket_system.book_ticket(session1.session_id, 5, 10)
print("-----------------------")


# Вывод плана на сеанс
session1.print_placing_plan()


# Поиск ближайшего сеанса на mov1
print("\n### Поиск ближайшего сеанса ###")
found_session = ticket_system.find_available_session(mov1.movie_id, "2025-09-23 09:00")
if found_session:
    print(f"Ближайший доступный сеанс: {found_session}")
