import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_aspecto_personal, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_aspecto_personal) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_aspecto_personal, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_aspecto_personal) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_aspecto_personal, **k):

    @staticmethod
    def POST_DELETE(id_aspecto_personal, **k):
    '''

    def GET(self, id_aspecto_personal, **k):
        message = None # Error message
        id_aspecto_personal = config.check_secure_val(str(id_aspecto_personal)) # HMAC id_aspecto_personal validate
        result = config.model.get_aspectos_personales(int(id_aspecto_personal)) # search  id_aspecto_personal
        result.id_aspecto_personal = config.make_secure_val(str(result.id_aspecto_personal)) # apply HMAC for id_aspecto_personal
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_aspecto_personal, **k):
        form = config.web.input() # get form data
        form['id_aspecto_personal'] = config.check_secure_val(str(form['id_aspecto_personal'])) # HMAC id_aspecto_personal validate
        result = config.model.delete_aspectos_personales(form['id_aspecto_personal']) # get aspectos_personales data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_aspecto_personal = config.check_secure_val(str(id_aspecto_personal))  # HMAC user validate
            id_aspecto_personal = config.check_secure_val(str(id_aspecto_personal))  # HMAC user validate
            result = config.model.get_aspectos_personales(int(id_aspecto_personal)) # get id_aspecto_personal data
            result.id_aspecto_personal = config.make_secure_val(str(result.id_aspecto_personal)) # apply HMAC to id_aspecto_personal
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/aspectos_personales') # render aspectos_personales delete.html 
