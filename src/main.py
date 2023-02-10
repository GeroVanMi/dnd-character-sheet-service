import json

from bson import json_util
from bson.objectid import ObjectId
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from Character import Character
from DatabaseHandler import get_mongo_db_collection

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "OK"}


@app.put('/create-character')
async def creat_character(character: Character):
    collection = get_mongo_db_collection()

    collection.insert_one({
        "name": character.name,
        "maxHP": character.max_hp
    })

    return JSONResponse(character, 201)


@app.get("/character")
async def get_character():
    collection = get_mongo_db_collection()
    characters = list(collection.find())
    # We have to cast the pymongo cursor object to a list in order to force it to unwrap.
    return JSONResponse(json.loads(json_util.dumps(characters)))


@app.get("/character/{character_id}")
async def get_character_by(character_id: str):
    collection = get_mongo_db_collection()
    character = collection.find_one({"_id": ObjectId(character_id)})
    return JSONResponse(json.loads(json_util.dumps(character)))
