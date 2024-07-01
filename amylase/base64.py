import itertools
import argparse
import sys

try:
    sys.set_int_max_str_digits(100000)
except:
    pass


def compress(to_encode: str) -> str:
    chars = "LRDU"
    unit_size = 1
    candidate_units = []

    indices = []
    for i in range(0, len(to_encode), unit_size):
        raw = to_encode[i: i + unit_size]
        if len(raw) < unit_size:
            raw += "L" * (unit_size - len(raw))
        if raw not in candidate_units:
            candidate_units.append(raw)
        for v, unit in enumerate(candidate_units):
            if unit[: len(raw)] == raw:
                indices.append(v)
                break
       
    zahyo_assyuku = {v: i for i, v in enumerate(set(indices))}
    zahyo_tenkai = {i: v for v, i in zahyo_assyuku.items()}

    units = [candidate_units[zahyo_tenkai[i]] for i in range(len(zahyo_assyuku))]
    indices = [zahyo_assyuku[v] for v in indices]
    base = len(units)

    assert ''.join([units[v] for v in indices])[:len(to_encode)] == to_encode
    encoded = base
    for v in reversed(indices):
        encoded = encoded * base + v

    table = ''.join(units)

    source_code = f"""\
-- base64 format: [encoded: ICFP string] [prefix: ICFP integer]
-- encoded string is decoded to LRDU string and then first prefix characters are taken

-- Pass the encoded string
B$

-- Make the recursive function of Decode
B$
  Lf B$ vf vf
  -- Decode :: Self -> String -> String
  -- Decodes the first entry in the source then recursively process the rest.
  Ld Ls
    ? ( B= vs @I{base} )
      S
      B.
        BT @I{unit_size} BD (B* @I{unit_size} B% vs @I{base}) @S{table} -- Decode the first entry
        (B$ B$ vd vd (B/ vs @I{base})) -- Process the rest

-- Encoded string
@I{encoded}
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
