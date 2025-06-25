from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Modelo de datos
class Item(BaseModel):
    id: int
    nombre: str
    descripcion: str = None
    precio: float
    disponible: bool = True

# Base de datos en memoria con dos elementos
items_db: List[Item] = [
    Item(id=1, nombre="Muñeca", descripcion="muñeca bonita", precio=12000.0, disponible=True),
    Item(id=2, nombre="Carrito", descripcion="A control remoto", precio=750
