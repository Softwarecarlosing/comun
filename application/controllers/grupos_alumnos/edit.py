import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_grupos_alumnos, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_grupos_alumnos) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_grupos_alumnos, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_grupos_alumnos) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_grupos_alumnos, **k):

    @staticmethod
    def POST_EDIT(id_grupos_alumnos, **k):
        
    '''

    def GET(self, id_grupos_alumnos, **k):
        message = None # Error message
        id_grupos_alumnos = config.check_secure_val(str(id_grupos_alumnos)) # HMAC id_grupos_alumnos validate
        result = config.model.get_grupos_alumnos(int(id_grupos_alumnos)) # search for the id_grupos_alumnos
        result.id_grupos_alumnos = config.make_secure_val(str(result.id_grupos_alumnos)) # apply HMAC for id_grupos_alumnos
        return config.render.edit(result, message) # render grupos_alumnos edit.html

    def POST(self, id_grupos_alumnos, **k):
        form = config.web.input()  # get form data
        form['id_grupos_alumnos'] = config.check_secure_val(str(form['id_grupos_alumnos'])) # HMAC id_grupos_alumnos validate
        # edit user with new data
        result = config.model.edit_grupos_alumnos(
            form['id_grupos_alumnos'],form['id_grupo'],form['email'],
        )
        if result == None: # Error on udpate data
            id_grupos_alumnos = config.check_secure_val(str(id_grupos_alumnos)) # validate HMAC id_grupos_alumnos
            result = config.model.get_grupos_alumnos(int(id_grupos_alumnos)) # search for id_grupos_alumnos data
            result.id_grupos_alumnos = config.make_secure_val(str(result.id_grupos_alumnos)) # apply HMAC to id_grupos_alumnos
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/grupos_alumnos') # render grupos_alumnos index.html
