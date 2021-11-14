import sys
import matrix_scanner  # matrix_scanner.py is a file you create, (it is not an external library)
import matrix_parser

if __name__ == '__main__':

    mode = 'parse'

    if mode == 'scan':
        try:
            filename = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
            file = open(filename, "r")
        except IOError:
            print("Cannot open {0} file".format(filename))
            sys.exit(0)

        text = file.read()
        lexer = matrix_scanner.Scanner()

        # Give the lexer some input
        lexer.input(text)

        # Tokenize
        while True:
            tok = lexer.token()
            if not tok:
                break  # No more input
            print(tok)

    if mode == 'parse':
        try:
            filename = sys.argv[1] if len(sys.argv) > 1 else "example1.m"
            file = open(filename, "r")
        except IOError:
            print("Cannot open {0} file".format(filename))
            sys.exit(0)

        parser = matrix_parser.parser
        text = file.read()
        parser.parse(text, lexer=matrix_scanner.lexer)
