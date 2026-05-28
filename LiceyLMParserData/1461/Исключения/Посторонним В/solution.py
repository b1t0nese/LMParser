class NoArgsError(Exception):
    pass


class EmptyListError(Exception):
    pass


def strangers(*data):
    if not data:
        raise NoArgsError("The arguments are not passed.")
    new_data = []
    for dat in data:
        if isinstance(dat, int):
            s_dat, dat, prime_divisors = dat, abs(dat), set()
            if dat == 0:
                new_data.append(dat)
                continue
            if dat % 2 == 0:
                prime_divisors.add(2)
                while dat % 2 == 0:
                    dat //= 2
            i = 3
            while i * i <= dat:
                if dat % i == 0:
                    prime_divisors.add(i)
                    while dat % i == 0:
                        dat //= i
                i += 2
            if dat > 1:
                prime_divisors.add(dat)
            if len(prime_divisors) != 5:
                new_data.append(s_dat)
        else:
            raise ValueError("There are not only numbers among the arguments!")
    if new_data:
        new_data.sort()
        return new_data
    else:
        raise EmptyListError("There were no suitable numbers.")