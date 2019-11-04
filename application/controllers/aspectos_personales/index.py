import config
import hashlib
import app

class Index:
    
    def __init__(self):
        pass
    
    def GET(self):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            
            email = app.session.user
            privilege = app.session.privilege
            picture = app.session.picture
            params = {}
            params['privilege'] = privilege
            params['user'] = email
            params['picture'] = picture
            if privilege == 4: # admin user
                return self.GET_INDEX(params) # call GET_INDEX() function
            elif privilege == 1: # guess user
                raise config.web.seeother('/guess') # rendner guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_INDEX(params):
        email = app.session.user
        privilege = app.session.user
        resul = config.model.validar_aspectos_personales(email) # get aspectos_personales table list
        result = resul
             
        return config.render.index(result['id_aspecto_personal'],params) # render aspectos_personales index.html
