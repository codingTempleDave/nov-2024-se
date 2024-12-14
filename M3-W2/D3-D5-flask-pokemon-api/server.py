from app import app, db, Trainer, Pokemon, trainer_schema, trainers_schema, pokemon_schema, pokemons_schema
from flask import request, jsonify
from marshmallow import ValidationError
from sqlalchemy import select

@app.route('/trainers', methods=['POST'])
def create_trainer():
    try:
        trainer_data = trainer_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    new_trainer = Trainer(name=trainer_data['name'], email=trainer_data['email'])
    db.session.add(new_trainer)
    db.session.commit()

    return trainer_schema.jsonify(new_trainer), 201


@app.route('/trainers', methods=['GET'])
def get_trainers():
    query = select(Trainer)
    trainers = db.session.execute(query).scalars().all()

    return trainers_schema.jsonify(trainers), 200


@app.route('/trainers/<int:id>', methods=['GET'])
def get_trainer(id):
    trainer = db.session.get(Trainer, id)
    return trainer_schema.jsonify(trainer), 200


@app.route('/trainers/<int:id>', methods=['PUT'])
def update_trainer(id):
    trainer = db.session.get(Trainer, id)

    if not trainer:
        return jsonify({"message": "Invalid trainer id"}), 400

    try:
        trainer_data = trainer_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    trainer.name = trainer_data['name']
    trainer.email = trainer_data['email']

    db.session.commit()
    return trainer_schema.jsonify(trainer), 200



@app.route('/trainers/<int:id>', methods=['DELETE'])
def delete_trainer(id):
    trainer = db.session.get(Trainer, id)

    if not trainer:
        return jsonify({"message": "Invalid trainer id"}), 400

    db.session.delete(trainer)
    db.session.commit()
    return jsonify({"message": f"successfully deleted {trainer.name}"}), 200


@app.route('/pokemon', methods=['POST'])
def create_pokemon():
    try:
        pokemon_data = pokemon_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    new_pokemon = Pokemon(name=pokemon_data['name'], type=pokemon_data['type'])
    db.session.add(new_pokemon)
    db.session.commit()

    return pokemon_schema.jsonify(new_pokemon), 201


@app.route('/pokemon', methods=['GET'])
def get_pokemon():
    query = select(Pokemon)
    pokemon = db.session.execute(query).scalars().all()

    return pokemons_schema.jsonify(pokemon), 200


@app.route('/trainers/<int:trainer_id>/catch_pokemon/<int:pokemon_id>', methods=['GET'])
def catch_pokemon(trainer_id, pokemon_id):
    trainer = db.session.get(Trainer, trainer_id)
    pokemon = db.session.get(Pokemon, pokemon_id)

    trainer.pokemon.append(pokemon)
    db.session.commit()
    return jsonify({"message": f"{trainer.name} caught a {pokemon.type} type {pokemon.name}"}), 200


@app.route('/trainers/<int:trainer_id>/pokemon', methods=['GET'])
def trainers_pokemon(trainer_id):
    trainer = db.session.get(Trainer, trainer_id)
    
    if not trainer:
        return jsonify({"message": "Invalid trainer id"}), 400
    
    pokemon = [p.name for p in trainer.pokemon]

    return jsonify({"message": f"{trainer.name}'s pokemon: {pokemon}"}), 200


@app.route('/trainers/<int:trainer_id>/add_pokemon', methods=['POST'])
def add_pokemon(trainer_id):
    trainer = db.session.get(Trainer, trainer_id)
    pokemon_ids = request.json

    for id in pokemon_ids['pokemon_ids']:
        pokemon = db.session.get(Pokemon, id)
        
        trainer.pokemon.append(pokemon)
        db.session.commit()

    return jsonify({"message": f"All pokemon added to {trainer.name}!"}), 200


app.run(debug=True) # runs flask server