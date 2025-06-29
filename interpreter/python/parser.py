from ir import Unit, Instruction, SymbolTable
from tokenizer import Tokeniser

class Parser:
    def __init__(self, text: str):
        self.tokenizer = Tokenizer(text)


    def parse(self) -> Unit:
        pass




