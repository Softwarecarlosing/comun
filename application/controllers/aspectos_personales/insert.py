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
            email = app.session.user
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
        
        # call model insert_aspectos_personales and try to insert new data
        config.model.insert_aspectos_personales(
            form['email'],
            form['estado_civil'],
            form['numero_hijos'],
            form['quien_los_cuida'],
            form['no_integrantes_familia'],
            form['comunicacion_familiar'],
            form['responsable'],
            form['respetuosa'],
            form['trabajo_equipo'],
        )
        #raise config.web.seeother('/aspectos_economicos/insert') # render aspectos_personales index.html
        app.session.loggedin = True
        app.session.user 
        app.session.privilege = 4 
        raise config.web.seeother('/alumnos/index_alumno') # render trayectorias_academicas index.html
