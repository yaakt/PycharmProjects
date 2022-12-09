class Russia:
    __instance__ = None

    def __init__(self):
        if Russia.__instance__ is None:
            Russia.__instance__ = self
        else:
            raise Exception("You cannot add another Russia class")

    @staticmethod
    def get_instance():
        if not Russia.__instance__:
            Russia()
        return Russia.__instance__


country = Russia()
print(country)

same_country = Russia.get_instance()
print(same_country)

new_country = Russia()
print(new_country)
