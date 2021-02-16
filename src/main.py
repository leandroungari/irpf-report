from loader import load_settings
from declaration.acoes import Acoes
from declaration.fiis import Fiis

class Application:
    def start(self):
        self.__settings = load_settings()
        self.__builders = {
            "acoes": Acoes(self.__settings.produtos[31]),
            "fiis": Fiis(self.__settings.produtos[73])
        }

    def generate(self):
        self.result = []
        for builder in self.__builders.values():
            content = builder.generate()
            self.result = self.result + content

    def persist(self):
        with open("data/output.txt", "w", encoding="utf-8") as file:
            for item in self.result:
                file.write(item)

            file.close()
    

if __name__ == "__main__":
    app = Application()
    app.start()
    app.generate()
    app.persist()