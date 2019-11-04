import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_historial_medico, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_historial_medico) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_historial_medico, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_historial_medico) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_historial_medico, **k):

    @staticmethod
    def POST_DELETE(id_historial_medico, **k):
    '''

    def GET(self, id_historial_medico, **k):
        message = None # Error message
        id_historial_medico = config.check_secure_val(str(id_historial_medico)) # HMAC id_historial_medico validate
        result = config.model.get_historiales_medicos(int(id_historial_medico)) # search  id_historial_medico
        result.id_historial_medico = config.make_secure_val(str(result.id_historial_medico)) # apply HMAC for id_historial_medico
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_historial_medico, **k):
        form = config.web.input() # get form data
        form['id_historial_medico'] = config.check_secure_val(str(form['id_historial_medico'])) # HMAC id_historial_medico validate
        result = config.model.delete_historiales_medicos(form['id_historial_medico']) # get historiales_medicos data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_historial_medico = config.check_secure_val(str(id_historial_medico))  # HMAC user validate
            id_historial_medico = config.check_secure_val(str(id_historial_medico))  # HMAC user validate
            result = config.model.get_historiales_medicos(int(id_historial_medico)) # get id_historial_medico data
            result.id_historial_medico = config.make_secure_val(str(result.id_historial_medico)) # apply HMAC to id_historial_medico
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/historiales_medicos') # render historiales_medicos delete.html 
