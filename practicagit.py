class Paciente:
    def __init__(self):
        self._nombre = ""
        self._cedula = 0
        self._genero = ""
        self._servicio = ""

    def verNombre(self):
        return self._nombre

    def verServicio(self):
        return self._servicio

    def verGenero(self):
        return self._genero

    def verCedula(self):
        return self._cedula

    def asignarNombre(self, n):
        self._nombre = n

    def asignarServicio(self, s):
        self._servicio = s

    def asignarGenero(self, g):
        self._genero = g

    def asignarCedula(self, c):
        self._cedula = c


class Sistema:
    def __init__(self):
        self._lista_pacientes = []
        self._numero_pacientes = len(self._lista_pacientes)

    def ingresarPaciente(self):
        nombre = input("Ingrese el nombre: ")
        cedula = int(input("Ingrese la cédula: "))
        genero = input("Ingrese el género: ")
        servicio = input("Ingrese el servicio: ")

        p = Paciente()
        p.asignarNombre(nombre)
        p.asignarCedula(cedula)
        p.asignarGenero(genero)
        p.asignarServicio(servicio)
        self._lista_pacientes.append(p)

        self._numero_pacientes = len(self._lista_pacientes)

    def verNumeroPacientes(self):
        return self._numero_pacientes

    def verDatosPaciente(self):
        cedula = int(input("Ingrese la cédula a buscar: "))

        for paciente in self._lista_pacientes:
            if cedula == paciente.verCedula():
                print("Nombre: " + paciente.verNombre())
                print("Cédula: " + str(paciente.verCedula()))
                print("Género: " + paciente.verGenero())
                print("Servicio: " + paciente.verServicio())
                break
        else:
            print("Paciente no encontrado.")


mi_sistema = Sistema()

while True:
    opcion = int(input("1. Nuevo paciente - 2. Número de pacientes - 3. Datos paciente - 4. Salir\n"))
    if opcion == 1:
        mi_sistema.ingresarPaciente()
    elif opcion == 2:
        print("Ahora hay: " + str(mi_sistema.verNumeroPacientes()) + " pacientes.")
    elif opcion == 3:
        mi_sistema.verDatosPaciente()
    elif opcion == 4:
        break
    else:
        print("Opción inválida")
