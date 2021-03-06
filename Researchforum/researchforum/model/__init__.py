from mongoengine import *
import logging

log = logging.getLogger(__name__)

connect("RESEARCH_FORUM_DB")

class User(Document):
    email_id = StringField(required = True)
    name = StringField(required = True)
    password = StringField(required = True)
    university = StringField(default = None)
    bio = StringField(default = None)
    tag_ids = StringField(default = None)

class Paper(Document):
    title = StringField(required = True)
    authors = StringField(default = None)
    conference = StringField(default = None)
    publication_date = DateTimeField(default = None)
    url = StringField(default = None)
    tag_ids = StringField(default = None)

    def to_dict(self):
        return [str(self.id),self.title,self.authors,self.authors,
                self.publication_date,self.url,self.tag_ids]

class Tags(Document):
    domain_name = StringField(default = None)

class Summary(Document):
    contents = StringField(required = True)
    user_id = StringField(required = True)
    paper_id = StringField(required = True)
    time = DateTimeField(default = None)
    comments = StringField(default = None)
    upvote = IntField(default = 0)

    def to_dict(self):
        return [str(self.id),self.contents,self.user_id,self.paper_id,str(self.upvote)]

class Comments(Document):
    comment = StringField(required = True)
    summary_id = StringField(required = True)
    user_id = StringField(required = True)


