from clases import Tablero
from itertools import product

class Case:

      jugadas = set()

      def __init__(self, x, y):
          instances = {}
          # Adición de las coordenadas
          self.x = x
          self.y = y
          # Queremos poder acceder a una casilla a partir de sus coordenadas
          instances[x, y] = self

          # Generación del nombre de la casilla
          self._generar_nombre_casilla()
          # Queremos poder acceder a una casilla a partir de su nombre
          instances[self.nombre] = self

          # Evolución de la casilla
          self.jugada = False
          self.barco = None  # No toca a un barco de momento.
      @staticmethod
      def _generar_nombre_casilla(x,y):
          """Este método puede ser sobrecargado fácilmente"""
          casilla = (x,y)
          return casilla

      def jugar(self):
          """Describe qué pasa cuando jugamos una casilla"""
          self.jugada = True
          self.jugadas.add(self)

          if self.barco is not None:
              if len(self.Barco.casillas - self.casillas_jugadas) == 0:
                  print("Hundido !!")
              else:
                  print("Tocado !")
          else:
              print("Agua !")

      def generar_casillas():
          for x, y in product(range(Tablero.num_lineas),range(Tablero.num_columnas)):
              Case(x, y)

      def __str__(self):
          """Sobrecarga del método de transformación en cadena"""
          if not self.jugada:
              return "CASO_NO_JUGADO"
          elif self.barco is None:
              return "CASO_AGUA"
          else:
              return "CASO_TOCADO"
