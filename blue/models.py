from datetime import datetime
from blue import db
from blue import ma


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class Photos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.String(100))
    projects_id = db.Column(db.Integer, db.ForeignKey("projects.id"))
    projects = db.relationship("Projects", back_populates="photos")


class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(100))
    status = db.Column(db.String(50))
    project_name = db.Column(db.String(50))
    location = db.Column(db.String(50))
    project_status = db.Column(db.String(50))
    phase_number = db.Column(db.String(50))
    photos = db.relationship("Photos")


# class PhotosSchema(ma.ModelSchema):
#     class Meta:
#         fields = ('id', 'photo')
#         model = Photos


# class ProjectsSchema(ma.ModelSchema):
#     photos = ma.Nested(PhotosSchema, many=True)

#     class Meta:
#         model = Projects
#         fields = ('id', 'code', 'status',
#                   'project_name', 'phase_number', 'photos')
