import config
import hashlib
import app


class View:

    def __init__(self):
        pass

    
    def GET(self, id_grupo):
        if app.session.loggedin is True: # validate if the user is logged
            session_user = app.session.user
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_VIEW(id_grupo) # call GET_VIEW() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(id_grupo):

    #def GET(self, id_grupo):
        id_grupo = config.check_secure_val(str(id_grupo)) # HMAC id_grupo validate
        result = config.model.get_grupos(id_grupo) # search for the id_grupo data
        return config.render.view(result) # render view.html with id_grupo data
