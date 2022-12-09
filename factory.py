class GreekTranslator:

    def __init__(self):
        self.translations = {"song": "τραγούδι", "word": "λέξη"}

    def translate(self, msg):
        return self.translations.get(msg, msg)


class SpanishTranslator:

    def __init__(self):
        self.translations = {"song": "canción", "word": "palabra"}

    def translate(self, msg):
        return self.translations.get(msg, msg)


class EnglishTranslator:

    def translate(self, msg):
        return msg


def Factory(language="English"):
    translators = {
        "Greek": GreekTranslator,
        "English": EnglishTranslator,
        "Spanish": SpanishTranslator,
    }

    return translators[language]()


if __name__ == "__main__":
    f = Factory("Greek")
    e = Factory("English")
    s = Factory("Spanish")

    message = ["song", "word"]

    for msg in message:
        print(f.translate(msg))
        print(e.translate(msg))
        print(s.translate(msg))


