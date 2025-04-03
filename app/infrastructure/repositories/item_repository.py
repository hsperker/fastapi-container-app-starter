from typing import Dict, List, Optional
from app.core.models import Item

class ItemRepository:
    """A mock repository that simulates database operations"""
    
    def __init__(self) -> None:
        # In-memory storage using a dictionary as a simple database
        self._items: Dict[int, Item] = {
            1: Item(id=1, name="Plumbus", description="A Plumbus is an all-purpose home device.")
        }
        self._counter = 1
    
    def get_all(self) -> List[Item]:
        """Get all items from the database"""
        return list(self._items.values())
    
    def get_by_id(self, item_id: int) -> Optional[Item]:
        """Get an item by its ID"""
        return self._items.get(item_id)
    
    def create(self, name: str, description: Optional[str] = None) -> Item:
        """Create a new item in the database"""
        self._counter += 1
        new_item = Item(
            id=self._counter,
            name=name,
            description=description
        )
        self._items[new_item.id] = new_item
        return new_item
    
    def delete(self, item_id: int) -> bool:
        """Delete an item from the database"""
        if item_id in self._items:
            del self._items[item_id]
            return True
        return False