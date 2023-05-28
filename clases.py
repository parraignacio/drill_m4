
import csv


class Vehiculo:
    def __init__(self, marca, modelo, nruedas):
        self.marca = marca
        self.modelo = modelo
        self.nruedas = nruedas
     
    def guardar_datos_csv(self):
        try:
            with open("vehiculos.csv", "a", newline="") as archivo:
                datos = [(f"<class 'Vehiculo.{self.__class__.__name__}'>", self.__dict__)]
                archivo_csv = csv.writer(archivo)
                archivo_csv.writerows(datos)
        
        except FileNotFoundError:
            print("No se ha encontrado el archivo vehiculos.csv")     
        
        except Exception as error:
            print('Se ha generado un error no previsto', type(error).__name__)
    
    def leer_datos_csv(self):
        try:
            with open("vehiculos.csv", "r") as archivo:
                vehiculos = csv.reader(archivo)
                print(f"Lista de Vehículos {type(self).__name__}")
                for item in vehiculos:
                    vehiculo_tipo = type(self).__name__
                    if vehiculo_tipo in item[0]:
                        print(item[1])
                
        except FileNotFoundError:
            print("No se ha encontrado el archivo vehiculos.csv")     
        
        except Exception as error:
            print('Se ha generado un error no previsto', type(error).__name__)
            
    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, {self.nruedas} ruedas"
 

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, nruedas, velocidad, cilindraje):
        super().__init__(marca, modelo, nruedas)
        self.velocidad = velocidad
        self.cilindraje = cilindraje
        
    def __str__(self):
        return f"{super().__str__()}, {self.velocidad} km/h, {self.cilindraje} cc"

class Particular(Automovil):
    def __init__(self, marca, modelo, nruedas, velocidad, cilindraje, npuestos):
        super().__init__(marca, modelo, nruedas, velocidad, cilindraje)
        self.npuestos = npuestos

    def set_npuestos(self, npuestos_new):
        self.npuestos = npuestos_new
        
    def get_npuestos(self):
        return self.npuestos
    
    def __str__(self):
        return f"{super().__str__()}, Puestos: {self.npuestos}"
        

class Carga(Automovil):
    def __init__(self, marca, modelo, nruedas, velocidad, cilindraje, peso_carga):
        super().__init__(marca, modelo, nruedas, velocidad, cilindraje)
        self.peso_carga = peso_carga
    
    def set_peso_carga(self, peso_carga_new):
        self.peso_carga =peso_carga_new
        
    def get_peso_carga(self):
        return self.peso_carga
    
    def __str__(self):
        return f"{super().__str__()}, Carga: {self.peso_carga} Kg"
        
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, nruedas, tipo):
        super().__init__(marca, modelo, nruedas)
        self.tipo = tipo

    def set_tipo(self, tipo_new):
        self.tipo = tipo_new
        
    def get_npuestos(self):
        return self.tipo
    
    def __str__(self):
        return f"{super().__str__()}, Tipo: {self.tipo}"
    
    
class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, nruedas, tipo, motor, cuadro, nradios):
        super().__init__(marca, modelo, nruedas, tipo)
        self.motor = motor
        self.cuadro = cuadro
        self.nradios = nradios
     
    def __str__(self):   
        return f"{super().__str__()}, Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.nradios}"