import config
import hashlib
import app
from random import choice



class Insert:

    def __init__(self):
        pass

    
    def GET(self):
        if app.session.loggedin is True:
            session_user = app.session.user
            session_user = app.session.privilege  # get the session_privilege
            if session_user == 0: # admin user
                return self.GET_INSERT() # call GET_INSERT() function
            else: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self):
        if app.session.loggedin is True: # validate if the user is logged
            session_user = app.session.user
            session_user = app.session.privilege # get the session_privilege
            if session_user == 0: # admin user
                return self.POST_INSERT() # call POST_EDIT function
            else : # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html
      

    
    def GET(self):
        programas_educativos = config.model_programas_educativos.get_all_programas_educativos()
        periodos = config.model_periodos.get_all_periodos()
        return config.render.insert(programas_educativos,periodos) # render insert.html

    
    def POST(self):
        form = config.web.input() # get form data
        longitud = 7

        # asignacion de valores de donde se obtendra la clave
        valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+*/"

        # iniciamos la variable 
        p = "" 

        # igualamos la variable a la clave obtenida
        # se unen y se elige por cada longitud se elige la catidad en los valores
        clave_grupo = p.join([choice(valores) for i in range(longitud)])


        # call model insert_grupos and try to insert new data
        config.model.insert_grupos(
            form['id_programa_educativo'],
            form['id_periodo'],
            form['grupo'],
            clave_grupo,
        )
        raise config.web.seeother('/grupos') # render grupos index.html

   
    