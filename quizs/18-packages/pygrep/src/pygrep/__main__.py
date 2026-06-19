import sys
from .core import filter_lines, filter_lines_regex


def main() -> None:
    args = sys.argv[1:]

    use_regex = False
    if args and args[0] == "-r":
        use_regex = True
        args = args[1:]

    if len(args) < 1:
        print("用法: pygrep [-r] <pattern> [文件...]")
        print("       <命令> | pygrep [-r] <pattern>")
        sys.exit(1)

    pattern = args[0]
    filepaths = args[1:]

    if filepaths:
        for filepath in filepaths:
            try:
                with open(filepath, encoding="utf-8") as f:
                    lines = f.readlines()
            except FileNotFoundError:
                print(f"文件未找到: {filepath}", file=sys.stderr)
                continue

            if use_regex:
                matched = filter_lines_regex(pattern, lines)
            else:
                matched = filter_lines(pattern, lines)

            for line in matched:
                print(line, end="")
    else:
        lines = sys.stdin.readlines()
        if use_regex:
            matched = filter_lines_regex(pattern, lines)
        else:
            matched = filter_lines(pattern, lines)

        for line in matched:
            print(line, end="")


if __name__ == "__main__":
    main()
