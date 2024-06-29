import itertools
import argparse


def compress(to_encode: str) -> str:
    chars = "LRDU"

    for unit_size in range(8, 1, -1):
        candidate_units = [''.join(t) for t in itertools.product(chars, repeat=unit_size)]

        indices = []
        for i in range(0, len(to_encode), unit_size):
            raw = to_encode[i: i + unit_size]
            for v, unit in enumerate(candidate_units):
                if unit[: len(raw)] == raw:
                    indices.append(v)
                    break
        if len(set(indices)) > 94:
            continue
            # raise ValueError(f"failed to construct lookup table for unit_size {unit_size}")
        break
       
    zahyo_assyuku = {v: i for i, v in enumerate(set(indices))}
    zahyo_tenkai = {i: v for v, i in zahyo_assyuku.items()}

    units = [candidate_units[zahyo_tenkai[i]] for i in range(len(zahyo_assyuku))]
    indices = [zahyo_assyuku[v] for v in indices]

    assert ''.join([units[v] for v in indices])[:len(to_encode)] == to_encode
    encoded = ''.join([chr(v + 33) for v in indices])

    table = ''.join(units)

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
    return source_code


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source_file")
    args = parser.parse_args()

    with open(args.source_file) as f:
        to_encode = f.read().strip()
    print(compress(to_encode))


if __name__ == "__main__":
    main()
