import time
class Edificio:

    def __init__(self, pisos, ascensores):
        self.pisos = pisos
        self.ascensores = ascensores

class Piso:
    def __init__(self, numero_piso, ascensor):
        self.numero_piso = numero_piso
        self.boton_arriba = False
        self.boton_abajo = False
        self.ascensor = ascensor
        self.tiempo_de_apertura_ascensor = 5

    def llamar_ascensor(self, arriba):
        if arriba:
            self.boton_arriba = True
            self.abrir_ascensor()
            self.boton_arriba = False
        else:
            print("Bajando:.........")
            self.boton_abajo = True
            self.abrir_ascensor()
            self.boton_abajo = False

    def abrir_ascensor(self):
        print("<<<<<< ABRIR ASCENSOR >>>>>>")
        self.ascensor.abierto = True
        self.ascensor.abierto = False
        time.sleep(2)

class Ascensor:
    def __init__(self, botones_de_piso):
        self.botones_de_piso = botones_de_piso
        self.piso = 0
        self.piso_actual = 0
        self.abierto = False

    def ir_al_piso(self, numero_de_piso):
        botones = list(filter(lambda button: button.numero_de_piso == numero_de_piso, self.botones_de_piso))
        print('----------------')
        boton_presionado = botones[0]
        print(f'--Yendo al Piso: {boton_presionado.numero_de_piso}')
        print(f'Piso Actual: {self.piso_actual}')
        while self.piso_actual != numero_de_piso:
            if self.piso_actual < numero_de_piso:
                self.subir_piso()
            else:
                self.bajar_piso()
                print("Piso: " + str(self.piso_actual))
                print('----------------')
            if self.piso_actual != numero_de_piso:
                 print(f'Error!! El piso {numero_de_piso} no existe en el edificio')
                 print('----------------')
    def subir_piso(self):
        self.piso_actual = self.piso_actual + 1

    def bajar_piso(self):
        self.piso_actual = self.piso_actual - 1

class BotonDePiso:
    def __init__(self, numero_de_piso):
        self.numero_de_piso = numero_de_piso
        self.encendido = False

class Configuracion():
    def __init__(self, numero_de_piso, ascensor, pisos):
        self.numero_de_piso = 0
        self.ascensor = 1
        self.pisos = []

    def edificio_torre(self, pisos):
        self.botones_de_pisos = [BotonDePiso(i) for i in range(self.ascensor)]
        self.ascensorA = Ascensor(self.botones_de_pisos)
        self.pisos = [Piso(i, self.ascensorA) for i in range(self.numero_de_piso + 1)]

numero_de_pisos = 15

edificio_torre = Configuracion(0, 1, 15)
edificio_torre.pisos[0].llamar_ascensor(arriba=True)
ediificio_torre.ascensorA.ir_al_piso()
