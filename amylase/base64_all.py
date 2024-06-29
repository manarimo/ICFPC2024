import subprocess
from to_scheme import encode_string

def run(command: str):
    subprocess.call(command, shell=True)

hand_solutions = {
    5: "RDLLLLULURRULRRRRRDLRRDLRRDLLDRLLDRLLLLLLLURLLURLLURULRURURURRRRRRRDRUURRDLDRDLLRDRDDDLDLRRDDLULDLUDLLLLLLLLLULDLLURURLLURLUUUURURURURLLLLDRLD",
    7: "RRRRRRLLDDDLLLDDDRRRRRRRRRRRUUULLUUURRUUULLLLLDDDDDDRRLLUUUUUULLLLLLDDUURRRUUULLLLLLLLRRRRRRRRUUUUUULLLLDDRRDDLULDLULDLUURRUULLLLDDDLLRRDDDDDDLLRRRRRDDDRLLLLLLRRDDDRRRDDDRRLLLLLLLLLLLLLUUURRRRRUUUUUDDDDDLLLUUULLUUURRRRRUUUUUULLLLLRRRRRUUUUUUUUDDLLLLLUUURRRRRUUUDDDLLLLLUUUURRRRRRRRRRRDDDDLLLLLRRDDDRRRLLLUUURRRRRRUUUURRRRRRRRRRRDDDDDDDLLLLLUUURRRRLLLLUUUDDDLLLLLRRDDDLLLRRRUUURRRDDDDDDDDDLLRRRRRRRLLLLLDDDDD",
    10: "RRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRDDLRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRDDLRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRDDLRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRDDLRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRURRRRRRRRRRDRRUDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLULLLLLLLLLLDLLUDRRURRDRRRRRRRRRRURRDRRRRRRRRRRURRDRRRRRRRRRRURRDRRRRRRRRRRU",
}

for problem_id in [7]:
    if problem_id in hand_solutions:
        with open("steps.txt", "w") as f:
            f.write(hand_solutions[problem_id])
    else:
        run(f"../yuusti/a.out < ../lambdaman/in/{problem_id:02}.txt > steps.txt")
    run("python3 base64.py steps.txt > out.asm")
    run("../osak/asm.rb out.asm > out.icfp")

    with open("out.icfp") as f:
        program = f.read()
    solve_command = f"solve lambdaman{problem_id} "

    final_program = f"B. S{encode_string(solve_command)} {program}".strip()
    with open("submit.icfp", "w") as f:
        f.write(final_program)

    print(f"id: {problem_id}, solution size: {len(final_program)}")