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
    
    def simular_falla(self, servicios):
        self.marcar_error()
        for servicio in servicios:
            if self.nombre in servicio.dependencias:
                servicio.marcar_afectado()
            
            
                
if __name__ == "__main__":
    nginx  = Servicio("nginx", "activo", 80,   ["mysql", "redis"])
    mysql  = Servicio("mysql", "activo", 3306, [])
    redis  = Servicio("redis", "activo", 6379, [])
    api    = Servicio("api",   "activo", 8080, ["nginx", "mysql"])

    servicios = [nginx, mysql, redis, api]

    print("Antes:")
    for s in servicios:
        print(s)

    mysql.simular_falla(servicios)

    print("\nDespués de falla en mysql:")
    for s in servicios:
        print(s)