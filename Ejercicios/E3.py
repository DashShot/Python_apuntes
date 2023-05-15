def run_timing():
    times = []
    while True:
        user_input = input("Ingrese el tiempo (minutos) para correr 10 km (deje en blanco para terminar): ")
        if user_input == "":    #   Entrada Vacía
            break
        try:
            time = float(user_input)
            times.append(time)
        except ValueError:
            print("Ingrese un número válido.")

    if times:
        average_time = sum(times) / len(times)
        num_races = len(times)
        print(f"Tiempo promedio: {average_time} minutos")
        print(f"Número de carreras: {num_races}")
    else:
        print("No se ingresaron tiempos de carrera.")


run_timing()
