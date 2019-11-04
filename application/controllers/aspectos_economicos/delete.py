import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_aspecto_economico, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_aspecto_economico) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_aspecto_economico, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_aspecto_economico) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_aspecto_economico, **k):

    @staticmethod
    def POST_DELETE(id_aspecto_economico, **k):
    '''

    def GET(self, id_aspecto_economico, **k):
        message = None # Error message
        id_aspecto_economico = config.check_secure_val(str(id_aspecto_economico)) # HMAC id_aspecto_economico validate
        result = config.model.get_aspectos_economicos(int(id_aspecto_economico)) # search  id_aspecto_economico
        result.id_aspecto_economico = config.make_secure_val(str(result.id_aspecto_economico)) # apply HMAC for id_aspecto_economico
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_aspecto_economico, **k):
        form = config.web.input() # get form data
        form['id_aspecto_economico'] = config.check_secure_val(str(form['id_aspecto_economico'])) # HMAC id_aspecto_economico validate
        result = config.model.delete_aspectos_economicos(form['id_aspecto_economico']) # get aspectos_economicos data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_aspecto_economico = config.check_secure_val(str(id_aspecto_economico))  # HMAC user validate
            id_aspecto_economico = config.check_secure_val(str(id_aspecto_economico))  # HMAC user validate
            result = config.model.get_aspectos_economicos(int(id_aspecto_economico)) # get id_aspecto_economico data
            result.id_aspecto_economico = config.make_secure_val(str(result.id_aspecto_economico)) # apply HMAC to id_aspecto_economico
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/aspectos_economicos') # render aspectos_economicos delete.html 
