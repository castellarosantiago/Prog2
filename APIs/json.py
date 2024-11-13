import json 
##convertir diccionario a JSON
pesrona = {"nombre":"juan", "edad":30, "ciudad":"bahia"}
json_data_str= json.dumps(pesrona)
print(json_data_str)
##convertir JSON a diccionario
persona_dicc = json.loads(json_data_str)
print(persona_dicc)["nombre"]