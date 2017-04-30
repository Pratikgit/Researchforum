import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from datetime import datetime
from researchforum.lib.base import BaseController, render
from researchforum.model import *
import json

log = logging.getLogger(__name__)

class ActionController(BaseController):

    def __before__(self):
        log.info("In before..")
        c.user_id = request.cookies.get('login', None)
        log.info("Login Cookie:%s" %c.user_id)

    def index(self):
        if c.user_id:
            redirect(url(controller='action', action='feeds'))
        else:
            return render('/login.html')

    def signup(self):
        if c.user_id:
            redirect(url(controller='action', action='feeds'))
        else:
            return render('/signup.html')

    def get_user(self):
        if c.user_id:
            redirect(url(controller='action', action='feeds'))
        else:
            email_id = request.params.get('email')
            password = request.params.get('password')
            u = User.objects(email_id = email_id, password = password)
            if u:
                u = u[0]
                log.info("User Created Successfully with id:%s" %u.id)
                c.user_id = "%s" %u.id
                response.set_cookie('login', '%s' %c.user_id, max_age = 18000)
                redirect(url(controller = 'action', action='feeds'))
            else:
                return "Some Error While Login."

    def create_user(self):
        if c.user_id:
            redirect(url(controller='action', action='feeds'))
        else:
            name = request.params.get('name')
            email_id = request.params.get('email')
            password = request.params.get('password')
            university = request.params.get('university')
            log.info("Params are:%s %s %s %s" %(name, email_id, password, university))
            new_user = User(email_id = email_id, name = name, password = password, university = university).save()
            c.user_id = "%s" %new_user.id
            if new_user:
                log.info("User Created Successfully with id:%s" %c.user_id)
                response.set_cookie('login', '%s' %c.user_id, max_age = 18000)
                redirect(url(controller = 'action', action='feeds'))
            else:
                return "Error while creating user.."

    def feeds(self):
        if not c.user_id:
            redirect(url(controller='action', action='index')) 
        u = User.objects(id = c.user_id)[0] 
        log.info("User Data:%s" %u)
        c.default_papers = []
        c.final_papers = []
        if u.tag_ids:
            tags = u.tag_ids.split(", ") 
            for paper in Paper.objects():
                paper_tags = paper.tag_ids.split(', ')
                for tag in tags:
                    if tag in paper_tags:
                        c.default_papers.append(paper.to_dict())
            for paper in c.default_papers:
                summary_list = []
                for s in Summary.objects():
                    print "%s %s" %(paper[0], s.paper_id)
                    if paper[0] == s.paper_id:
                        summary_list.append(s.to_dict())
                new_p = paper
                new_p.append(summary_list)
                c.final_papers.append(new_p) 
            log.info("Default Papers:%s" %c.final_papers)
            return render('/wall.html')
        else:
            return "No Feed to Display..."
    
    def create_post(self):
        if not c.user_id:
            redirect(url(controller='action', action='index')) 
        title = request.params.get('title')
        author_names = request.params.get('author_names')
        conf_name = request.params.get('conf_name')
        publication_date = request.params.get('publication_date')
        url = request.params.get('url')
        tag_ids = request.params.get('tag_ids')
        summary = request.params.get('summary')
        publication_date = datetime.strptime(publication_date, '%Y-%m-%d')
        p = Paper(title = title, authors = author_names, conference = conf_name, 
                        publication_date = publication_date, url = url, tag_ids = tag_ids).save()
        if p:
            if summary:
                s = Summary(contents = summary, user_id = c.user_id, paper_id = str(p.id), time = datetime.utcnow()).save() 
            redirect(url(controller = 'action', action='feeds'))
        else:
            return "Error while creating new Post.."

