class Servicio:
    def __init__(self, nombre, estado, puerto, dependencias=[]):
        self.nombre = nombre
        self.estado = estado
        self.puerto = puerto
        self.dependencias = dependencias
        

    def __str__(self):
        return f"[{self.estado.upper()}] {self.nombre} (puerto {self.puerto})"
    
    def marcar_error(self):
        self.estado = 'error'

    def marcar_afectado(self):
        self.estado = 'afectado'
        
        
if __name__ == "__main__":
    s = Servicio("nginx", "activo", 80, ["mysql", "redis"])
    print(s)
    s.marcar_error()
    print(s)
    s.marcar_afectado()
    print(s)