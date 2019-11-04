import config
import hashlib
import app


class View:

    def __init__(self):
        pass

    
    def GET(self, email):
        if app.session.loggedin is True: # validate if the user is logged
            user = app.session.user
            privilege = app.session.privilege # get the session_privilege
            if privilege == 4: # admin user
                return self.GET_VIEW(email) # call GET_VIEW() function
            elif privilege == 0: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(email):
    
        email = app.session.user # HMAC email validate
        result = config.model_alumnos.obtener_alumno(email) # search for the email data
        return config.render.view(result) # render view.html with email data
