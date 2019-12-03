import argparse

if __name__ == "__main__":
    # Parse CLI arguements
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str,
                        help="Input file with wires.")
    parser.add_argument("--part", type=int, default=1,
                        choices=[1, 2],
                        help="Either sovling part 1 or part 2 of problem")
    args = parser.parse_args()

    # Read in input file with list of masses and parse
    with open(args.input_file, 'r') as f:
        contents = f.readlines()

    wires = []
    for row in contents:
        wires.append([x.strip() for x in row.split(',')])

    assert len(wires) == 2
    for i, wire in enumerate(wires):
        print("Wire {}: {}\n".format(i + 1, ','.join(wire)))
