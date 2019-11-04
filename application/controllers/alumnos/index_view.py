import config 
import app


class IndexView:
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
            if privilege == 0: # admin user
              return self.GET_INDEX_VIEW(params) # call GET_INDEX() function
            if privilege == 1: # admin user
              return self.GET_INDEX_VIEW(params) # call GET_INDEX() function
            if privilege == 2:
              return self.GET_INDEX_VIEW(params) 
            else: # guess user
              raise config.web.seeother('/') # rendner guess.html
        else: # the user dont have logged
             params = {}
             params['user'] = 'anonymous'
             params['privilege'] = '-1'
             raise config.web.seeother('/') # render login.html
  



  
   @staticmethod
   def GET_INDEX_VIEW(params):
        result = config.model_alumnos_grupos.get_all_alumnos_grupos().list()
        for row in result:
            row.email = config.make_secure_val(str(row.email))
        return config.render.index_view(result,params)
