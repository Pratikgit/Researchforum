import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from researchforum.lib.base import BaseController, render
from researchforum.model import *

log = logging.getLogger(__name__)

class SignupController(BaseController):

    def index(self):
        #ross = User(email='ross@example.com', name='Ross', password='122').save()
        return render('/signup.html')

    def create_user(self):
        name = request.params.get('name')
        email = request.params.get('email')
        password = request.params.get('password')
        uni_name = request.params.get('university')
        log.info("Params are:%s %s %s %s" %(name, email, password, uni_name))
        new_user = User(email=email, name=name, password=password, uni_name = uni_name).save()
        c.user_id = "%s" %new_user.id
        if new_user:
            log.info("User Created Successfully with id:%s" %c.user_id)
            #return "User Created..."
            response.set_cookie('login', 'present', max_age = 18000)
            return "User Created..."
        else:
            return "Error while creating user.."
    
