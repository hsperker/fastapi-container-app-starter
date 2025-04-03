from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional

from app.core.models import Item
from app.core.services import ItemService
from app.infrastructure.repositories import ItemRepository

router = APIRouter(
    prefix="/items",
    tags=["items"]
)

# Create a single repository instance that will be shared
item_repository = ItemRepository()

def get_item_service() -> ItemService:
    return ItemService(item_repository)

@router.get("", response_model=List[Item])
def get_items(
    item_service: ItemService = Depends(get_item_service)
) -> List[Item]:
    """Get all items"""
    return item_service.get_items()

@router.get("/{item_id}", response_model=Item)
def get_item(
    item_id: int,
    item_service: ItemService = Depends(get_item_service)
) -> Item:
    """Get a specific item by ID"""
    item = item_service.get_item(item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Item with ID {item_id} not found"
        )
    return item

@router.post("", response_model=Item, status_code=status.HTTP_201_CREATED)
def add_item(
    name: str, 
    description: Optional[str] = None,
    item_service: ItemService = Depends(get_item_service)
) -> Item:
    """Add a new item"""
    return item_service.add_item(name, description)

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(
    item_id: int,
    item_service: ItemService = Depends(get_item_service)
) -> None:
    """Delete an item"""
    success = item_service.delete_item(item_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} not found"
        )