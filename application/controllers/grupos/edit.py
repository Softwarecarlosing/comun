import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_grupo, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_grupo) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_grupo, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_grupo) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_grupo, **k):

    @staticmethod
    def POST_EDIT(id_grupo, **k):
        
    '''

    def GET(self, id_grupo, **k):
        message = None # Error message
        id_grupo = config.check_secure_val(str(id_grupo)) # HMAC id_grupo validate
        result = config.model.get_grupos(int(id_grupo)) # search for the id_grupo
        result.id_grupo = config.make_secure_val(str(result.id_grupo)) # apply HMAC for id_grupo
        return config.render.edit(result, message) # render grupos edit.html

    def POST(self, id_grupo, **k):
        form = config.web.input()  # get form data
        form['id_grupo'] = config.check_secure_val(str(form['id_grupo'])) # HMAC id_grupo validate
        # edit user with new data
        result = config.model.edit_grupos(
            form['id_grupo'],form['id_programa_educativo'],form['id_periodo'],form['grupo'],form['clave_grupo'],
        )
        if result == None: # Error on udpate data
            id_grupo = config.check_secure_val(str(id_grupo)) # validate HMAC id_grupo
            result = config.model.get_grupos(int(id_grupo)) # search for id_grupo data
            result.id_grupo = config.make_secure_val(str(result.id_grupo)) # apply HMAC to id_grupo
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/grupos') # render grupos index.html
