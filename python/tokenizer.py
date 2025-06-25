import re
from tokens import TokenType, Token

class Tokeniser:
    def __init__(self, text):
        self.buffer = text.strip()
        self.current_token = None

    def next(self):
        self.buffer = self.buffer.lstrip()
        
        # Buffer is empty
        if not self.buffer:
            self.current_token = Token("EOF", TokenType.EOF)
            return

        # RegEx and their TokenType
        patterns = [
            (r'^INC\b', TokenType.INC),
            (r'^DEC\b', TokenType.DEC),
            (r'^JMP\b', TokenType.JMP),
            (r'^TST\b', TokenType.TST),
            (r'^HLT\b', TokenType.HLT),
            (r'^\.', TokenType.DOT),
            (r'^:', TokenType.COLON),
            (r'^data\b', TokenType.DATA),
            (r'^//.*', TokenType.COMMENT),                          
            (r'^[0-9]+', TokenType.NUMBER),
            (r'^[a-zA-Z_][a-zA-Z0-9_]*', TokenType.IDENTIFIER),
        ]

        for pattern, token_type in patterns:
            match = re.match(pattern, self.buffer)
            if match:
                lexeme = match.group()
                self.current_token = Token(lexeme, token_type)
                self.buffer = self.buffer[len(lexeme):]
                return

        # If nothing matched
        raise IllegalTokenException(f"Illegal token: {self.buffer}")

    def has_next(self):
        return self.current_token is None or self.current_token.get_type() != TokenType.EOF

    def get_current_token(self):
        return self.current_token
