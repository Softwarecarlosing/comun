import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_grupo, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_grupo) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_grupo, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_grupo) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_grupo, **k):

    @staticmethod
    def POST_DELETE(id_grupo, **k):
    '''

    def GET(self, id_grupo, **k):
        message = None # Error message
        id_grupo = config.check_secure_val(str(id_grupo)) # HMAC id_grupo validate
        result = config.model.get_grupos(int(id_grupo)) # search  id_grupo
        result.id_grupo = config.make_secure_val(str(result.id_grupo)) # apply HMAC for id_grupo
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_grupo, **k):
        form = config.web.input() # get form data
        form['id_grupo'] = config.check_secure_val(str(form['id_grupo'])) # HMAC id_grupo validate
        result = config.model.delete_grupos(form['id_grupo']) # get grupos data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_grupo = config.check_secure_val(str(id_grupo))  # HMAC user validate
            id_grupo = config.check_secure_val(str(id_grupo))  # HMAC user validate
            result = config.model.get_grupos(int(id_grupo)) # get id_grupo data
            result.id_grupo = config.make_secure_val(str(result.id_grupo)) # apply HMAC to id_grupo
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/grupos') # render grupos delete.html 
