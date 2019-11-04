import config
import hashlib
import app

class AspectosEconomicosIngreso:
    
  
    def __init__(self):
        pass
   ##### validacion de existencia y raise a direccion de ingreso a formularios 
    def GET(self):
        email = app.session.user
        privilege = app.session.privilege
        email=app.session.user
        busqueda = config.model.validar_aspectos_economicos(email)
        if busqueda:
           aspectos_economicos = busqueda

           params={}
           params['privilege']= app.session.privilege
           params['user'] = email
           message = None 
           return config.web.seeother('/aspectos_economicos')
        if busqueda == None:
           return config.web.seeother('/aspectos_economicos/insert')
