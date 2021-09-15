class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    post = db.relationship('Application', backref='applicant', lazy=True)

    def __repr__(self):
        return f'User({self.username})'


class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(75), nullable=False)
    company = db.Column(db.String(75), nullable=False)
    position = db.Column(db.String(75), nullable=False)
    date = db.Column(db.Date(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'Application({self.company}, {self.position}, {self.date.strftime("%m/%d/%Y")}'
