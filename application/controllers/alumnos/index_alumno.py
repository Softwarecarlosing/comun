import config 
import app


class IndexAlumno:
   def __init__(self):
	   pass

     
   def GET(self):
        if app.session.loggedin is True: # validate if the user is logged
            email = app.session.user
            privilege = app.session.privilege # get the session_privilege
            picture = app.session.picture 
            params = {}
            params['user'] = email
            params['privilege'] = privilege
            if privilege == 4: # admin user
              return self.GET_INDEX(params) # call GET_INDEX() function
            else: # guess user
              raise config.web.seeother('/') # rendner guess.html
        else: # the user dont have logged
             params = {}
             params['user'] = 'anonymous'
             params['privilege'] = '-1'
             raise config.web.seeother('/') # render login.html
  



  
   @staticmethod
   def GET_INDEX(params):
        return config.render.index_alumno(params)


