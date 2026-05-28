class PizzaWithoutDoughError(Exception):
    pass


class SauceLackError(PizzaWithoutDoughError):
    pass


class NotEnoughCheeseError(PizzaWithoutDoughError):
    pass


class AnanasError(PizzaWithoutDoughError):
    pass


class OutOfGroceriesError(Exception):
    pass


def pizza(*ingredients, vegan=False, sauce=None):
    ingredients = list(ingredients)

    if 'dough' not in ingredients:
        raise PizzaWithoutDoughError("You can't make pizza without dough.")
    if sauce is not None:
        if sauce not in ingredients:
            raise SauceLackError("Where's the sauce?")
        ingredients.remove(sauce)
    cheeses = []
    for item in ingredients:
        if 'cheese' in item:
            cheeses.append(item)
    if len(cheeses) < 2:
        raise NotEnoughCheeseError("You're not using enough cheese on that pizza.")
    for cheese in cheeses:
        ingredients.remove(cheese)
    for ingredient in ingredients:
        if 'ananas' in ingredient or 'pineapple' in ingredient:
            raise AnanasError("Pineapple on pizza!")
    if vegan:
        ingredients = [i for i in ingredients if 'meat' not in i]

    ingredients.remove('dough')
    ingredients.sort(key=lambda x: (-len(x), x))
    if not ingredients:
        raise OutOfGroceriesError("There's nothing to put in the pizza.")

    pizza = ['dough']
    if sauce is not None:
        pizza.append(sauce)
    pizza.append(cheeses[0])
    for cheese in cheeses[1:-1]:
        pizza.append(cheese)
    pizza.extend(ingredients)
    pizza.append(cheeses[-1])
    return pizza