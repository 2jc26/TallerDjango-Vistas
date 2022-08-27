# Monitoring Views Workshop
Integrantes Grupo 1 Pareja 2:
Daniel Bernal - 
Javier Cerino - j.cerino - 202020873

•	Consultar la lista de todas las medidas (measurements) 
  o	Path: “/measurements”
  o	Method: “GET”
# Recursos Fotográficos Pruebas PostMan:
![image](https://user-images.githubusercontent.com/77985120/187037892-ad12babd-7b62-4056-b884-b3d12f115fe0.png)

•	Consultar una medida dado su identificador
o	Path: “/measurements/?id=<id>”
o	Method: “GET”
# Recursos Fotográficos Pruebas PostMan:
![image](https://user-images.githubusercontent.com/77985120/187037944-88437c7f-06f2-4799-84e1-ee08c7c7bfa7.png)

•	Crear una medida
o	Path: “/measurements”
o	Method: “POST”
o	Body: Measurement Model
# Recursos Fotográficos Pruebas PostMan:

•	  Cambiar una medida dado su identificador
o	Path: “/measurements/<id>” o “/measurements/?id=<id>”
o	Method: “PUT” o "PATCH"
o	Body: Measurement Model
•	Borrar una medida dado su identificador
o	Path: “/measurements/<id>” o “/measurements/?id=<id>”
o	Method: “DELETE”
