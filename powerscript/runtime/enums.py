"""
PowerScript Enum Support

Provides enum functionality for PowerScript
"""

from enum import Enum, IntEnum, Flag, IntFlag, auto
from typing import Any, Dict, Type, Union


class PowerScriptEnum(Enum):
    """Base enum class for PowerScript with additional functionality"""
    
    def __str__(self) -> str:
        """String representation"""
        return self.name
        
    def __repr__(self) -> str:
        """Debug representation"""
        return f"{self.__class__.__name__}.{self.name}"
    
    @classmethod
    def from_value(cls, value: Any) -> 'PowerScriptEnum':
        """Create enum from value"""
        for member in cls:
            if member.value == value:
                return member
        raise ValueError(f"No {cls.__name__} member with value {value}")
    
    @classmethod
    def from_name(cls, name: str) -> 'PowerScriptEnum':
        """Create enum from name"""
        try:
            return cls[name]
        except KeyError:
            raise ValueError(f"No {cls.__name__} member with name '{name}'")
    
    @classmethod
    def values(cls) -> list:
        """Get all enum values"""
        return [member.value for member in cls]
    
    @classmethod
    def names(cls) -> list:
        """Get all enum names"""
        return [member.name for member in cls]
    
    @classmethod
    def items(cls) -> list:
        """Get all (name, value) pairs"""
        return [(member.name, member.value) for member in cls]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {"name": self.name, "value": self.value}


class PowerScriptIntEnum(IntEnum):
    """Integer enum for PowerScript"""
    
    def __str__(self) -> str:
        return self.name
    
    @classmethod  
    def from_value(cls, value: int) -> 'PowerScriptIntEnum':
        """Create enum from value"""
        return cls(value)
    
    @classmethod
    def from_name(cls, name: str) -> 'PowerScriptIntEnum':
        """Create enum from name"""
        return cls[name]


class PowerScriptFlag(Flag):
    """Flag enum for PowerScript (supports bitwise operations)"""
    
    def __str__(self) -> str:
        return self.name
    
    @classmethod
    def from_value(cls, value: int) -> 'PowerScriptFlag':
        """Create flag from value"""
        return cls(value)


class PowerScriptIntFlag(IntFlag):
    """Integer flag enum for PowerScript"""
    
    def __str__(self) -> str:
        return self.name
    
    @classmethod
    def from_value(cls, value: int) -> 'PowerScriptIntFlag':
        """Create flag from value"""
        return cls(value)


# Utility functions for enum creation
def create_enum(name: str, members: Union[list, dict], base_class: Type = PowerScriptEnum) -> Type[PowerScriptEnum]:
    """Create an enum class dynamically"""
    if isinstance(members, list):
        # List of names, auto-assign values
        members_dict = {member: auto() for member in members}
    elif isinstance(members, dict):
        # Dictionary of name -> value
        members_dict = members
    else:
        raise ValueError("Members must be a list or dictionary")
    
    return type(name, (base_class,), members_dict)


def create_int_enum(name: str, members: Union[list, dict]) -> Type[PowerScriptIntEnum]:
    """Create an integer enum class dynamically"""
    return create_enum(name, members, PowerScriptIntEnum)


def create_flag_enum(name: str, members: Union[list, dict]) -> Type[PowerScriptFlag]:
    """Create a flag enum class dynamically"""
    return create_enum(name, members, PowerScriptFlag)


# Example usage and common enums
class Status(PowerScriptEnum):
    """Example status enum"""
    PENDING = "pending"
    RUNNING = "running" 
    COMPLETED = "completed"
    FAILED = "failed"


class Priority(PowerScriptIntEnum):
    """Example priority enum"""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


class Permission(PowerScriptFlag):
    """Example permission flags"""
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()
    DELETE = auto()
    
    # Composite permissions
    READ_WRITE = READ | WRITE
    ALL = READ | WRITE | EXECUTE | DELETE