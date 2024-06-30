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
    for i in range(0, 10000):
        print(f"Testing {i}")
        code, term, num_cells, visited_cells = rw.simulate(12356 + i)
        if term:
            print(12356+i, term)
        print(f"{visited_cells}/{num_cells}")
    # print(code, term)


if __name__ == "__main__":
    main()
