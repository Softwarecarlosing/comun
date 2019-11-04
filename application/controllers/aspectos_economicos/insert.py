import config
import hashlib
import app

class Insert:

    def __init__(self):
        pass

    
    def GET(self):
        if app.session.loggedin is True:
            email = app.session.user
            privilege = app.session.privilege  # get the session_privilege
            if privilege == 4: # admin user
              return self.GET_INSERT() # call GET_INSERT() function
            else: # guess user
              raise config.web.seeother('/') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            privilege = app.session.privilege # get the session_privilege
            if privilege == 4: # admin user
                return self.POST_INSERT() # call POST_EDIT function
            else: # guess user
                raise config.web.seeother('/') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_INSERT():
        message = None
        email = app.session.user
        return config.render.insert(email,message) # render insert.html




    @staticmethod
    def POST_INSERT():
    
        form = config.web.input() # get form data

        # call model insert_aspectos_economicos and try to insert new data
        config.model.insert_aspectos_economicos(
            form['email'],
            form['beca'],
            form['nombre_beca'],
            form['depende_economicamente'],
            form['tiene_computadora'],
            form['tiene_telefono'],
            form['trabaja'],
            form['empresa'],
            form['jefe_inmediato'],
            form['telefono_trabajo'],
            form['email_trabajo'],
            form['actividad'],
            form['jornada_laboral'],
            form['calle'],
            form['colonia'],
            form['cp'],
            form['no_exterior'],
            form['no_interior'],
            form['municipio'],
            form['referencias'],
        )
        #raise config.web.seeother('/historiales_medicos/insert') # render aspectos_economicos index.html
        app.session.loggedin = True
        app.session.user 
        app.session.privilege = 4 
        raise config.web.seeother('/alumnos/index_alumno') # render trayectorias_academicas index.html
