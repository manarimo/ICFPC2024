$TEST = true

require_relative '../asm.rb'

tokens = tokenize("BT @I12 @Shoge")
cst = parse(tokens)
puts print_nodes(cst)

tokens = tokenize("@Ssolve@_lambdaman11")
cst = parse(tokens) 
puts print_nodes(cst) #=> S3/,6%},!-"$!-!.VV == String("solve lambdaman11")
