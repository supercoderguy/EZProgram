#EZProgram Interpreter

file = input('Enter the EZProgram file you want to run (/path/to/file.ezp): ')
var = {}
varlist = []

class execute:
    def say(command):
        message = command.split("say", 1)[1].strip().strip("'")
        print(message)
    def math(command):
        ans = eval(command.split('math', 1)[1].strip().strip('\''))
        print(ans)
    def ask(command):
        print(input(command.split('ask', 1)[1].strip().strip('\'')))
    def var(variable, content):
        var[variable] = content
        print(var[variable])

with open(file, 'r') as ezpf:
    program_lines = ezpf.readlines()

for line in program_lines:
    line = line.strip()
    if line.startswith("say"):
        execute.say(line)
    elif line.startswith('math'):
        execute.math(line)
    elif line.startswith('ask'):
        execute.ask(line)
    elif line.startswith('var'):
        varlist = (line.split())
        execute.var(varlist[1], varlist[3])
    else:
        print(f"Unknown command: {line}")
