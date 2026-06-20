from dataclasses import dataclass

@dataclass
class User:
    id: str
    name: str
    role: str
    email: str = ""