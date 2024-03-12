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
        for boton in self.botones_de_piso:
            if boton.numero_de_piso == numero_de_piso:
                print('~~~~~~~~~~~~~~~~~~~')
                print(f' ~~~ SUBIR AL ~~~ \n"PISO: " => {boton.numero_de_piso}')
                print(f'Piso Actual: {self.piso_actual}')
                print(">>>>>> CERRAR ASCENSOR <<<<<<")
                time.sleep(2)
                print("Subiendo:^^^^^^^")
                time.sleep(2)
                while self.piso_actual != numero_de_piso:
                    if self.piso_actual < numero_de_piso:
                        self.subir_piso()
                    else:
                        self.bajar_piso()
                    print("Piso: " + str(self.piso_actual))
                    print('----------------')
                break
                Case 

    def subir_piso(self):
        self.piso_actual = self.piso_actual + 1

    def bajar_piso(self):
        self.piso_actual = self.piso_actual - 1

class ControlDeDirecciones:
    def solicitar_ascensor(self, piso_actual):
        ascensor_disponible = min(self.ascensores, key=lambda ascensor: len(ascensor.destinos_del_piso))
        ascensor_disponible.ir_a_piso(piso_actual)
        ascensor_disponible.ir_a_piso(ascensor_disponible.ir_a_piso)

class BotonDePiso:
    def __init__(self, numero_de_piso):
        self.numero_de_piso = numero_de_piso
        self.encendido = False

botones_de_pisos = [BotonDePiso(i) for i in range(6)]
ascensorA = Ascensor(botones_de_pisos)

pisos = [Piso(i, ascensorA) for i in range(6)]

pisos[0].llamar_ascensor(arriba=True)
ascensorA.ir_al_piso(5)

pisos[3].llamar_ascensor(arriba=False)
ascensorA.ir_al_piso(0)

# edificio_torre = Configuracion(15, 2)