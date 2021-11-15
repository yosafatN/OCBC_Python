from config import db, ma


class Avocado(db.Model):
    __tablename__ = "avocado"
    date = db.Column(db.DateTime)
    avgprice = db.Column(db.Float())
    totalvol = db.Column(db.Integer())
    avo_a = db.Column(db.Integer())
    avo_b = db.Column(db.Integer())
    avo_c = db.Column(db.Integer())
    type = db.Column(db.Integer())
    regionid = db.Column(db.Integer())


class AvocadoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Avocado
        sqla_session = db.session
        load_instance = True
