import sys
import glob
import subprocess
from pathlib import Path
from subprocess import CalledProcessError

SRC_BASE_DIR = Path(__file__).parent.joinpath("exercise")


def file_level_helper(
    src_file: str | Path,
) -> (
    str | tuple[bool, str | None, str, str]
):  # skip reason | succeed, actual, expected, reason
    assert sys.executable, "Frozen module unsupported"

    src = SRC_BASE_DIR / src_file
    input_file = src.with_suffix(suffix=".in")
    output_file = src.with_suffix(suffix=".out")

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            inputs = f.read()
    except FileNotFoundError:
        return "input file was missing"
    try:
        with open(output_file, "r", encoding="utf-8") as f:
            expected_outputs = f.read()
    except FileNotFoundError:
        return "output file was missing"

    try:
        proc = subprocess.run(
            args=[
                sys.executable,
                "-X",
                "utf8",
                src,
            ],
            input=inputs,
            capture_output=True,
            check=True,
            encoding="utf-8",
        )
    except CalledProcessError:
        return False, None, expected_outputs, "Program execution failed!"

    if "NotImplementedError" in proc.stderr:
        return "exercise unimplemented"
    actual = proc.stdout.strip()
    return (
        expected_outputs.strip() == proc.stdout.strip(),
        actual,
        expected_outputs,
        "Output mismatched!",
    )


def main():
    for test_file in glob.iglob(pathname="**/*.py", root_dir=SRC_BASE_DIR):
        print(f"Testing {test_file}... ", file=sys.stderr, end="")

        test_result = file_level_helper(test_file)

        if isinstance(test_result, str):
            print(f"Skipped: {test_result}", file=sys.stderr)
            continue

        succ, actual, expected, reason = test_result
        if succ:
            print("Passed.", file=sys.stderr)
        else:
            print(f"Failed: {reason}", file=sys.stderr)
            if actual:
                print(f"Actual:\n{actual}", file=sys.stderr)
                print(f"Expect:\n{expected}", file=sys.stderr)


if __name__ == "__main__":
    main()
