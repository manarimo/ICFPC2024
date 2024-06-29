import sys
from urllib.request import urlopen, Request
import argparse


def communicate(body: str) -> str:
    request = Request(
        method="POST",
        url="https://boundvariable.space/communicate",
        headers={
            'Authorization': 'Bearer 88befdee-f76d-427d-a63f-12238452ce65'
        },
        data=body.encode(encoding="ascii")
    )
    with urlopen(request) as response:
        response_data: bytes = response.read()
        return response_data.decode(encoding="ascii")


ORDER = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`|~ \n"
ENCODE_MAP = {c: i for i, c in enumerate(ORDER)}


def encode_string(s: str) -> str:
    return "S" + ''.join([chr(ENCODE_MAP[c] + 33) for c in s])


def decode_string(s: str) -> str:
    if s[0] != "S":
        raise ValueError(f"ICFP string is expected, but received: `{s}`")
    return ''.join(ORDER[ord(c) - 33] for c in s[1:])


def decode_integer(s: str) -> int:
    if s[0] != "I":
        raise ValueError(f"ICFP integer is expected, but received: `{s}`")
    value = 0
    for c in s[1:]:
        value = value * 94 + ord(c) - 33
    return value


def repl():
    while True:
        command = input("> ").strip()
        response = communicate(encode_string(command))
        print(decode_string(response))


def getset(command: str, args):
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="file input")
    parser.add_argument("-d", "--direct", help="direct input")
    parser.add_argument("-s", "--string-output", action="store_true", help="interpret response as a string")

    args = parser.parse_args(args)
    if args.file is not None:
        with open(args.file) as f:
            input = f.read().strip()
    elif args.direct is not None:
        input = args.direct
    else:
        raise ValueError("either -f or -d must be specified.")

    if command == "send":
        response = communicate(encode_string(input))
    elif command == "eval":
        code = f"B. {encode_string('echo ')} " + input
        response = communicate(code)

    if args.string_output:
        response = decode_string(response)
    print(response)


def main():
    command = sys.argv[1:]
    command_name, args = command[0], command[1:]
    if command_name == "repl":
        repl()
    elif command_name in ["eval", "send"]:
        getset(command_name, args)
    else:
        print(f"unknown command: {command_name}")


if __name__ == "__main__":
    main()
