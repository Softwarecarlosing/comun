import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    
    def GET(self, email, message=None):
        if app.session.loggedin is True: # validate if the user is logged
            email = app.session.user
            privilege = app.session.privilege # get the session_privilege
            picture = app.session.picture
            params = {}
            params['email'] = email 
            params['privilege'] = privilege
            if privilege == 1:
                return self.POST_EDIT(email, params, message)
            if privilege == 4: # alumno_inscrito
                return self.GET_EDIT(email, params, message) # call GET_EDIT function
            # guess user
        else:
            raise config.web.seeother('/guess')        

    def POST(self, email, message=None):
        if app.session.loggedin is True: # validate if the user is logged
            email = app.session.user
            privilege = app.session.privilege # get the session_privilege
            params = {}
            params['email'] = email
            params['privilege'] = privilege
            if privilege == 1: # alumno_iscrito
                return self.POST_EDIT(email, params, message) # call POST_EDIT function
            if privilege == 4:
                return self.POST_EDIT(email,params, message)
        else: # the user dont have logged
            raise config.web.seeother('/guess') # render login.html
    
    @staticmethod
    def GET_EDIT(email, params, message):
        message = None # Error message
        #email = config.check_secure_val(str(email)) # HMAC email validate
        email = app.session.user
        result = config.model_alumnos.get_alumnos(email) # search for the email
        #result.email = config.make_secure_val(str(result.email)) # apply HMAC for email
        return config.render.edit(result, params, message) # render alumnos edit.html




    @staticmethod
    def POST_EDIT(email, params, message):
        form = config.web.input()  # get form data
        #form['email'] = config.check_secure_val(str(form['email'])) # HMAC email validate
        # edit user with new data
        result = config.model_alumnos.edit_alumnos(
            form['email'],
            form['id_grupo'],
            form['matricula'],
            form['fecha_alta'],
            form['nombre'],
            form['ap_paterno'],
            form['ap_materno'],
            form['fecha_nacimiento'],
            form['curp'],
            form['cuatrimestre'],
            form['telefono_celular'],
            form['telefono_casa'],
            form['email_institucional'],
            form['email_personal'],
            form['calle'],
            form['colonia'],
            form['cp'],
            form['no_exterior'],
            form['no_interior'],
            form['municipio'],
            form['referencias'],
            form['idioma_principal'],
            form['segundo_idioma'],
        )
        #if result == None: # Error on udpate data
            #email = config.check_secure_val(str(email)) # validate HMAC email
            #result = config.model_alumnos.get_alumnos(str(email)) # search for email data
            #result.email = config.make_secure_val(str(result.email)) # apply HMAC to email
            #message = "Error al editar el registro" # Error message
            #return config.render.edit(result, params,message) # render edit.html again
        #else: # update user data succefully
        raise config.web.seeother('/alumnos/index_alumno') # render alumnos index.html
