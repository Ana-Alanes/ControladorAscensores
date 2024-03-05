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

    def ir_piso_arriba(self):
        self.boton_arriba = True
        self.ascensor.abierto = True
        ## Aqui poner Codigo para que espere 5 segundos
        self.ascensor.abierto = False
        self.boton_arriba = False

    def ir_piso_abajo(self):
        pass

class Ascensor:
    def __init__(self, botones_de_piso):
        self.botones_de_piso = botones_de_piso
        self.piso = 0
        self.abierto = False

    def ir_al_piso(self, numero_de_piso):
        botones = list(filter(lambda button: button.numero_de_piso == numero_de_piso, self.botones_de_piso))
        print('----------------')
        boton_presionado = botones[0]
        print(boton_presionado.numero_de_piso)
        print(f'--Yendo al Piso: {boton_presionado.numero_de_piso}')
        print('----------------')


class BotonDePiso:
    def __init__(self, numero_de_piso):
        self.numero_de_piso = numero_de_piso
        self.encendido = False



####--------------------------------------------

boton_piso0 = BotonDePiso(0)
boton_piso1 = BotonDePiso(1)
boton_piso2 = BotonDePiso(2)
boton_piso3 = BotonDePiso(3)
botones_de_pisos = [boton_piso0, boton_piso1, boton_piso2, boton_piso3]

ascensorA = Ascensor(botones_de_pisos)
piso0 = Piso(0, ascensorA)
piso1 = Piso(1, ascensorA)
piso2 = Piso(2, ascensorA)
piso3 = Piso(3, ascensorA)



pisos = [piso0, piso1, piso2, piso3]



ascensores = [ascensorA]

edificio_carilo = Edificio(pisos, ascensorA)

piso0.ir_piso_arriba()
ascensorA.ir_al_piso(3)
ascensorA.ir_al_piso(2)

# edificio_torre = Configuracion(15, 2)