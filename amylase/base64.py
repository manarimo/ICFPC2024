import itertools
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source_file")
    args = parser.parse_args()

    unit_size = 2
    with open(args.source_file) as f:
        to_encode = f.read().strip()

    chars = "LRDU"
    units = [''.join(t) for t in itertools.product(chars, repeat=unit_size)]
    table = ''.join(units)
    indices = []
    for i in range(0, len(to_encode), unit_size):
        raw = to_encode[i: i + unit_size]
        for v, unit in enumerate(units):
            if unit[: len(raw)] == raw:
                indices.append(v)
                break
    assert ''.join([units[v] for v in indices])[:len(to_encode)] == to_encode
    encoded = ''.join([chr(v + 33) for v in indices])

    source_code = f"""\
-- base64 format: [encoded: ICFP string] [prefix: ICFP integer]
-- encoded string is decoded to LRDU string and then first prefix characters are taken

-- Finally take prefix
BT

-- String length
@I{len(to_encode)}

-- Pass the encoded string
B$

-- Make the recursive function of Decode
B$
  Lf B$ Lx B$ vf B$ vx vx Lx B$ vf B$ vx vx -- Fix
  -- Decode :: Self -> String -> String
  -- Decodes the first entry in the source then recursively process the rest.
  Ld Ls
    ? ( B= vs S )
      S
      B.
        BT @I{unit_size} BD (B* @I{unit_size} U# (BT @I1 vs)) @S{table} -- Decode the first entry
        (B$ vd (BD @I1 vs)) -- Process the rest

-- Encoded string
S{encoded}
"""
    print(source_code)


if __name__ == "__main__":
    main()
