"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()




class Cupcake(db.Model):
    """cupcake"""

    __tablename__= 'cupcakes'
   

    id = db.Column(db.Integer,primary_key=True,
                    autoincrement=True,
                    nullable=False)
    flavor = db.Column(db.String(40), nullable=True)
    size = db.Column(db.String(20), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    
    image = db.Column(db.String(200), nullable=False, default="https://tinyurl.com/demo-cupcake")

    def to_dict(self):
        """Serialize cupcake to dict"""

        return {
            "id": self.id,
            "flavor": self.flavor,
            "rating": self.rating,
            "size": self.size,
            "image": self.image,
        }
        

def connect_db(app):
    db.app = app
    db.init_app(app)
