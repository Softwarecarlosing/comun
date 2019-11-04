import config
import hashlib
import app

class Index:
    
    def __init__(self):
        pass
    
    def GET(self):
        if app.session.loggedin is True: # validate if the user is logged
            email = app.session.user
            privilege = app.session.privilege
            picture = app.session.picture
            params = {}
            params['privilege'] = privilege
            params['user'] = email
            params['picture'] = picture
            params['privilege'] = privilege
            if privilege == 4: # admin user
                return self.GET_INDEX(email,params) # call GET_INDEX() function
            elif privilege == -1: # guess user
                raise config.web.seeother('/guess') # rendner guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_INDEX(email,params):
        result = config.model.validar_aspectos_economicos(email) # get aspectos_economicos table list
        id_aspecto_economico = result
        return config.render.index(id_aspecto_economico['id_aspecto_economico'],params)
             # apply HMAC to id_aspecto_economico (primary key)
        
