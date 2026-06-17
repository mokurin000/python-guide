import sys
import glob
import subprocess
from pathlib import Path

SRC_BASE_DIR = Path(__file__).parent.joinpath("exercise")

INPUT_MISSING = "input file was missing"
OUTPUT_MISSING = "output file was missing"
UNIMPLMENTED = "exercise unimplemented"


def testcase_helper(
    src_file: Path,
    input_file: Path,
    output_file: Path,
) -> (
    str | tuple[bool, str | None, str, str]
):  # skip reason | succeed, actual, expected, reason
    assert sys.executable, "Frozen module unsupported"

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            inputs = f.read()
    except FileNotFoundError:
        return INPUT_MISSING
    try:
        with open(output_file, "r", encoding="utf-8") as f:
            expected_outputs = f.read()
    except FileNotFoundError:
        return OUTPUT_MISSING

    proc = subprocess.run(
        args=[
            sys.executable,
            "-X",
            "utf8",
            src_file,
        ],
        input=inputs,
        capture_output=True,
        check=False,
        encoding="utf-8",
    )

    if "NotImplementedError" in proc.stderr:
        return UNIMPLMENTED
    actual = proc.stdout.strip()
    return (
        expected_outputs.strip() == proc.stdout.strip(),
        actual,
        expected_outputs,
        "Output mismatched!",
    )


def main():
    skip_count = 0

    for test_file in glob.iglob(pathname="**/*.py", root_dir=SRC_BASE_DIR):
        src = SRC_BASE_DIR / test_file

        for input_file in sorted(src.parent.glob(f"{src.stem}.in*")):
            output_file = input_file.with_name(
                input_file.name.replace(".in", ".out", 1)
            )

            test_result = testcase_helper(src, input_file, output_file)

            if isinstance(test_result, str):
                reason = test_result

                skip_count += 1
                if "-v" in sys.argv or "--verbose" in sys.argv:
                    print(f"Skipped {input_file}: {reason}", file=sys.stderr)

                if reason == UNIMPLMENTED:
                    break
                else:
                    continue

            print(f"Testing {input_file}... ", file=sys.stderr, end="")

            succ, actual, expected, reason = test_result
            if succ:
                print("Passed.", file=sys.stderr)
            else:
                print(f"Failed: {reason}", file=sys.stderr)
                if actual:
                    print(f"Actual:\n{actual}", file=sys.stderr)
                    print(f"Expect:\n{expected}", file=sys.stderr)

    print(f"Skipped {skip_count} tests.", file=sys.stderr)


if __name__ == "__main__":
    main()
