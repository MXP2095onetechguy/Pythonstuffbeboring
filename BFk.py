import brainfuck

print("Brainfuck intepreter")
print("------------------------------------------------------------------------------")
# md = input("") # mode
print("""example brainfuck code provided from module: +[----->+++<]>+.---.+++++++..+++.[--->+<]>----.
------------------------------------------------------------------------------
another one: ++++[++++>---<]>-.---[----->+<]>-.+++[->+++<]>++.++++++++.+++++.--------.-[--->+<]>--.+[->+++<]>+.++++++++.+[++>---<]>-.""")
bf = input("please give your brainfuck code: ")
print("------------------------------------------------------------------------------")
print("compiled brainfuck: " + brainfuck.evaluate(bf))
input("")
