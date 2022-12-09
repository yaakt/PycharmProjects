from abc import ABC, abstractmethod


class Cocktail(ABC):
    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_ingredients(self):
        pass


class Oder(Cocktail):

    def get_cost(self):
        return 500

    def get_ingredients(self):
        return 'rum and cola'


class AbstractDecorator(Cocktail):
    def __init__(self, decorated_cocktail):
        self.decorated_cocktail = decorated_cocktail

    def get_cost(self):
        self.decorated_cocktail.get_cost()

    def get_ingredients(self):
        self.decorated_cocktail.get_ingredients()


class Ice(AbstractDecorator):

    def __init__(self, decorated_cocktail):
        AbstractDecorator.__init__(self, decorated_cocktail)

    def get_cost(self):
        return self.decorated_cocktail.get_cost() + 0

    def get_ingredients(self):
        return self.decorated_cocktail.get_ingredients() + ', ice'


class Syrup(AbstractDecorator):

    def __init__(self, decorated_cocktail):
        AbstractDecorator.__init__(self, decorated_cocktail)

    def get_cost(self):
        return self.decorated_cocktail.get_cost() + 100

    def get_ingredients(self):
        return self.decorated_cocktail.get_ingredients() + ', syrup'

Cocktail1 = Oder()
print('Ingredients: ' + Cocktail1.get_ingredients() +
      '; Cost: ' + str(Cocktail1.get_cost()))

Cocktail2 = Ice(Cocktail1)
print('Ingredients: ' + Cocktail2.get_ingredients() +
      '; Cost: ' + str(Cocktail2.get_cost()))

Cocktail3 = Syrup(Cocktail1)
print('Ingredients: ' + Cocktail3.get_ingredients() +
      '; Cost: ' + str(Cocktail3.get_cost()))