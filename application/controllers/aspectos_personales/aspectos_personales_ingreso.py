import config
import hashlib
import app

class AspectosPersonalesIngreso:
    
    def __init__(self):
        pass
    
    def GET(self):
        email = app.session.user
        privilege = app.session.privilege
        email=app.session.user
        busqueda = config.model.validar_aspectos_personales(email)
        if busqueda:
           aspectos_personales = busqueda

           params={}
           params['privilege']= app.session.privilege
           params['user'] = email
           message = None 
           return config.web.seeother('/aspectos_personales')
           #return config.web.seeother('/aspectos_personales')
        if busqueda == None:
           return config.web.seeother('/aspectos_personales/insert')
        
    
    #def POST(self):
        #email=app.session.user
        #busqueda = config.model.validar_aspectos_personales(email)
        #if busqueda:
           #aspectos_personales = busqueda
        #return config.web.seeother('/alumnos/index_alumno')
           #params={}
           #params['privilege']= app.session.privilege
           #params['user'] = email
           #message = None 
           #return config.render.edit(aspectos_personales,message)
        #if busqueda == None:
           #return config.web.seeother('/aspectos_personales/insert')


        #result = config.model.get_aspectos_economicos(email) # get aspectos_economicos table list
        #if result:

             # apply HMAC to id_aspecto_economico (primary key)
        #return config.render.index(result,params) # render aspectos_economicos index.html
