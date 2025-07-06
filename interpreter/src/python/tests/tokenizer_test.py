import sys
sys.path.append("..")
import token
from tokenizer import Tokeniser

def usage():
    print("Usage:")
    print("  python tokenizer_test.py --interactive       Run the tokenizer in interactive mode")
    print("  python tokenizer_test.py --test              Run the predefined testing suite")
    print("  python tokenizer_test.py --file <filename>   Run the tokenizer on a given file")

"""
Parses command-line arguments.

Returns a tuple (mode, filename):
- mode: "interactive", "test", or "file"
- filename: only set if mode == "file"
"""
def parse_args(argv):
    if len(argv) == 2:
        if argv[1] == "--interactive":
            return ("interactive", None)
        elif argv[1] == "--test":
            return ("test", None)
        else:
            usage()
            sys.exit(1)
    elif len(argv) == 3 and argv[1] == "--file":
        return ("file", argv[2])
    else:
        usage()
        sys.exit(1)

def run_tests():
    print("Running test suite...")

    tests = [
        {
            "source": "INC x",
            "expected": [("INC", "INC"), ("x", "IDENTIFIER"), ("EOF", "EOF")]
        },
        {
            "source": "DEC counter",
            "expected": [("DEC", "DEC"), ("counter", "IDENTIFIER"), ("EOF", "EOF")]
        },
        {
            "source": "JMP 10",
            "expected": [("JMP", "JMP"), ("10", "NUMBER"), ("EOF", "EOF")]
        },
        {
            "source": "TST x\nHLT",
            "expected": [
                ("TST", "TST"), 
                ("x", "IDENTIFIER"), 
                ("HLT", "HLT"),
                ("EOF", "EOF")
            ]
        },
        {
            "source": "// This is a comment\nINC a",
            "expected": [
                ("// This is a comment", "COMMENT"),
                ("INC", "INC"),
                ("a", "IDENTIFIER"),
                ("EOF", "EOF")
            ]
        },
        {
            "source": ".data:\nmyVar: 42",
            "expected": [
                (".", "DOT"),
                ("data", "DATA"),
                (":", "COLON"),
                ("myVar", "IDENTIFIER"),
                (":", "COLON"),
                ("42", "NUMBER"),
                ("EOF", "EOF")
            ]
        },
    ]

    for i, test in enumerate(tests):
        tokenizer = Tokeniser(test["source"])
        result = []
        while tokenizer.has_next():
            tokenizer.next()
            tok = tokenizer.get_current_token()
            result.append((tok.get_token(), tok.get_type().name))

        assert result == test["expected"], f"Test {i + 1} failed.\nExpected: {test['expected']}\nGot:      {result}"
        print(f"Test {i + 1} passed.")

    print("All tests passed!")

def run_interactive():
    print("Interactive mode. Enter Bonsai assembly. Ctrl+D to exit.")
    try:
        while True:
            line = input(">>> ")
            tokenizer = Tokeniser(line)
            while tokenizer.has_next():
                tokenizer.next()
                print(tokenizer.get_current_token())
    except EOFError:
        print("\nExiting interactive mode.")

def run_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            tokenizer = Tokeniser(content)
            while tokenizer.has_next():
                tokenizer.next()
                print(tokenizer.get_current_token())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

if __name__ == "__main__":
    mode, filename = parse_args(sys.argv)
    if mode == "interactive":
        run_interactive()
    elif mode == "test":
        run_tests()
    elif mode == "file":
        run_file(filename)
