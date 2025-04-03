import pytest
from typing import List
from app.core.models import Item
from app.core.services import ItemService
from app.infrastructure.repositories import ItemRepository

class TestItemServiceIntegration:
    """Integration tests for ItemService with the actual repository"""
    
    @pytest.fixture
    def item_service(self) -> ItemService:
        """Create an ItemService with the actual repository implementation"""
        repository = ItemRepository()  # Uses real implementation
        return ItemService(repository)
    
    def test_full_item_lifecycle(self, item_service: ItemService) -> None:
        """Test the full lifecycle of an item: create, get, delete"""
        # Get initial items (should include the default item)
        initial_items: List[Item] = item_service.get_items()
        initial_count: int = len(initial_items)
        assert initial_count >= 1
        
        # Add a new item
        name: str = "test item"
        description: str = "test description"
        created_item: Item = item_service.add_item(name, description)
        
        # Verify the item was created with correct data
        assert created_item.id is not None
        assert created_item.name == "Test item"  # Should be capitalized
        assert created_item.description == description
        
        # Get the item by ID
        retrieved_item = item_service.get_item(created_item.id)
        assert retrieved_item is not None
        assert retrieved_item.id == created_item.id
        assert retrieved_item.name == created_item.name
        assert retrieved_item.description == created_item.description
        
        # Get all items, should include the new one
        all_items = item_service.get_items()
        assert len(all_items) == initial_count + 1
        
        # Delete the item
        deleted = item_service.delete_item(created_item.id)
        assert deleted is True
        
        # Verify it's gone
        assert item_service.get_item(created_item.id) is None
        assert len(item_service.get_items()) == initial_count