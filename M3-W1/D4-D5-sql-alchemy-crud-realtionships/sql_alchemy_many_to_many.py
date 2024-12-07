from sqlalchemy import create_engine, Table, Column
from sqlalchemy import String, DateTime, func, select, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from typing import List

engine = create_engine('mysql+mysqlconnector://root:abc123@localhost/starwarsdb', echo=True)

class Base(DeclarativeBase):
    pass

sith_appentice = Table(
	"sith_apprentice",
	Base.metadata,
	Column("sith_id", ForeignKey("sith.sith_id")),
	Column("apprentice_id", ForeignKey("apprentices.apprentice_id")),
)

class Sith(Base):
    __tablename__ = "sith"

    sith_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable = False)
    lightsaber_color: Mapped[str] = mapped_column(String(100))
    sith_title: Mapped[str] = mapped_column(String(100))
    created_at = mapped_column(DateTime, default=func.now()) 
    updated_at = mapped_column(DateTime, default=func.now(), onupdate=func.now())
		
	#Many to many relationship from this Sith to a List of Apprentice Objects
    apprentices: Mapped[List["Apprentice"]] = relationship(secondary="sith_apprentice", back_populates="masters")
    
class Apprentice(Base):
    __tablename__ = "apprentices"

    apprentice_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    created_at = mapped_column(DateTime, default=func.now()) 
    updated_at = mapped_column(DateTime, default=func.now(), onupdate=func.now())
		
    #Many to many relationship from this Apprentice to a List of Sith Objects
    masters: Mapped[List["Sith"]] = relationship(secondary="sith_apprentice", back_populates="apprentices")

Base.metadata.create_all(engine)

session = Session(engine)

palpatine = Sith(name="Emperor Palpatine", lightsaber_color='red', sith_title="Emperor")
dooku = Sith(name="Count Dooku", lightsaber_color='red', sith_title = "Count")
snoke = Sith(name="Supreme Leader Snoke", lightsaber_color='red', sith_title="Supreme Leader")

vader = Apprentice(name="Darth Vader")
maul = Apprentice(name="Darth Maul")
kylo = Apprentice(name="Kylo Ren")
ventress = Apprentice(name="Asajj Ventress")

palpatine.apprentices.append(vader)
palpatine.apprentices.append(maul)
kylo.masters.append(snoke)
kylo.masters.append(palpatine)

session.add(palpatine)
session.add(dooku)
session.add(snoke)
session.add(vader)
session.add(maul)
session.add(kylo)
session.add(ventress)

session.commit()

#viewing the apprentices of the sith
for apprentice in palpatine.apprentices:
	print(apprentice.name)	

#Viewing the masters of an apprentice
for master in kylo.masters:
	print(master.name)