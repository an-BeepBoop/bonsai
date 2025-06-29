from enum import Enum 

class TokenType(Enum):
    INC = 1
    DEC = 2
    JMP = 3
    TST = 4
    HLT = 5
    IDENTIFIER = 6
    COLON = 7
    SECTION = 8
    DOT = 9
    DATA = 10
    NUMBER = 11 
    COMMENT = 12
    EOF = 13

class IllegalTokenException(Exception):
    pass

class Token():
    def __init__(self, token: str, type: TokenType):
        self.token = token
        self.type = type
    
    def get_token(self) -> str:
        return self.token

    def get_type(self) -> TokenType:
        return self.type

    def __str__(self):
        if self.type == TokenType.IDENTIFIER:
            return f"IDENTIFIER({self.token})"
        elif self.type == TokenType.NUMBER:
            return f"NUMBER({self.token})"
        elif self.type == TokenType.COMMENT:
            return f"COMMENT({self.token[2:]})"
        return self.type.name

