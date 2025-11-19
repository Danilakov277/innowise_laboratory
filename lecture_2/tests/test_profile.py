import pytest
import sys
import os

# Добавляем корневую директорию проекта в Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Теперь импортируем из main
from main import life_stage, Profile, get_user_hobbies, CURRENT_YEAR


class TestLifeStage:
    """Test cases for life_stage function."""
    
    def test_child_age(self):
        """Test ages 0-12 return 'Child'."""
        assert life_stage(0) == "Child"
        assert life_stage(6) == "Child"
        assert life_stage(12) == "Child"
    
    def test_teenager_age(self):
        """Test ages 13-19 return 'Teenager'."""
        assert life_stage(13) == "Teenager"
        assert life_stage(16) == "Teenager"
        assert life_stage(19) == "Teenager"
    
    def test_adult_age(self):
        """Test ages 20+ return 'Adult'."""
        assert life_stage(20) == "Adult"
        assert life_stage(25) == "Adult"
        assert life_stage(100) == "Adult"


class TestProfile:
    """Test cases for Profile class."""
    
    def test_profile_creation(self):
        """Test Profile creation with valid data."""
        user_dict = {
            "name": "John Doe",
            "birth_year": 1990,
            "current_age": CURRENT_YEAR - 1990,
            "life_stage": life_stage(CURRENT_YEAR - 1990),
            "hobbies": ["reading", "swimming"]
        }
        
        profile = Profile(user_dict)
        
        assert profile.name == "John Doe"
        assert profile.birth_year == 1990
        assert profile.current_age == CURRENT_YEAR - 1990
        assert profile.life_stage == "Adult"
        assert profile.hobbies == ["reading", "swimming"]
    
    def test_profile_str_with_hobbies(self):
        """Test string representation with hobbies."""
        user_dict = {
            "name": "Alice Smith",
            "birth_year": 2010,
            "current_age": 15,
            "life_stage": "Teenager",
            "hobbies": ["music", "sports"]
        }
        
        profile = Profile(user_dict)
        result = str(profile)
        
        assert "Alice Smith" in result
        assert "15" in result
        assert "Teenager" in result
        assert "Favorite Hobbies (2):" in result
        assert "- music" in result
        assert "- sports" in result
    
    def test_profile_str_without_hobbies(self):
        """Test string representation without hobbies."""
        user_dict = {
            "name": "Bob Johnson",
            "birth_year": 2000,
            "current_age": 25,
            "life_stage": "Adult",
            "hobbies": []
        }
        
        profile = Profile(user_dict)
        result = str(profile)
        
        assert "Bob Johnson" in result
        assert "25" in result
        assert "Adult" in result
        assert "You didn't mention any hobbies." in result
        assert "Favorite Hobbies" not in result
    
    def test_profile_slots(self):
        """Test that __slots__ are properly defined."""
        user_dict = {
            "name": "Test User",
            "birth_year": 1995,
            "current_age": 30,
            "life_stage": "Adult",
            "hobbies": ["test"]
        }
        
        profile = Profile(user_dict)
        
        # Test that __slots__ restricts attribute assignment
        with pytest.raises(AttributeError):
            profile.non_existent_attr = "value"


class TestGetUserHobbies:
    """Test cases for get_user_hobbies function."""
    
    def test_get_hobbies_with_stop(self, monkeypatch):
        """Test hobby collection with stop command."""
        inputs = ["reading", "swimming", "stop"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
        
        hobbies = get_user_hobbies()
        
        assert hobbies == ["reading", "swimming"]
    
    def test_get_hobbies_with_different_stop_commands(self, monkeypatch):
        """Test hobby collection with various stop commands."""
        stop_commands = ["exit", "quit", "done", "end", "STOP"]
        
        for stop_cmd in stop_commands:
            inputs = ["hobby1", "hobby2", stop_cmd]
            monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
            
            hobbies = get_user_hobbies()
            assert hobbies == ["hobby1", "hobby2"]
    
    def test_get_hobbies_empty_input_skipped(self, monkeypatch):
        """Test that empty inputs are skipped."""
        inputs = ["", "hobby1", "", "hobby2", "stop"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
        
        hobbies = get_user_hobbies()
        
        assert hobbies == ["hobby1", "hobby2"]
    
    def test_get_hobbies_case_insensitive_stop(self, monkeypatch):
        """Test case insensitive stop command recognition."""
        inputs = ["hobby1", "STOP", "hobby2"]  # Should stop after "STOP"
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
        
        hobbies = get_user_hobbies()
        
        assert hobbies == ["hobby1"]  # "hobby2" should not be added


class TestIntegration:
    """Integration tests for the complete flow."""
    
    def test_complete_flow(self, monkeypatch):
        """Test the complete user profile creation flow."""
        # Mock user inputs
        inputs = [
            "John Doe",           # name
            "1990",               # birth year
            "reading",            # hobby 1
            "gaming",             # hobby 2  
            "stop"                # stop command
        ]
        input_iterator = iter(inputs)
        monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))
        
        # Execute main logic
        name = "John Doe"
        birth_year = 1990
        current_age = CURRENT_YEAR - birth_year
        hobbies = ["reading", "gaming"]
        
        user_dict = {
            "name": name,
            "birth_year": birth_year,
            "current_age": current_age,
            "life_stage": life_stage(current_age),
            "hobbies": hobbies
        }
        
        profile = Profile(user_dict)
        
        # Verify the result
        assert profile.name == "John Doe"
        assert profile.birth_year == 1990
        assert profile.life_stage == "Adult"
        assert profile.hobbies == ["reading", "gaming"]
        
        profile_str = str(profile)
        assert "John Doe" in profile_str
        assert "Adult" in profile_str
        assert "Favorite Hobbies (2):" in profile_str


def test_current_year_constant():
    """Test that CURRENT_YEAR is properly defined."""
    assert CURRENT_YEAR == 2025
    assert isinstance(CURRENT_YEAR, int)