import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    
    def GET(self, id_aspecto_economico, message=None):
        if app.session.loggedin is True: # validate if the user is logged
            session_user = app.session.user
            session_privilege = app.session.privilege # get the session_privilege
            params = {}
            params['user'] = session_user
            params['privilege'] = session_privilege
            if session_privilege == 4: # admin user
                return self.GET_EDIT(id_aspecto_economico,params,message) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                return self.GET_EDIT(id_aspecto_economico,params,message) # call GET_EDIT function
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_aspecto_economico, message=None):
        if app.session.loggedin is True: # validate if the user is logged
            session_user = app.session.user
            session_privilege = app.session.privilege # get the session_privilege
            params = {}
            params['user'] = session_user
            params['privilege'] = session_privilege
            if session_privilege == 4: # admin user
                return self.POST_EDIT(id_aspecto_economico,params,message) # call POST_EDIT function
            elif session_privilege == 0: # guess user
                return self.POST_EDIT(id_aspecto_economico,params,message)
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    
    

    @staticmethod
    def GET_EDIT(id_aspecto_economico, params,message):

        message = None # Error message
        # HMAC id_aspecto_economico validate
        result = config.model.get_aspectos_economicos(id_aspecto_economico)# search for the id_aspecto_economico
         # apply HMAC for id_aspecto_economico
        return config.render.edit(result,params,message) # render aspectos_economicos edit.html



    @staticmethod
    def POST_EDIT(id_aspecto_economico, params,message):
        
        form = config.web.input()  # get form data
        
        # edit user with new data
        result = config.model.edit_aspectos_economicos(
            form['id_aspecto_economico'],
            form['email'],
            form['beca'],
            form['nombre_beca'],
            form['depende_economicamente'],
            form['tiene_computadora'],
            form['tiene_telefono'],
            form['trabaja'],
            form['empresa'],
            form['jefe_inmediato'],
            form['telefono_trabajo'],
            form['email_trabajo'],
            form['actividad'],
            form['jornada_laboral'],
            form['calle'],
            form['colonia'],
            form['cp'],
            form['no_exterior'],
            form['no_interior'],
            form['municipio'],
            form['referencias'],
        )
        
        raise config.web.seeother('/alumnos/index_alumno') # render alumnos index.html
            
