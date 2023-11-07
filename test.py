# test.py
import subprocess
import os


def run_test(prog, name):
    input_file = f"test/{prog}.{name}.in"
    expected_output_file = f"test/{prog}.{name}.out"
    expected_status_file = f"test/{prog}.{name}.status"

    with open(input_file, "r") as infile:
        # Run the program on STDIN
        result = subprocess.run(
            ["python", f"prog/{prog}.py"],
            input=infile.read(),
            text=True,
            capture_output=True,
        )

        # Compare STDOUT with expected output
        with open(expected_output_file, "r") as expected_out:
            assert result.stdout == expected_out.read()

        # Compare exit status with expected status
        with open(expected_status_file, "r") as expected_status:
            assert result.returncode == int(expected_status.read())


# Run tests for each program
run_test("wc", "testcase1")
run_test("gron", "testcase1")
# run_test("yourchoice", "testcase3")
