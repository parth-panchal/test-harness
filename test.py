import subprocess
import os
import sys


def run_test(prog, name):
    input_file = f"test/{prog}.{name}.in"
    arg_expected_output_file = f"test/{prog}.{name}.arg.out"

    # Run the program with input as a command-line argument
    result = subprocess.run(
        ["python3", f"prog/{prog}.py", input_file],
        text=True,
        capture_output=True,
    )

    # Check for expected output from command-line argument
    if os.path.exists(arg_expected_output_file):
        with open(arg_expected_output_file, "r") as expected_out:
            expected_output = expected_out.read()
            if result.stdout != expected_output:
                print(
                    f"FAIL: {prog} {name} failed in argument mode (TestResult.OutputMismatch)"
                )
                print("\texpected:\n")
                print(expected_output)
                print("\n")
                print("\tgot:\n")
                print(result.stdout)
                return False

    print(f"OK: {prog} {name}")
    return True


def main():
    failed_tests = 0
    output_mismatch_count = 0

    # Iterate over all files in the test directory
    for filename in os.listdir("test"):
        if filename.endswith(".in"):
            prog, name = filename.split(".", 1)
            success = run_test(prog, name.rstrip(".in"))
            if not success:
                failed_tests += 1
                if "OutputMismatch" in str(sys.exc_info()[1]):
                    output_mismatch_count += 1

    print(f"\noutput mismatch: {output_mismatch_count}")
    print(f"total: {failed_tests}")

    if failed_tests > 0:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
