import csv
from datetime import date

asignaturas = {
    "PSP": 100,
    "Empresa": 80,
    "Multimedia": 120,
    "SGE": 90,
    "Interfaces": 110,
    "Proyecto": 130,
    "Acceso Datos": 70
}

hoy = date.today()
print("***********************************************************")
print("1 - Consultar faltas de una asignatura")
print("2 - Registrar falta de una asignatura")
print("3 - Consultar registro completo de faltas de una asignatura")
print("4 - Salir")
print("***********************************************************")


opcion = input("Selecciona una opción: ")

if opcion == "1":
    asignatura = input(
        "Selecciona la asignatura: \nPSP\nEmpresa\nMultimedia\nSGE\nInterfaces\nProyecto\nAcceso Datos: \n")
    total_horas_faltadas = 0
    with open("faltas.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) >= 1 and row[1] == asignatura:
                total_horas_faltadas += int(row[2])
    if total_horas_faltadas == 0:
        print("No hay faltas registradas en esta asignatura")
    else:
        porcentaje_faltas = total_horas_faltadas / \
            asignaturas[asignatura] * 100
        print(f"Faltas acumuladas en {asignatura}: {porcentaje_faltas:.2f}%")

elif opcion == "2":
    asignatura = input(
        "Selecciona la asignatura: \nPSP/Empresa/Multimedia/SGE/Interfaces/Proyecto/Acceso Datos: ")
    horas_faltadas = int(input("Indica el número de horas que has faltado: "))
    total_horas_faltadas = 0
    with open("faltas.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) >= 1 and row[1] == asignatura:
                total_horas_faltadas += int(row[2])
    porcentaje_faltas = (total_horas_faltadas +
                         horas_faltadas) / asignaturas[asignatura] * 100
    with open("faltas.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([hoy, asignatura, horas_faltadas, porcentaje_faltas])

elif opcion == "3":
  asignatura = input(
      "Selecciona la asignatura: \nPSP/Empresa/Multimedia/SGE/Interfaces/Proyecto/Acceso Datos: ")

  def obtener_registros_asignatura(asignatura):
    registros = []
    with open("faltas.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) >= 1 and row[1] == asignatura:
                registros.append(row)
    return registros
  registros = obtener_registros_asignatura(asignatura)

  for registro in registros:
    fecha = registro[0]
    asignatura = registro[1]
    horas_faltadas = registro[2]
    porcentaje_faltas = registro[3]
    print(f"{fecha},{asignatura},{horas_faltadas},{porcentaje_faltas}%")


elif opcion == "4":
    print("Hasta luego")

else:
    print("Opción no válida")
