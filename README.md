# Monitoring Views Workshop
Integrantes Grupo 1 Pareja 2:
Daniel Bernal - 
Javier Cerino - j.cerino - 202020873

# Consultar la lista de todas las medidas (measurements) 
Path: “/measurements”
Method: “GET”
# Recursos Fotográficos Pruebas PostMan:
![image](https://user-images.githubusercontent.com/77985120/187037892-ad12babd-7b62-4056-b884-b3d12f115fe0.png)

# Consultar una medida dado su identificador
Path: “/measurements/?id=<id>”
Method: “GET”
# Recursos Fotográficos Pruebas PostMan:
![image](https://user-images.githubusercontent.com/77985120/187037944-88437c7f-06f2-4799-84e1-ee08c7c7bfa7.png)

# Crear una medida
Path: “/measurements”
Method: “POST”
Body: Measurement Model
# Recursos Fotográficos Pruebas PostMan:
![image](https://user-images.githubusercontent.com/77985120/187038981-73d4ee76-3253-4012-9b63-ae7de5e88881.png)

# Cambiar una medida dado su identificador
Path: “/measurements/<id>” o “/measurements/?id=<id>”
Method: “PUT” o "PATCH"
Body: Measurement Model
# Recursos Fotográficos Pruebas PostMan:
![image](https://user-images.githubusercontent.com/77985120/187039074-d431de36-4b1c-430e-9b50-8639ca15b429.png)

# Borrar una medida dado su identificador
Path: “/measurements/<id>” o “/measurements/?id=<id>”
Method: “DELETE”
#  Recursos Fotográficos Pruebas PostMan:
![image](https://user-images.githubusercontent.com/77985120/187039093-34ee1a39-696f-482d-9796-9f776a055db6.png)

