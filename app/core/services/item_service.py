from typing import List, Optional
from app.core.models import Item
from app.infrastructure.repositories import ItemRepository

class ItemService:
    def __init__(self, repository: ItemRepository):
        self.repository = repository
    
    def get_items(self) -> List[Item]:
        """Get all available items"""
        return self.repository.get_all()
    
    def get_item(self, item_id: int) -> Optional[Item]:
        """Get a specific item by ID"""
        return self.repository.get_by_id(item_id)
    
    def add_item(self, name: str, description: Optional[str] = None) -> Item:
        """Add a new item with business rules"""
        # Apply business rules: capitalize the name
        name = name.capitalize()
        
        # Store the item via repository
        return self.repository.create(name, description)
    
    def delete_item(self, item_id: int) -> bool:
        """Delete an item"""
        return self.repository.delete(item_id)