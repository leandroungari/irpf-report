from loader import welcome, load_settings
from declaration.acoes import Acoes

class Application:
    def start(self):
        welcome()
        self.__settings = load_settings()
        self.__builders = {
            "acoes": Acoes(self.__settings.produtos[31])
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