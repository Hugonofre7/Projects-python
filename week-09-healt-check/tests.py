# test_servicio.py
from servicio import Servicio

def test_crear_servicio():
    s = Servicio("nginx", "activo", 80, ["mysql"])
    assert s.nombre == "nginx"
    assert s.estado == "activo"
    assert s.puerto == 80
    assert s.dependencias == ["mysql"]
    
def test_marcar_error():
    s = Servicio("nginx", "activo", 80, ["mysql"])
    s.marcar_error()
    assert s.estado == "error"

def test_simular_falla():
    #Arrange
    s = Servicio("nginx", "activo", 80, ["mysql"])
    mysql = Servicio("mysql", "activo", 3306, [])
    servicios = [s, mysql]
    
    #Act
    mysql.simular_falla(servicios)
    
    #Assert
    assert mysql.estado == "error"
    assert s.estado == "afectado"
    
if __name__ == "__main__":
    test_crear_servicio()
    test_marcar_error()
    test_simular_falla()
    print("Todos los tests pasaron!")
