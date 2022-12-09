from abc import ABC, abstractmethod


class Netflix:
    def __init__(self):
        self.subscribers = set()

    def subscribe(self, who):
        self.subscribers.add(who)

    def unsubscribe(self, who):
        self.subscribers.discard(who)

    def notify(self):
        for subscriber in self.subscribers:
            subscriber.message()


class AbstractObserver(ABC):
    @abstractmethod
    def message(self):
        pass


class Subscriber(AbstractObserver):
    def __init__(self, name):
        self.name = name

    def message(self):
        print('{}, do not forget your subscription'.format(self.name))


subscriber1 = Subscriber('Bob')
subscriber2 = Subscriber('Lilly')
subscriber3 = Subscriber('Jane')

app = Netflix()

app.subscribe(subscriber1)
app.subscribe(subscriber2)
app.subscribe(subscriber3)

app.notify()

app.unsubscribe(subscriber3)

app.notify()
