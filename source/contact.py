class Contact:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def greet(self):
        return f"Salut je m'appelle {self.name} et j'ai {self.age} ans"
