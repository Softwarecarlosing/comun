import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    
    def GET(self, id_aspecto_personal, message=None):
        if app.session.loggedin is True: # validate if the user is logged
            session_user = app.session.user
            session_privilege = app.session.privilege # get the session_privilege
            message=None
            params = {}
            params['user'] = session_user
            params['privilege'] = session_privilege
            if session_privilege == 4: # admin user
                return self.GET_EDIT(id_aspecto_personal,params,message) # call GET_EDIT function
            elif session_privilege == 0: # guess user
                return self.GET_EDIT(id_aspecto_personal,params,message) # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_aspecto_personal, message=None):
        if app.session.loggedin is True: # validate if the user is logged
            session_user = app.session.user
            session_privilege = app.session.privilege # get the session_privilege
            message = None
            params = {}
            params['user'] = session_user
            params['privilege'] = session_privilege
            if session_privilege == 4: # admin user
                return self.POST_EDIT(id_aspecto_personal,params,message) # call POST_EDIT function
            elif session_privilege == 0: # guess user
                return self.POST_EDIT(id_aspecto_personal,params,message) # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_aspecto_personal,params, message):
        message = None # Error message
        #id_aspecto_personal = config.check_secure_val(str(id_aspecto_personal)) # HMAC id_aspecto_personal validate
        result = config.model.get_aspectos_personales(id_aspecto_personal) # search for the id_aspecto_personal
         # apply HMAC for id_aspecto_personal
        return config.render.edit(result,message) # render aspectos_personales edit.html

    @staticmethod
    def POST_EDIT(id_aspecto_personal,params, message):
        form = config.web.input()  # get form data
        #form['id_aspecto_personal'] = config.check_secure_val(str(form['id_aspecto_personal'])) # HMAC id_aspecto_personal validate
        # edit user with new data
        result = config.model.edit_aspectos_personales(
            form['id_aspecto_personal'],
            form['email'],
            form['estado_civil'],
            form['numero_hijos'],
            form['quien_los_cuida'],
            form['no_integrantes_familia'],
            form['comunicacion_familiar'],
            form['responsable'],
            form['respetuosa'],
            form['trabajo_equipo'],
        )
        #if result == None: # Error on udpate data
            #id_aspecto_personal = config.check_secure_val(str(id_aspecto_personal)) # validate HMAC id_aspecto_personal
            #result = config.model.get_aspectos_personales(int(id_aspecto_personal)) # search for id_aspecto_personal data
            #result.id_aspecto_personal = config.make_secure_val(str(result.id_aspecto_personal)) # apply HMAC to id_aspecto_personal
            #message = "Error al editar el registro" # Error message
            #return config.render.edit(result, message) # render edit.html again
        #else: # update user data succefully
            #raise config.web.seeother('/aspectos_personales') # render aspectos_personales index.html
        raise config.web.seeother('/alumnos/index_alumno')
