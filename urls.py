




urls = (
    '/', 'application.controllers.main.index.Index',
    '/404', 'application.controllers.main.notfound.NotFound',
    '/500', 'application.controllers.main.internalerror.InternalError',
    '/loginselection', 'application.controllers.main.loginselection.LoginSelection',
    '/loginselectionadmin','application.controllers.main.loginselectionadmin.LoginSelectionAdmin',
    "/login", "application.controllers.main.login.LoginPage",
    '/loginlocal', "application.controllers.main.loginlocal.LoginLocal",
    '/logingoogleadmin', 'application.controllers.main.logingoogleadmin.LoginPage',
    '/loginlocaladmin', 'application.controllers.main.loginlocaladmin.LoginLocalAdmin',
    "/logout", "application.controllers.main.logout.Logout",
    "/auth2/(google)", "application.controllers.main.logingoogleadmin.AuthPage",
    "/auth2/(google)/callback", "application.controllers.main.logingoogleadmin.AuthCallbackPage",
    "/auth/(google)", "application.controllers.main.login.AuthPage",
    "/auth/(google)/callback", "application.controllers.main.login.AuthCallbackPage",
    '/users', 'application.controllers.users.index.Index',
    '/ingresoclave', 'application.controllers.main.ingresoclave.ValidacionClave',
    '/users/printer', 'application.controllers.users.printer.Printer',
    '/users/view/(.+)', 'application.controllers.users.view.View',
    '/users/edit/(.+)', 'application.controllers.users.edit.Edit',
    '/users/delete/(.+)', 'application.controllers.users.delete.Delete',
    '/users/insert', 'application.controllers.users.insert.Insert',
    '/users/change_pwd', 'application.controllers.users.change_pwd.Change_pwd',
    '/logs', 'application.controllers.logs.index.Index',
    '/logs/printer', 'application.controllers.logs.printer.Printer',
    '/logs/view/(.+)', 'application.controllers.logs.view.View',
    '/tutoria', 'application.controllers.tutoria.index.Index',
    '/tutoria/view/(.+)', 'application.controllers.tutoria.view.View',
    '/tutoria/edit/(.+)', 'application.controllers.tutoria.edit.Edit',
    '/tutoria/delete/(.+)', 'application.controllers.tutoria.delete.Delete',
    '/tutoria/insert', 'application.controllers.tutoria.insert.Insert',
    '/programas_educativos', 'application.controllers.programas_educativos.index.Index',
    '/programas_educativos/view/(.+)', 'application.controllers.programas_educativos.view.View',
    '/programas_educativos/edit/(.+)', 'application.controllers.programas_educativos.edit.Edit',
    '/programas_educativos/delete/(.+)', 'application.controllers.programas_educativos.delete.Delete',
    '/programas_educativos/insert', 'application.controllers.programas_educativos.insert.Insert',
    '/grupos_alumnos', 'application.controllers.grupos_alumnos.index.Index',
    '/grupos_alumnos/view/(.+)', 'application.controllers.grupos_alumnos.view.View',
    '/grupos_alumnos/edit/(.+)', 'application.controllers.grupos_alumnos.edit.Edit',
    '/grupos_alumnos/delete/(.+)', 'application.controllers.grupos_alumnos.delete.Delete',
    '/grupos_alumnos/insert', 'application.controllers.grupos_alumnos.insert.Insert',
    '/tutores_grupos', 'application.controllers.tutores_grupos.index.Index',
    '/tutores_grupos/view/(.+)', 'application.controllers.tutores_grupos.view.View',
    '/tutores_grupos/edit/(.+)', 'application.controllers.tutores_grupos.edit.Edit',
    '/tutores_grupos/delete/(.+)', 'application.controllers.tutores_grupos.delete.Delete',
    '/tutores_grupos/insert', 'application.controllers.tutores_grupos.insert.Insert',
    '/periodos', 'application.controllers.periodos.index.Index',
    '/periodos/view/(.+)', 'application.controllers.periodos.view.View',
    '/periodos/edit/(.+)', 'application.controllers.periodos.edit.Edit',
    '/periodos/delete/(.+)', 'application.controllers.periodos.delete.Delete',
    '/periodos/insert', 'application.controllers.periodos.insert.Insert',
    '/grupos', 'application.controllers.grupos.index.Index',
    '/grupos/view/(.+)', 'application.controllers.grupos.view.View',
    '/grupos/edit/(.+)', 'application.controllers.grupos.edit.Edit',
    '/grupos/delete/(.+)', 'application.controllers.grupos.delete.Delete',
    '/grupos/insert', 'application.controllers.grupos.insert.Insert',
    '/alumnos/index_alumno', 'application.controllers.alumnos.index_alumno.IndexAlumno',
    '/alumnos','application.controllers.alumnos.index_view.IndexView',
    '/alumno', 'application.controllers.alumnos.index.Index',
    '/alumnos/view/(.+)', 'application.controllers.alumnos.view.View',
    '/alumnos/edit/(.+)', 'application.controllers.alumnos.edit.Edit',
    '/alumnos/delete/(.+)', 'application.controllers.alumnos.delete.Delete',
    '/alumnos/insert', 'application.controllers.alumnos.insert.Insert',
    '/padres_tutores', 'application.controllers.padres_tutores.index.Index',
    '/padres_tutores_ingreso', 'application.controllers.padres_tutores.padres_tutores_ingreso.PadresTutoresIngreso',
    '/padres_tutores/view/(.+)', 'application.controllers.padres_tutores.view.View',
    '/padres_tutores/edit/(.+)', 'application.controllers.padres_tutores.edit.Edit',
    '/padres_tutores/delete/(.+)', 'application.controllers.padres_tutores.delete.Delete',
    '/padres_tutores/insert', 'application.controllers.padres_tutores.insert.Insert',
    '/historiales_medicos', 'application.controllers.historiales_medicos.index.Index',
    '/historiales_medicos_ingreso', 'application.controllers.historiales_medicos.historiales_medicos_ingreso.HistorialesMedicosIngreso',
    '/historiales_medicos/view/(.+)', 'application.controllers.historiales_medicos.view.View',
    '/historiales_medicos/edit/(.+)', 'application.controllers.historiales_medicos.edit.Edit',
    '/historiales_medicos/delete/(.+)', 'application.controllers.historiales_medicos.delete.Delete',
    '/historiales_medicos/insert', 'application.controllers.historiales_medicos.insert.Insert',
    '/aspectos_economicos', 'application.controllers.aspectos_economicos.index.Index',
    '/aspectos_economicos_ingreso', 'application.controllers.aspectos_economicos.aspectos_economicos_ingreso.AspectosEconomicosIngreso',
    '/aspectos_economicos/view/(.+)', 'application.controllers.aspectos_economicos.view.View',
    '/aspectos_economicos/edit/(.+)', 'application.controllers.aspectos_economicos.edit.Edit',
    '/aspectos_economicos/delete/(.+)', 'application.controllers.aspectos_economicos.delete.Delete',
    '/aspectos_economicos/insert', 'application.controllers.aspectos_economicos.insert.Insert',
    '/aspectos_personales', 'application.controllers.aspectos_personales.index.Index',
    '/aspectos_personales_ingreso','application.controllers.aspectos_personales.aspectos_personales_ingreso.AspectosPersonalesIngreso',
    '/aspectos_personales/view/(.+)', 'application.controllers.aspectos_personales.view.View',
    '/aspectos_personales/edit/(.+)', 'application.controllers.aspectos_personales.edit.Edit',
    '/aspectos_personales/delete/(.+)', 'application.controllers.aspectos_personales.delete.Delete',
    '/aspectos_personales/insert', 'application.controllers.aspectos_personales.insert.Insert',
    '/trayectorias_academicas', 'application.controllers.trayectorias_academicas.index.Index',
    '/trayectorias_academicas_ingreso', 'application.controllers.trayectorias_academicas.trayectorias_academicas_ingreso.TrayectoriasAcademicasIngreso',
    '/trayectorias_academicas/view/(.+)', 'application.controllers.trayectorias_academicas.view.View',
    '/trayectorias_academicas/edit/(.+)', 'application.controllers.trayectorias_academicas.edit.Edit',
    '/trayectorias_academicas/delete/(.+)', 'application.controllers.trayectorias_academicas.delete.Delete',
    '/trayectorias_academicas/insert', 'application.controllers.trayectorias_academicas.insert.Insert',
    '/trayectorias_academicas/finalizar', 'application.controllers.trayectorias_academicas.finalizar.Finalizar',
    '/area_atencion', 'application.controllers.area_atencion.index.Index',
    '/area_atencion/view/(.+)', 'application.controllers.area_atencion.view.View',
    '/area_atencion/edit/(.+)', 'application.controllers.area_atencion.edit.Edit',
    '/area_atencion/delete/(.+)', 'application.controllers.area_atencion.delete.Delete',
    '/area_atencion/insert', 'application.controllers.area_atencion.insert.Insert',
    '/tutoria_especial', 'application.controllers.tutoria_especial.index.Index',
    '/tutoria_especial/view/(.+)', 'application.controllers.tutoria_especial.view.View',
    '/tutoria_especial/edit/(.+)', 'application.controllers.tutoria_especial.edit.Edit',
    '/tutoria_especial/delete/(.+)', 'application.controllers.tutoria_especial.delete.Delete',
    '/tutoria_especial/insert', 'application.controllers.tutoria_especial.insert.Insert',
    '/tutores_grupos', 'application.controllers.tutores_grupos.index.Index',
    '/tutores_grupos/view/(.+)', 'application.controllers.tutores_grupos.view.View',
    '/tutores_grupos/edit/(.+)', 'application.controllers.tutores_grupos.edit.Edit',
    '/tutores_grupos/delete/(.+)', 'application.controllers.tutores_grupos.delete.Delete',
    '/tutores_grupos/insert', 'application.controllers.tutores_grupos.insert.Insert',
    '/observaciones_individuales', 'application.controllers.observaciones_individuales.index.Index',
    '/observaciones_individuales/view/(.+)', 'application.controllers.observaciones_individuales.view.View',
    '/observaciones_individuales/edit/(.+)', 'application.controllers.observaciones_individuales.edit.Edit',
    '/observaciones_individuales/delete/(.+)', 'application.controllers.observaciones_individuales.delete.Delete',
    '/observaciones_individuales/insert/(.+)', 'application.controllers.observaciones_individuales.insert.Insert',
    '/observaciones_individuales/alumnos', 'application.controllers.observaciones_individuales.alumnos.Alumnos',
   )