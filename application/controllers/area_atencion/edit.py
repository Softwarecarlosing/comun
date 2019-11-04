import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_area_atencion, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_area_atencion) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_area_atencion, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_area_atencion) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_area_atencion, **k):

    @staticmethod
    def POST_EDIT(id_area_atencion, **k):
        
    '''

    def GET(self, id_area_atencion, **k):
        message = None # Error message
        id_area_atencion = config.check_secure_val(str(id_area_atencion)) # HMAC id_area_atencion validate
        result = config.model.get_area_atencion(int(id_area_atencion)) # search for the id_area_atencion
        result.id_area_atencion = config.make_secure_val(str(result.id_area_atencion)) # apply HMAC for id_area_atencion
        return config.render.edit(result, message) # render area_atencion edit.html

    def POST(self, id_area_atencion, **k):
        form = config.web.input()  # get form data
        form['id_area_atencion'] = config.check_secure_val(str(form['id_area_atencion'])) # HMAC id_area_atencion validate
        # edit user with new data
        result = config.model.edit_area_atencion(
            form['id_area_atencion'],form['area'],form['descripcion'],
        )
        if result == None: # Error on udpate data
            id_area_atencion = config.check_secure_val(str(id_area_atencion)) # validate HMAC id_area_atencion
            result = config.model.get_area_atencion(int(id_area_atencion)) # search for id_area_atencion data
            result.id_area_atencion = config.make_secure_val(str(result.id_area_atencion)) # apply HMAC to id_area_atencion
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/area_atencion') # render area_atencion index.html
