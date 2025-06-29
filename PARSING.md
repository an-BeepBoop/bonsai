## Lexing, Parsing + Grammar

The simplicity of Bonsai Assembly does not necessitate constructing a parse tree. Instead, a flat list format is used to store instructions.

### Tokens

In addition to reserved keywords for instructions, the following token productions are defined:
```
Identifier ::= Letter (Letter | Digit | `_`)*
Number     ::= Digit (Digit)*
```
---

### Grammar Notation
The current Bonsai Assembly parser utilises an LL(k) recursive descent parser. The grammar is defined as follows:

```
<Unit> ::=  <InstrList> <Data> 
```

**Instruction Productions**
```
<InstrList> ::= <Instr> <InstrList> | ε
<Instr>     ::= <TstInstr> | <JmpInstr> | <DecInstr> | <IncInstr> | <HltInstr>
<TstInstr>  ::= tst Identifier  
<JmpInstr>  ::= jmp Number  
<DecInstr>  ::= dec Identifier  
<IncInstr>  ::= inc Identifier  
<HltInstr>  ::= hlt
```

**Data Section**
```
<Data>     ::= "." "data" ":" <DeclList> | ε
<DeclList> ::= <Decl> <DeclList> | ε
<Decl> ::= Identifier ":" Number
```
