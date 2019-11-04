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
            if privilege == 3: # admin user
              return self.GET_INSERT() # call GET_INSERT() function
            else: # guess user
              raise config.web.seeother('/') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            privilege = app.session.privilege # get the session_privilege
            if privilege == 3: # admin user
                return self.POST_INSERT() # call POST_EDIT function
            else: # guess user
                raise config.web.seeother('/') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_INSERT():
        #grupos = config.model_grupos.get_all_grupos()
        #grupo = config.controller_clave.verificar
        #int grupo=app.session.grupo

        app.session.clave_grupo
        #id_grupo=app.session.grupo
        #grupo=config.model_grupos.search_grup(id_grupo) 
        #grupo=app.session.grupo
        #app.session.clave_grupo
        #grupo = int(grup)
        #grup.split('id_grupo')[1]
        #grupo = grup.split('id_grupo')[1]
        message = None 
        clave_grupo=app.session.clave_grupo
        grup = config.model_grupos.validate_id(clave_grupo)
        grupo=grup
        #grupo = config.application.controllers.main.ingresoclave.grupo(grupo)
        return config.render.insert(message)


    @staticmethod
    def POST_INSERT():
        form = config.web.input()

        email = app.session.user
        matricula = email.split('@')[0]
        app.session.clave_grupo
        clave_grupo=app.session.clave_grupo
        grup = config.model_grupos.validate_id(clave_grupo)
        grupoobtenido=grup

        id_grupo=str(grupoobtenido['id_grupo'])
        

        #try:
           #app.session.grupo[0]
      #hd = profile['hd']
           #hd = profile['hd']
        #except KeyError:
         #pass
        #id_grupo=app.session.grupo
        #id_grupo=id_grup.split('')[1]
        #id_grupo=grup
        #id_grupo=config.model_grupos.search_grup(id_grupo)
        #grupo=config.model_grupos.validate_id(clave_grupo)
        
        config.model_alumnos.insert_alumnos(
            email,
            id_grupo,
            matricula,
            form['fecha_alta'],
            form['nombre'],
            form['ap_paterno'],
            form['ap_materno'],
            form['fecha_nacimiento'],
            form['curp'],
            form['cuatrimestre'],
            form['telefono_celular'],
            form['telefono_casa'],
            email,
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
        
        #raise config.web.seeother('/aspectos_personales/insert')
        app.session.loggedin = True
        app.session.user = email
        app.session.privilege = 4 
        raise config.web.seeother('/alumnos/index_alumno') # render alumnos index.html
        




#modificar #manejar 3 perfiles de ingrs grupo, cuatrimiestre 0-1 municipio idomas correo en perfil formularios  gruo diecto idiomas combo  
"""<div class="form-group">
     <label>Grupos</label>
     <select name="id_grupo" class="form-control">
           
                <option value=$grupo>$grupo</option>
     </select>
</div>"""

#str(int(grupo))