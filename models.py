from app import db

class Show(db.Model):
  __tablename__ = 'shows'
  id = db.Column(db.Integer, primary_key=True)
  venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'), nullable=False)
  artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)
  start_time = db.Column(db.String(), nullable=False)

class Venue(db.Model):
    __tablename__ = 'venues'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    city = db.Column(db.String())
    state = db.Column(db.String())
    address = db.Column(db.String())
    phone = db.Column(db.String())
    image_link = db.Column(db.String(), nullable=True)
    facebook_link = db.Column(db.String())
    seeking_talent = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(), default='We are seeking a talent')
    website = db.Column(db.String())
    genres = db.Column(db.ARRAY(db.String()))
    shows = db.relationship('Show', backref='venue')

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    city = db.Column(db.String())
    state = db.Column(db.String())
    address = db.Column(db.String())
    phone = db.Column(db.String())
    image_link = db.Column(db.String())
    facebook_link = db.Column(db.String())
    seeking_venue = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(), default='We are seeking a venue')
    website = db.Column(db.String())
    genres = db.Column(db.ARRAY(db.String()))
    shows = db.relationship('Show', backref='artist')

    # TODO: implement any missing fields, as a database migration using Flask-Migrate