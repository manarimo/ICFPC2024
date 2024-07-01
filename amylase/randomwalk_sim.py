import randomwalk as rw

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--problem", help="problem_file")
    parser.add_argument("-i", "--problem-id", help="problem_id")

    args = parser.parse_args()
    with open(args.problem, encoding="ascii") as f:
        problem = f.read()

    rw.init_global(problem, args.problem_id)
    for i in range(100, 1000):
        print(f"Testing {i}")
        code, term, num_cells, visited_cells, completed_step, home_steps = rw.simulate(12356 + i)
        if num_cells == visited_cells:
            print(12356+i, completed_step, home_steps)
        print(f"{visited_cells}/{num_cells}")
    # print(code)


if __name__ == "__main__":
    main()
