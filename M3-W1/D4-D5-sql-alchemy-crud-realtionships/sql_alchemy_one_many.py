# Create Virtual Environment: py -m venv venv | python3 -m venv venv
# Activate it on PC:   venv\Scripts\activate
# Activate it on MAC:  source venv/bin/activate
# pip install sqlalchemy | Object Relational Mapping (ORM)
# pip install mysql-connector-python
# deactivate - gets out of the virtual environment

from sqlalchemy import create_engine
from sqlalchemy import String, DateTime, func, select, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from typing import List

engine = create_engine('mysql+mysqlconnector://root:abc123@localhost/starwarsdb', echo=True)

class Base(DeclarativeBase):
    pass

class Sith(Base):
    __tablename__ = "sith"

    sith_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable = False)
    lightsaber_color: Mapped[str] = mapped_column(String(100))
    sith_title: Mapped[str] = mapped_column(String(100))
    created_at = mapped_column(DateTime, default=func.now()) 
    updated_at = mapped_column(DateTime, default=func.now(), onupdate=func.now())
		
	#One-to-Many relationship from this Sith to a List of Apprentice Objects
    apprentices: Mapped[List["Apprentice"]] = relationship(back_populates="master", cascade="all, delete-orphan")
    
class Apprentice(Base):
    __tablename__ = "apprentices"

    apprentice_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    sith_id: Mapped[int] = mapped_column(ForeignKey("sith.sith_id"))
    created_at = mapped_column(DateTime, default=func.now()) 
    updated_at = mapped_column(DateTime, default=func.now(), onupdate=func.now())
		
    #Many-to-One relationship, Multiple Apprentice objects can point back to the same Sith
    master: Mapped["Sith"] = relationship(back_populates="apprentices")
    
Base.metadata.create_all(engine)

session = Session(engine)

# palpatine = Sith(name="Emperor Palpatine", lightsaber_color='red', sith_title="Emperor")
# dooku = Sith(name="Count Dooku", lightsaber_color='red', sith_title = "Count")
# snoke = Sith(name="Supreme Leader Snoke", lightsaber_color='red', sith_title="Supreme Leader")

# vader = Apprentice(name="Darth Vader")
# maul = Apprentice(name="Darth Maul")
# kylo = Apprentice(name="Kylo Ren")
# ventress = Apprentice(name="Asajj Ventress")

# palpatine.apprentices.append(vader)
# palpatine.apprentices.append(maul)
# dooku.apprentices.append(ventress)
# snoke.apprentices.append(kylo)

# session.add(palpatine)
# session.add(dooku)
# session.add(snoke) 

# session.add(vader)
# session.add(maul)
# session.add(kylo)
# session.add(ventress)

# session.commit()


#First we query the Sith
query = select(Sith).where(Sith.name == 'Emperor Palpatine')
sith = session.execute(query).scalars().first()

# Then we can display all the apprentices of that Sith
print(f"{sith.name}'s apprentices:")
for apprentice in sith.apprentices:
	print(apprentice.name)
 
#First we query our apprentice
query = select(Apprentice).where(Apprentice.name == 'Asajj Ventress')
apprentice = session.execute(query).scalars().first()

print(f"{apprentice.name}'s master is {apprentice.master.name}") 