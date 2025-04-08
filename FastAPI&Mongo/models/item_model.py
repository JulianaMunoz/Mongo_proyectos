from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    _id: str = None
    nombre: str
    descripcion: Optional[str] = None
    precio: int = None

class ItemResponse(Item):
    id: str
