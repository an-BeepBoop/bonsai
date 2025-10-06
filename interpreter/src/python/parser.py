from ir import Unit, Instruction, SymbolTable
from tokenizer import Tokeniser
from typing import List, Tuple

class IllegalParseException(Exception):
    pass

class Parser:
    def __init__(self, text: str):
        self.tokenizer = Tokeniser(text)
    
    def parse(self) -> Unit:
        """
        Adheres to the grammar rule:       
        <Unit> ::=  <InstrList> <Data>
        """
        instructions = parse_instruction_list()
        declarations = parse_declaration_list()
        unit = Unit(instructions, declarations)
        return unit
        
    def parse_instruction_list(self) -> List[Instruction]:
        """
        Adheres to the grammar rule:       
        <InstrList> ::= <Instr> <InstrList> | ε
        """
        pass

    def parse_instruction(self) -> Instruction:
        """
        Adheres to the grammar rule:       
        <Instr>     ::= <TstInstr> | <JmpInstr> | <DecInstr> | <IncInstr> | <HltInstr>
        <TstInstr>  ::= tst Identifier  
        <JmpInstr>  ::= jmp Number  
        <DecInstr>  ::= dec Identifier  
        <IncInstr>  ::= inc Identifier  
        <HltInstr>  ::= hlt
        """
        pass

    def parse_declaration_list(self) -> SymbolTable:
        """
        Adheres to the grammar rule:
        <Data>     ::= "." "data" ":" <DeclList> | ε
        <DeclList> ::= <Decl> <DeclList> | ε
        """
        pass

    def parse_declaration(self) -> Tuple[str, int]:
        """
        Adheres to the grammar rule:
        <Decl> ::= Identifier ":" Number
        """
        current_token = tokenizer
        pass





