import config
import hashlib
import app

class Index:
    
    def __init__(self):
        pass
        

    
    def GET(self):
        if app.session.loggedin is True:
            email = app.session.user
            privilege = app.session.privilege
            picture = app.session.picture
            params = {}
            params['user'] = email
            params['privilege'] = privilege
            params['picture'] = picture

            if privilege == 1:# tutor
              return self.GET_INDEX(email,params)
            if privilege ==2: # docente 
              return self.GET_INDEX(email,params)
            if privilege == 3:# alumno
              return self.GET_INDEX(email,params)
            if privilege == 4:# alumno_inscrito
              return self.GET_INDEX(email,params)
            if privilege == 5:# coordinador 
              return self.GET_INDEX(email,params)
       
    @staticmethod
    def GET_INDEX(email,params):
        emai = app.session.user
        #privilege = app.session.privilege
        #params = {}
        #params['user'] = email
        #params['privilege'] = privilege
        #realizar la especificacio antes de de enviarlos como paramentro
        #result = config.model_alumnos.validate_alumno(email) # get alumnos table list
             # apply HMAC to email (primary key)
        email = emai
        result = config.model_alumnos.obtener_alumno(email)
        
        
        return config.render.index(str(result['email']),params) # render alumnos index.html
    
    