#                               +-----------------------------------+
#                               |             Torneo                |
#                               +-----------------------------------+
#                               | - fecha: str                      |
#                               | - pista: Pista                    |
#                               | - tabla_posiciones: TablaPosiciones|
#                               +-----------------------------------+
#                               | + agregar_auto(auto: Auto)        |
#                               | + mostrar_posiciones()            |
#                               +-----------------------------------+
#                               
#                               +-----------------------------------+
#                               |              Pista                |
#                               +-----------------------------------+
#                               | - nombre: str                     |
#                               | - distancia_km: float             |
#                               +-----------------------------------+
#                               
#                               +-----------------------------------+
#                               |              Auto                 |
#                               +-----------------------------------+
#                               | - marca: str                      |
#                               | - peso: float                     |
#                               | - velocidad_max: float            |
#                               | - potencia: int                   |
#                               | - piloto: Piloto                  |
#                               +-----------------------------------+
#                               
#                               +-----------------------------------+
#                               |              Piloto               |
#                               +-----------------------------------+
#                               | - nombre: str                     |
#                               | - apellido: str                   |
#                               | - nro_inscripcion: int            |
#                               | - experiencia: int                |
#                               +-----------------------------------+
#                               
#                               +-----------------------------------+
#                               |        TablaPosiciones            |
#                               +-----------------------------------+
#                               | - posiciones: list                |
#                               +-----------------------------------+
#                               | + agregar_auto(auto: Auto)        |
#                               | + mostrar_posiciones()            |
#                               +-----------------------------------+

class Piloto:
    def __init__(self, nombre, apellido, nro_inscripcion, experiencia):
        self.nombre = nombre
        self.apellido = apellido
        self.nro_inscripcion = nro_inscripcion
        self.experiencia = experiencia

class Auto:
    def __init__(self, marca, peso, velocidad_max, potencia, piloto):
        self.marca = marca
        self.peso = peso
        self.velocidad_max = velocidad_max
        self.potencia = potencia
        self.piloto = piloto

class Pista:
    def __init__(self, nombre, distancia_km):
        self.nombre = nombre
        self.distancia_km = distancia_km

class TablaPosiciones:
    def __init__(self):
        self.posiciones = []

    def agregar_auto(self, auto):
        self.posiciones.append(auto)

    def mostrar_posiciones(self):
        for idx, auto in enumerate(self.posiciones, 1):
            piloto = auto.piloto
            print(f"{idx}. {piloto.nombre} {piloto.apellido} - {auto.marca} ({auto.potencia} HP)")

class Torneo:
    def __init__(self, fecha, pista):
        self.fecha = fecha
        self.pista = pista
        self.tabla_posiciones = TablaPosiciones()

    def agregar_auto(self, auto):
        self.tabla_posiciones.agregar_auto(auto)

    def mostrar_posiciones(self):
        print(f"Torneo en {self.pista.nombre} - {self.fecha}")
        self.tabla_posiciones.mostrar_posiciones()

# Ejemplo de uso:



piloto1 = Piloto("Checo", "Pérez", 101, 5)
piloto2 = Piloto("Carlos", "Gómez", 102, 3)

auto1 = Auto("Ferrari", 1200, 350, 700, piloto1)
auto2 = Auto("Lotus", 1300, 360, 750, piloto2)

pista = Pista("Monza", 5.8)

torneo = Torneo("2024-09-20", pista)
torneo.agregar_auto(auto1)
torneo.agregar_auto(auto2)

torneo.mostrar_posiciones()
