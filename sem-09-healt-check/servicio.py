class Servicio:
    def __init__(self, nombre, estado, puerto, dependencias=[]):
        self.nombre = nombre
        self.estado = estado
        self.puerto = puerto
        self.dependencias = dependencias
        

    def __str__(self):
        return f"[{self.estado.upper()}] {self.nombre} (puerto {self.puerto})"
        
        
if __name__ == "__main__":
    s = Servicio("nginx", "activo", 80, ["mysql", "redis"])
    print(s)
    print(s.nombre)
    print(s.estado)