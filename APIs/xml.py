import xml.etree.ElementTree as ET

class Persona:
    def __init__(self, nombre: str, apellido: str, dni: str):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni

    @classmethod
    def from_xml(cls, xml_str: str):
        root = ET.fromstring(xml_str)
        nombre = root.find('nombre').text
        apellido = root.find('apellido').text
        dni = root.find('dni').text
        return cls(nombre, apellido, dni)

    def to_xml(self) -> str:
        root = ET.Element('persona')
        nombre = ET.SubElement(root, 'nombre')
        nombre.text = self.__nombre
        apellido = ET.SubElement(root, 'apellido')
        apellido.text = self.__apellido
        dni = ET.SubElement(root, 'dni')
        dni.text = self.__dni
        return ET.tostring(root, encoding='unicode')

    def __str__(self):
        return f'Persona(nombre={self.__nombre}, apellido={self.__apellido}, dni={self.__dni})'

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia de Persona
    persona = Persona("Juan", "Pérez", "12345678A")
    
    # Serializar a XML
    xml_data = persona.to_xml()
    print("Datos en formato XML:", xml_data)
    
    # Deserializar desde XML
    persona_deserializada = Persona.from_xml(xml_data)
    print("Persona deserializada:", persona_deserializada)