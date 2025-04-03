import pytest
from unittest.mock import Mock
from typing import List, Optional
from app.core.models import Item
from app.core.services import ItemService
from app.infrastructure.repositories import ItemRepository

class TestItemService:
    """Test suite for the ItemService class"""
    
    @pytest.fixture
    def mock_repository(self) -> Mock:
        """Create a mock repository for testing"""
        repository = Mock(spec=ItemRepository)
        # Setup common mock return values
        repository.get_all.return_value = [
            Item(id=1, name="Test item", description="Test description")
        ]
        return repository
        
    @pytest.fixture
    def item_service(self, mock_repository: Mock) -> ItemService:
        """Create an ItemService with a mock repository for testing"""
        return ItemService(mock_repository)
    
    def test_get_items(self, item_service: ItemService, mock_repository: Mock) -> None:
        """Test retrieving all items"""
        # Arrange
        expected_items: List[Item] = [Item(id=1, name="Test item", description="Test description")]
        mock_repository.get_all.return_value = expected_items
        
        # Act
        result = item_service.get_items()
        
        # Assert
        assert result == expected_items
        mock_repository.get_all.assert_called_once()
    
    def test_get_item(self, item_service: ItemService, mock_repository: Mock) -> None:
        """Test retrieving a single item"""
        # Arrange
        item_id: int = 1
        expected_item: Item = Item(id=item_id, name="Test item", description="Test description")
        mock_repository.get_by_id.return_value = expected_item
        
        # Act
        result = item_service.get_item(item_id)
        
        # Assert
        assert result == expected_item
        mock_repository.get_by_id.assert_called_once_with(item_id)
    
    def test_get_item_not_found(self, item_service: ItemService, mock_repository: Mock) -> None:
        """Test retrieving a non-existent item"""
        # Arrange
        item_id: int = 999
        mock_repository.get_by_id.return_value = None
        
        # Act
        result = item_service.get_item(item_id)
        
        # Assert
        assert result is None
        mock_repository.get_by_id.assert_called_once_with(item_id)
    
    def test_add_item(self, item_service: ItemService, mock_repository: Mock) -> None:
        """Test adding a new item"""
        # Arrange
        name: str = "new item"
        description: str = "new description"
        expected_item: Item = Item(id=2, name="New item", description="new description")
        mock_repository.create.return_value = expected_item
        
        # Act
        result = item_service.add_item(name, description)
        
        # Assert
        assert result == expected_item
        # Verify business rule: name should be capitalized
        mock_repository.create.assert_called_once_with("New item", description)
    
    def test_delete_item(self, item_service: ItemService, mock_repository: Mock) -> None:
        """Test deleting an item"""
        # Arrange
        item_id: int = 1
        mock_repository.delete.return_value = True
        
        # Act
        result = item_service.delete_item(item_id)
        
        # Assert
        assert result is True
        mock_repository.delete.assert_called_once_with(item_id)
    
    def test_delete_item_not_found(self, item_service: ItemService, mock_repository: Mock) -> None:
        """Test deleting a non-existent item"""
        # Arrange
        item_id: int = 999
        mock_repository.delete.return_value = False
        
        # Act
        result = item_service.delete_item(item_id)
        
        # Assert
        assert result is False
        mock_repository.delete.assert_called_once_with(item_id)