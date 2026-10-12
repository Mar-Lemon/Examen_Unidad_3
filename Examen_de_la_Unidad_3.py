class Planeta:
  # Atributo de clase para el conteo total
  total_planetas = 0

  def __init__(self, nombre, distancia, *caracteristicas, **recursos):
    self.nombre = nombre
    self.distancia = distancia  # Por ejemplo, en millones de kilómetros o años luz
    self.caracteristicas = caracteristicas  # Uso de *args
    self.recursos = recursos  # Uso de **kwargs
    Planeta.total_planetas += 1
    print(f"[+] Planeta '{self.nombre}' registrado exitosamente.")

  def __del__(self):
    Planeta.total_planetas -= 1
    print(f"[-] Planeta '{self.nombre}' eliminado del sistema.")

  @classmethod
  def obtener_conteo_planetas(cls):
    return cls.total_planetas


class NaveEspacial:
  # Atributo de clase para el conteo total
  total_naves = 0

  def __init__(self, nombre, velocidad, *misiones_adicionales, **recursos_nave):
    self.nombre = nombre
    self.velocidad = velocidad  # Velocidad de la nave
    self.destino = None
    self.misiones_adicionales = misiones_adicionales  # Uso de *args
    self.recursos_nave = recursos_nave  # Uso de **kwargs
    NaveEspacial.total_naves += 1
    print(f"[+] Nave espacial '{self.nombre}' registrada exitosamente.")

  def __del__(self):
    NaveEspacial.total_naves -= 1
    print(f"[-] Nave espacial '{self.nombre}' dada de baja.")

  @classmethod
  def obtener_conteo_naves(cls):
    return cls.total_naves

  def asignar_destino(self, planeta):
    self.destino = planeta
    print(f"-> Destino asignado a la nave {self.nombre}: {planeta.nombre}")

  def calcular_tiempo_viaje(self):
    if not self.destino:
      return "Error: La nave no tiene un destino asignado."
    if self.velocidad <= 0:
      return "Error: La velocidad debe ser mayor a 0."
    
    tiempo = self.destino.distancia / self.velocidad
    return tiempo

  def mostrar_informacion(self):
    destino_nombre = self.destino.nombre if self.destino else "Sin destino"
    info = (
        f"\nNave: {self.nombre}\n"
        f"Velocidad: {self.velocidad}\n"
        f"Destino actual: {destino_nombre}\n"
        f"Misiones adicionales (*args): {self.misiones_adicionales}\n"
        f"Recursos (**kwargs): {self.recursos_nave}"
    )
    return info


def menu_interactivo():
  planetas = []
  naves = []

  while True:
    print("\n========================================")
    print("      SIMULADOR DE VIAJES INTERPLANETARIOS")
    print("========================================")
    print("1. Registrar planetas")
    print("2. Registrar naves")
    print("3. Asignar destino")
    print("4. Calcular tiempo de viaje")
    print("5. Mostrar información")
    print("6. Salir")
    
    opcion = input("\nSeleccione una opción (1-6): ").strip()

    if opcion == "1":
      nombre = input("Ingrese el nombre del planeta: ")
      distancia = float(input("Ingrese la distancia (millones de km): "))
      
      # Ejemplo opcional de uso de *args y **kwargs desde consola
      caract_input = input("Ingrese características separadas por coma (*args, opcional): ")
      args = tuple(c.strip() for c in caract_input.split(",")) if caract_input else ()
      
      nuevo_planeta = Planeta(nombre, distancia, *args, tipo="Rocoso")
      planetas.append(nuevo_planeta)

    elif opcion == "2":
      nombre = input("Ingrese el nombre de la nave espacial: ")
      velocidad = float(input("Ingrese la velocidad de la nave: "))
      
      mision_input = input("Ingrese misiones adicionales separadas por coma (*args, opcional): ")
      misiones = tuple(m.strip() for m in mision_input.split(",")) if mision_input else ()
      
      nueva_nave = NaveEspacial(nombre, velocidad, *misiones, combustible="Plasma")
      naves.append(nueva_nave)

    elif opcion == "3":
      if not planetas or not naves:
        print("\n[!] Debe registrar al menos un planeta y una nave primero.")
        continue
      
      print("\nPlanetas disponibles:")
      for i, p in enumerate(planetas):
        print(f"{i}. {p.nombre}")
      p_idx = int(input("Seleccione el número del planeta destino: "))

      print("\nNaves disponibles:")
      for i, n in enumerate(naves):
        print(f"{i}. {n.nombre}")
      n_idx = int(input("Seleccione el número de la nave: "))

      naves[n_idx].asignar_destino(planetas[p_idx])

    elif opcion == "4":
      if not naves:
        print("\n[!] No hay naves registradas.")
        continue
      
      print("\nNaves disponibles:")
      for i, n in enumerate(naves):
        print(f"{i}. {n.nombre}")
      n_idx = int(input("Seleccione el número de la nave a calcular: "))
      
      tiempo = naves[n_idx].calcular_tiempo_viaje()
      print(f"\n[Resultado] El tiempo estimado de viaje es: {tiempo} unidades de tiempo.")

    elif opcion == "5":
      print(f"\n--- ESTADÍSTICAS GENERALES ---")
      print(f"Total de Planetas registrados: {Planeta.obtener_conteo_planetas()}")
      print(f"Total de Naves registradas: {NaveEspacial.obtener_conteo_naves()}")
      
      print("\n--- DETALLES DE NAVES ---")
      if not naves:
        print("No hay naves registradas.")
      for n in naves:
        print(n.mostrar_informacion())

      print("\n--- DETALLES DE PLANETAS ---")
      if not planetas:
        print("No hay planetas registrados.")
      for p in planetas:
        print(f"Planeta: {p.nombre} | Distancia: {p.distancia} | Características: {p.caracteristicas}")

    elif opcion == "6":
      print("\nSaliendo del simulador de viajes interplanetarios. ¡Buen viaje!")
      break
    else:
      print("\n[!] Opción inválida. Por favor, seleccione un número entre 1 y 6.")


if __name__ == "__main__":
  menu_interactivo()