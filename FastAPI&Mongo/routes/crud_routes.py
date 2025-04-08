from fastapi import APIRouter, HTTPException, Depends
from models.item_model import Item, ItemResponse
from datab.conexion_db import get_database
from motor.motor_asyncio import AsyncIOMotorDatabase

router = APIRouter()

def crud_helper(item: dict) -> dict:
    return {
        "id": str(item["_id"]),
        "nombre": item["nombre"],
        "descripcion": item.get("descripcion"),
        "precio": item.get("precio"),
    }

@router.get("/items/", response_model=list[ItemResponse])
async def get_items(db: AsyncIOMotorDatabase = Depends(get_database)):
    items = []
    async for item in db.items.find():
        items.append(crud_helper(item))
    return items

@router.post("/items/", response_model=ItemResponse, status_code=201)
async def create_item(
    item: Item,
    db: AsyncIOMotorDatabase = Depends(get_database),
):
    item_dict = item.dict()
    item_dict["_id"] = item_dict["nombre"]
    await db.items.insert_one(item_dict)
    nuevo_item = await db.items.find_one({"_id": item_dict["nombre"]})
    return crud_helper(nuevo_item)

@router.get("/items/{id}", response_model=ItemResponse)
async def get_item(id: str, db: AsyncIOMotorDatabase = Depends(get_database)):
    item = await db.items.find_one({"_id": id})
    if item:
        return crud_helper(item)
    raise HTTPException(status_code=404, detail="Item no encontrado")

@router.put("/items/{id}", response_model=ItemResponse)
async def update_sitio(
    id: str,
    item: Item,
    db: AsyncIOMotorDatabase = Depends(get_database),
):
    item_data = {k: v for k, v in item.dict().items() if v is not None}
    result = await db.items.update_one({"_id": id}, {"$set": item_data})
    if result.modified_count:
        item_actualizado = await db.items.find_one({"_id": id})
        return crud_helper(item_actualizado)
    raise HTTPException(status_code=404, detail="Item no encontrado")

@router.delete("/{id}")
async def delete_sitio(
    id: str,
    db: AsyncIOMotorDatabase = Depends(get_database),
):
    result = await db.items.delete_one({"_id": id})
    if result.deleted_count:
        return {"message": "Item eliminado"}
    raise HTTPException(status_code=404, detail="Item no encontrado")
