## Lexing, Parsing + Grammar

The simplicity of Bonsai Assembly does not necessitate constructing a parse tree. Instead, a flat list format is used to store instructions.

### Tokens

In addition to reserved keywords for instructions, the following token productions are defined:
```
Identifier = Letter {Letter | Digit | `_`}
Number = Digit {Digit}
```
---

### Grammar Notation

We use the following notation for defining grammar syntax:
```
X Y — X followed by Y  
X | Y — X or Y  
[X] — optional X  
{X} — zero or more X  
```

The grammar is defined as follows:
```
<Unit> ::= { <Instr> } [ <Data> ]
```

**Instruction Productions**
```
<Instr>    ::= <TstInstr> | <JmpInstr> | <DecInstr> | <IncInstr> | <HltInstr>
<TstInstr> ::= tst Identifier  
<JmpInstr> ::= jmp Number  
<DecInstr> ::= dec Identifier  
<IncInstr> ::= inc Identifier  
<HltInstr> ::= hlt
```

**Data Section**
```
<Data> ::= "." "data" ":" { <Decl> }  
<Decl> ::= Identifier ":" Number
```
