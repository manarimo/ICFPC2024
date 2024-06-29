import subprocess

problem_id = 8

with open(f"{problem_id:02}.out") as f:
    text = f.read()

assignments = {}
for l in text.splitlines():
    l = l.replace("[", "").replace("]", "").replace("v", "").replace(",", "").strip()
    if not l:
        continue
    var, val = [c.strip() for c in l.split("=")]
    assignments[int(var)] = val == "True"

variable_count = len(assignments)
print(f"{variable_count} variables found")

v = []
for i in range(1, variable_count + 1):
    v.append(int(assignments[i]))
print(v)

def to_decimal(v):
    dec = 0
    for b in v:
        dec = dec * 2 + b
    return dec


def submit(x):
    print(f"submit {x}")
    subprocess.call(f"python3 ../cli.py send -s -d 'solve efficiency{problem_id} {x}'", shell=True)

def submit_around(x):
    print(f"try around {x}")
    for xx in range(x - 1, x + 2):
        submit(xx)

submit(to_decimal(v))
submit(to_decimal(reversed(v)))

