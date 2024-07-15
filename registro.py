import random
import csv

from os import system
import os

ruta = r'D:\WorkSpace\python\proyectoClinica\csv\pacientes.csv'

lista_pacientes = []
head = ["Id", "Nombre", "Apellido", "Edad", "Direccion", "Comuna"]


def registro():
    while True:
        os.system('cls')
        print('-----------------------------------------------------')
        print('\tBienvenido al sistema de registro de pacientes.')
        print('----------------------------------------------------')
        opcion = input('Desea registrar un nuevo paciente? (s/n): ').strip()
        if opcion.lower() == 'n':
            print('Gracias por usar nuestra clinica Digital. Hasta luego.')
            break
        elif opcion.lower() == 's':
            os.system('cls')
            try:
                print('\tRegistro de pacientes\n')
                nombrePaciente = input('Ingrese el nombre del paciente: ')
                if not nombrePaciente:
                    print('El nombre del paciente es obligatorio.')
                    continue
                apellidoPaciente = input('Ingrese el apellido del paciente: ')
                if not apellidoPaciente:
                    print('El apellido del paciente es obligatorio.')
                    continue
                edadPaciente = int(input('Ingrese la edad del paciente: '))
                if not 0 < edadPaciente < 110:
                    print('La edad del paciente debe estar entre 1 y 109 años.')
                    continue
                direccionPaciente = input(
                    'Ingrese la dirección del paciente: ')
                if not direccionPaciente:
                    print('La dirección del paciente es obligatoria.')
                    continue
                comunapaciente = input('Ingrese la comuna del paciente: ')
                if not comunapaciente:
                    print('La comuna del paciente es obligatoria.')
                    continue

                diccPaciente = {
                    "Id": random.randint(1, 1000000),
                    "Nombre": nombrePaciente,
                    "Apellido": apellidoPaciente,
                    "Edad": edadPaciente,
                    "Direccion": direccionPaciente,
                    "Comuna": comunapaciente
                }
                lista_pacientes.append(diccPaciente)
                print('--------------------------------')
                print('Paciente registrado exitosamente.')
                print('--------------------------------')

            except ValueError as e:
                print('Error:', str(e))
                continue

            opcion = input('¿Desea registrar otro paciente? (s/n): ')
            if opcion.lower() != "s":
                print()
                print('Gracias por usar nuestra clinica Digital. Hasta luego.')
                break
            else:
                print('--------------------------------')
                print('opcion no valida. Presione enter para continuar.')


def grabar_csv():
    directorty = os.path.dirname(ruta)
    rutaRelativa = os.path.relpath(ruta, start=os.getcwd())

    if not os.path.exists(directorty):
        os.makedirs(directorty)
        print('Creando directorio para guardar los datos...')
        print('...')
        print('Directorio creado exitosamente.')

    with open(ruta, 'a', newline='') as record_csv:
        writer = csv.DictWriter(record_csv, fieldnames=head)
        writer.writeheader()
        writer.writerows(lista_pacientes)
        print(f'Los datos se han guardado correctamente en el directorio: {
              rutaRelativa}.')
        enter = input('Presione enter para continuar...')
        os.system('cls')


def listar_pacientes():
    print('-----------------------------------------------------')
    ruta = r'D:\WorkSpace\python\proyectoClinica\csv\pacientes.csv'
    with open(ruta, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile, dialect='excel',
                                delimiter=',', fieldnames=head)
        print('\tListado de pacientes registrados.')

        pacientes = [(row["Id"], row["Nombre"], row["Apellido"], row["Edad"],
                      row["Direccion"], row["Comuna"]) for row in reader]
    print('-----------------------------------------------------')
    for paciente in pacientes:
        print(f'{paciente[0]}, {paciente[1]}, {paciente[2]}, {
            paciente[3]}, {paciente[4]}, {paciente[5]}\n')
    print('-----------------------------------------------------')
    enter = input('Presione enter para continuar...')
    os.system('cls')


def menu():
    print('1. Registro Pacientes')
    print('2. Grabar datos en CSV')
    print('3. Listar pacientes')
    # print('')
    print('6. Salir')
    op = int(input('Seleccione una opción: '))
    if op == 1:
        registro()
    if op == 2:
        grabar_csv()
    if op == 3:
        listar_pacientes()
    if op == 6:
        print('Gracias por usar nuestra clinica Digital. Hasta luego.')
        os.system('cls')
        enter = input('Presione enter para continuar...')
        exit()


if __name__ == '__main__':
    while True:
        menu()
