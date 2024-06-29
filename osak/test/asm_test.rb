$TEST = true

require_relative '../asm.rb'

tokens = tokenize("BT @I12 @Shoge")
cst = parse(tokens)
print_nodes(cst)
