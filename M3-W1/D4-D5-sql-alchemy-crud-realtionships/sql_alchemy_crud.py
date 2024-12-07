# Create Virtual Environment: py -m venv venv | python3 -m venv venv
# Activate it on PC:   venv\Scripts\activate
# Activate it on MAC:  source venv/bin/activate
# pip install sqlalchemy | Object Relational Mapping (ORM)
# pip install mysql-connector-python
# deactivate - gets out of the virtual environment

from sqlalchemy import create_engine
from sqlalchemy import String, DateTime, func, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

engine = create_engine('mysql+mysqlconnector://root:abc123@localhost/starwarsdb')

class Base(DeclarativeBase):
    pass

# python code that creates a sith table
class Sith(Base):
    __tablename__ = "sith"

    sith_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable = False)
    lightsaber_color: Mapped[str] = mapped_column(String(100))
    sith_title: Mapped[str] = mapped_column(String(100))
    created_at = mapped_column(DateTime, default=func.now())  # Automatically set at row creation
    updated_at = mapped_column(DateTime, default=func.now(), onupdate=func.now())
    
Base.metadata.create_all(engine)

session = Session(engine)

# maul = Sith(name="Darth Maul", lightsaber_color='red', sith_title = "Apprentice")
# vader = Sith(name="Darth Vader", lightsaber_color='red', sith_title = "Master")
# palpatine = Sith(name="Emperor Palpatine", lightsaber_color='red', sith_title = "Emperor")
# dooku = Sith(name="Count Dooku", lightsaber_color='red', sith_title = "Count")

# session.add(maul)
# session.add(vader)
# session.add(palpatine)
# session.add(dooku)
# session.commit()

# View the Sith
query = select(Sith)
sith = session.execute(query).scalars().all() # returns a list of Sith instances

# Print the Sith
for s in sith:
    print(f"Sith info: {s.name} | {s.lightsaber_color} | {s.sith_title}")
    
# View specific Sith
query = select(Sith).where(Sith.name == "Darth Vader")
sith = session.execute(query).scalars().first() # returns instance, not a list

print(f"Found Sith: {sith.name}") 

# Starts with Darth
starts_with_darth = session.query(Sith).filter(Sith.name.like('Darth%')).all()

for s in starts_with_darth:
    print(f"Starts with Darth: {s.name} | {s.lightsaber_color} | {s.sith_title}")
    

# Update Sith
query = select(Sith).where(Sith.sith_id == 3)
sith = session.execute(query).scalars().first()

sith.name = 'Darth Sidious'

session.commit()

# Delete Sith
query = select(Sith).where(Sith.sith_id == 4)
sith = session.execute(query).scalars().first()

session.delete(sith)
session.commit()