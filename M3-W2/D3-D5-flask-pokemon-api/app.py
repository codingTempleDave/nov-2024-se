# py -m venv venv | python3 -m venv venv - create virtual env
# venv\Scripts\activate | source venv/bin/activate - activate virtual env 
# pip install Flask Flask-SQLAlchemy Flask-Marshmallow mysql-connector-python marshmallow-sqlalchemy
# create flask_pokemon database in workbench
# pip freeze > requirements.txt - Saving list of installed packages

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import ForeignKey, Table, String, Column
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import List, Optional

# Initialize Flask app
app = Flask(__name__)

# MySQL database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:abc123@localhost/flask_pokemon'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Creating our Base Model
class Base(DeclarativeBase):
    pass

# Initialize SQLAlchemy and Marshmallow
db = SQLAlchemy(model_class=Base)
db.init_app(app)
ma = Marshmallow(app)

#The association table between Users and Pets
trainer_pokemon = Table(
	"trainer_pokemon",
	Base.metadata,
	Column("trainer_id", ForeignKey("trainers.trainer_id")),
	Column("pokemon_id", ForeignKey("pokemon.pokemon_id")),
)

class Trainer(Base):
    __tablename__ = "trainers"
    
    trainer_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[Optional[str]] = mapped_column(String(200))
		
	# One-to-Many relationship from this Trainer to a List of Pokemon Objects
    pokemon: Mapped[List["Pokemon"]] = relationship(secondary=trainer_pokemon, back_populates="trainers")
    
class Pokemon(Base):
    __tablename__ = "pokemon"

    pokemon_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    type: Mapped[str] = mapped_column(String(200))
		
    #One-to-Many relationship, One Pokemon can be owned by a List of Trainer Objects
    trainers: Mapped[List["Trainer"]] = relationship(secondary=trainer_pokemon, back_populates="pokemon")

# Trainer Schema
class TrainerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trainer
        
# Pokemon Schema
class PokemonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pokemon       
       
# Initialize Schemas
trainer_schema = TrainerSchema()
trainers_schema = TrainerSchema(many=True) #Can serialize many Trainer objects (a list of them)
pokemon_schema = PokemonSchema()
pokemons_schema = PokemonSchema(many=True)

# Without the app context, Flask wouldn't know which app's configuration to use.     
with app.app_context():
    db.create_all() # uses the schema to create the database tables  