from . import db

class User (db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer,primary_key=True)
  username = db.Column(db.String(255))
  comment_id = db.Column(db.Integer,db.ForeignKey('comment.id'))



class Comment (db.Model):
  __tablename__ = 'comment'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255))
  users = db.relationship('Users', backref='comment',lazy='dynamic')





  def __repr__(self):
    return f'User(username)'