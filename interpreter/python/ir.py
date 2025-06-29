"""
This file contains all of the intermediate representation classes used
to parse and represent Bonsai Assembly.
"""

from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, Any, List


"""
All the classes related to representing instructions.
"""
class InstructionType(Enum):
    INCREMENT = 1
    DECREMENT = 2
    TEST = 3
    JUMP = 4
    HALT = 5


class Instruction(ABC):
    def __init__(self, instruction_type: InstructionType):
        self.instruction_type = instruction_type


class Inc(Instruction):
    def __init__(self, identifier: str):
        super().__init__(InstructionType.INCREMENT)
        self.identifier = identifier


class Dec(Instruction):
    def __init__(self, identifier: str):
        super().__init__(InstructionType.DECREMENT)
        self.identifier = identifier


class Tst(Instruction):
    def __init__(self, identifier: str):
        super().__init__(InstructionType.TEST)
        self.identifier = identifier


class Jmp(Instruction):
    def __init__(self, target: int):
        super().__init__(InstructionType.JUMP)
        self.target = target


class Hlt(Instruction):
    def __init__(self):
        super().__init__(InstructionType.HALT)


"""
All the classes representing data declarations.
We use a symbol table to maintain references.
"""
class SymbolTable:
    def __init__(self):
        self.table = {}

    def add(self, identifier: str, value: int):
        if identifier in self.table:
            raise ValueError(f"Duplicate declaration of variable '{identifier}'")
        self.table[identifier] = value


"""
Represents a complete Bonsai Assembly program.
Contains a list of instructions and a symbol table for variable declarations.
"""
class Unit:
    def __init__(self, instruction_list: List["Instruction"], declarations: "SymbolTable"):
        self.instruction_list = instruction_list
        self.declarations = declarations


