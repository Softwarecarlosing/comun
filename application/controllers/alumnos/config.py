import web
import hmac
import application.models.model_grupos
import application.models.model_alumnos
import application.models.model_alumnos_grupos
import application.controllers.main.ingresoclave

render = web.template.render('application/views/alumnos/', base='master')
model_alumnos = application.models.model_alumnos
model_grupos = application.models.model_grupos
controller_clave = application.controllers.main.ingresoclave
model_alumnos_grupos = application.models.model_alumnos_grupos

secret_key = "kuorra_key"


def hash_str(s):
    return hmac.new(secret_key, s).hexdigest()


def make_secure_val(s):
    return "%s!%s" % (s, hash_str(s))


def check_secure_val(h):
    val = h.split('!')[0]
    if h == make_secure_val(val):
        return val
