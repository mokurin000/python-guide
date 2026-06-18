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
    answer_mode=False,
) -> (
    str | tuple[bool, str | None, str, str]
):  # skip reason | succeed, actual, expected, reason
    assert sys.executable, "Frozen module unsupported"

    answer_path = src_file.parent / "answer" / src_file.name
    if answer_mode and answer_path.exists():
        src_file = answer_path

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
    verbose_mode = "-v" in sys.argv or "--verbose" in sys.argv
    answer_mode = "-a" in sys.argv or "--answer" in sys.argv

    skip_count = 0
    succ_count = 0
    fail_count = 0

    for test_file in glob.iglob(pathname="**/*.py", root_dir=SRC_BASE_DIR):
        src = SRC_BASE_DIR / test_file

        input_files = sorted(src.parent.glob(f"in/{src.stem}.in*"))
        if not input_files:
            skip_count += 1
            if verbose_mode:
                print(f"Skipped {src}: no testcase available", file=sys.stderr)

        print(f"Testing {src}...", file=sys.stderr)

        for case_num, input_file in enumerate(input_files, start=1):
            output_file = src.parent.joinpath("out").joinpath(
                input_file.name.replace(".in", ".out", 1)
            )

            test_result = testcase_helper(
                src,
                input_file,
                output_file,
                answer_mode=answer_mode,
            )

            if isinstance(test_result, str):
                reason = test_result

                skip_count += 1
                if verbose_mode:
                    print(f"Skipped Case {case_num}: {reason}", file=sys.stderr)

                continue

            print(f"Case {case_num}: ", file=sys.stderr, end="")

            succ, actual, expected, reason = test_result
            succ_count += succ
            fail_count += not succ
            if succ:
                print("Passed.", file=sys.stderr)
            else:
                print(f"Failed: {reason}", file=sys.stderr)
                if actual:
                    print(f"Actual:\n{actual}", file=sys.stderr)
                    print(f"Expect:\n{expected}", file=sys.stderr)

    print(f"Skipped {skip_count} tests.", file=sys.stderr)

    print(
        f"Passed tests: {succ_count} ({succ_count / (succ_count + fail_count) * 100:.1f}%)"
    )
    print(
        f"Failed tests: {fail_count} ({fail_count / (succ_count + fail_count) * 100:.1f}%)"
    )


if __name__ == "__main__":
    main()
