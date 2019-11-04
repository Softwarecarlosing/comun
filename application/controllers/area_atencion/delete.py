import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_area_atencion, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_area_atencion) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_area_atencion, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_area_atencion) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_area_atencion, **k):

    @staticmethod
    def POST_DELETE(id_area_atencion, **k):
    '''

    def GET(self, id_area_atencion, **k):
        message = None # Error message
        id_area_atencion = config.check_secure_val(str(id_area_atencion)) # HMAC id_area_atencion validate
        result = config.model.get_area_atencion(int(id_area_atencion)) # search  id_area_atencion
        result.id_area_atencion = config.make_secure_val(str(result.id_area_atencion)) # apply HMAC for id_area_atencion
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_area_atencion, **k):
        form = config.web.input() # get form data
        form['id_area_atencion'] = config.check_secure_val(str(form['id_area_atencion'])) # HMAC id_area_atencion validate
        result = config.model.delete_area_atencion(form['id_area_atencion']) # get area_atencion data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_area_atencion = config.check_secure_val(str(id_area_atencion))  # HMAC user validate
            id_area_atencion = config.check_secure_val(str(id_area_atencion))  # HMAC user validate
            result = config.model.get_area_atencion(int(id_area_atencion)) # get id_area_atencion data
            result.id_area_atencion = config.make_secure_val(str(result.id_area_atencion)) # apply HMAC to id_area_atencion
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/area_atencion') # render area_atencion delete.html 
