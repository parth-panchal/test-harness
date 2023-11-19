import subprocess
import os
import sys


def run_test(prog, name, args):
    input_file = f"test/{prog}.{name}.in"
    arg_expected_output_file = f"test/{prog}.{name}.arg.out"
    # Run the program with input as a command-line argument
    cmd = ["python3", f"prog/{prog}.py", input_file]
    if args:
        cmd.append(args)
    result = subprocess.run(
        cmd,
        text=True,
        capture_output=True,
    )
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
    for filename in os.listdir("test"):
        if filename.endswith(".in"):
            if filename.startswith("wc"):
                prog, name = filename.split(".", 1)
                if name == "testcase1.in":
                    success = run_test(prog, name.rstrip(".in"), "")
                    if not success:
                        failed_tests += 1
                if name == "testcase2.in":
                    success = run_test(prog, name.rstrip(".in"), "-l")
                    if not success:
                        failed_tests += 1
                if name == "testcase3.in":
                    success = run_test(prog, name.rstrip(".in"), "-wc")
                    if not success:
                        failed_tests += 1
            if filename.startswith("gron"):
                prog, name = filename.split(".", 1)
                if name == "testcase1.in":
                    success = run_test(prog, name.rstrip(".in"), "")
                    if not success:
                        failed_tests += 1
                if name == "testcase2.in":
                    success = run_test(prog, name.rstrip(".in"), "")
                    if not success:
                        failed_tests += 1
                if name == "testcase3.in":
                    success = run_test(prog, name.rstrip(".in"), "--obj o")
                    if not success:
                        failed_tests += 1
            if filename.startswith("csv_sum"):
                if name == "testcase1.in":
                    success = run_test(prog, name.rstrip(".in"), "Age Salary")
                    if not success:
                        failed_tests += 1
                if name == "testcase2.in":
                    success = run_test(prog, name.rstrip(".in"), "Age")
                    if not success:
                        failed_tests += 1
                if name == "testcase3.in":
                    success = run_test(prog, name.rstrip(".in"), "Salary")
                    if not success:
                        failed_tests += 1
                prog, name = filename.split(".", 1)
                success = run_test(prog, name.rstrip(".in"), "")
                if not success:
                    failed_tests += 1
    print(f"\nfailed tests: {failed_tests}")
    if failed_tests > 0:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
