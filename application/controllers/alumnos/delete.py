import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, email, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(email) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, email, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(email) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(email, **k):

    @staticmethod
    def POST_DELETE(email, **k):
    '''

    def GET(self, email, **k):
        message = None # Error message
        email = config.check_secure_val(str(email)) # HMAC email validate
        result = config.model.get_alumnos(int(email)) # search  email
        result.email = config.make_secure_val(str(result.email)) # apply HMAC for email
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, email, **k):
        form = config.web.input() # get form data
        form['email'] = config.check_secure_val(str(form['email'])) # HMAC email validate
        result = config.model.delete_alumnos(form['email']) # get alumnos data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            email = config.check_secure_val(str(email))  # HMAC user validate
            email = config.check_secure_val(str(email))  # HMAC user validate
            result = config.model.get_alumnos(int(email)) # get email data
            result.email = config.make_secure_val(str(result.email)) # apply HMAC to email
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/alumnos') # render alumnos delete.html 
