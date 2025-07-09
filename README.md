# Proyecto Urban Routes 
Definir localizadores y metodos para la clase UrbanRoutesPage y las pruebas automatizadas en la clase TestUrbanRoutes.

Las pruebas automatizadas que cubran el proceso completo de pedir un taxi.
Las pruebas deben cubrir estas acciones:

- Configurar la dirección. 
- Seleccionar la tarifa Comfort. 
- Rellenar el número de teléfono. 
- Agregar una tarjeta de crédito.

Ademas de que el usuario pueda elegir preferencias en el transcurso de la ruta.

## Cohortes lista  
"numero": 1, "Field from - to",
"numero": 2, "botones Pedir taxi - Comfort",
"numero": 3, "Numero de telefono, agregar tarjeta, boton toggle, boton de incremento",
"numero": 4, "Reservar viaje"

### Instrucciones
Antes de que ejecutar las pruebas debe ser actualizado urban_routes_url
#### Ejecucion de pruebas

- @ClassMethod para probar cierta funciones de Urban Routes
- Prueba de funcionalidad de direcciones Desde y Hasta: Localizadores definidos en data.py
- Prueba de funcionalidad de seleccion de tarifa 'Comfort': boton "Pedir un taxi"
- Prueba de funcionalidad de ingreso de numero de telefono: Localizador definido en data.py
- Prueba de funcionalidad de ingreso de metodo de pago (tarjeta de credito): Localizador definido en data.py
- Prueba de funcionalidad de preferencias durante el viaje: botones toggle e increment

##### Tecnologias utilizadas
- Python
- JSON
- Selenium.WebDriver
- WebDriverWait
- expected_conditions