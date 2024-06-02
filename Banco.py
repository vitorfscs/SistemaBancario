class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "AU AU"
    
class gato(Animal):
    def fazer_som(self):
        return "Miau"
    
cachorro = Cachorro("REX")
Gato = gato("Whiska")

print(cachorro.fazer_som())  # Saída: Au Au
print(Gato.fazer_som()) # Saída: Miau