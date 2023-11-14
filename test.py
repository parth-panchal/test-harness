import subprocess
import os


def run_test(prog, name):
    input_file = f"test/{prog}.{name}.in"
    expected_output_file = f"test/{prog}.{name}.out"
    with open(input_file, "r") as infile:
        result = subprocess.run(
            ["python3", f"prog/{prog}.py"],
            input=infile.read(),
            text=True,
            capture_output=True,
        )
        with open(expected_output_file, "r") as expected_out:
            assert result.stdout == expected_out.read()


# Run tests for each program
run_test("wc", "testcase1")
run_test("gron", "testcase1")
