# Test Harness Project

##Author
Parth Panchal, [ppanchal1@stevens.edu](mailto:ppanchal1@stevens.edu)

## GitHub Repository

[github.com/parth-panchal/test-harness](https://github.com/parth-panchal/test-harness)

## Time Spent

I estimate that I spent approximately 48 hours on this project.

## Description

This project is a test harness for testing the functionality of three different programs: `wc.py`, `gron.py`, and `csv_sum.py`. The test harness runs each program on various inputs, compares the output with expected results, and reports the test results.

## Testing Approach

The test harness follows a simple approach:

1. It looks for test files (`PROG.NAME.in`) in the `test/` directory.
2. For each test, it runs the program with input from STDIN and compares the output with the expected output (`PROG.NAME.out`).
3. If the output matches the expected output, the test is marked as passed. Otherwise, the test is marked as failed.

## Known Issues

- None at the moment.

## Difficult Issue Resolution

One challenging issue I encountered was figuring out how to test with command line arguments. I still couldn't figure out the exact way to do it, so I ended up hard-coding the arguments to the testing calls for the files.

## Implemented Extensions

1. **`wc` for multiple files**

   - The `wc.py` program now supports processing multiple files and provides a total count at the end.
   - Example: `wc.py file1.txt file2.txt`
   - Example Output:

   ```
    10      20     150 file1.txt
    15      25     180 file2.txt
    25      45     330 total

   ```

2. **`wc` flags to control output**

   - The `wc.py` program now supports flags to control the information shown (`-l` for lines, `-w` for words, `-c` for characters).
   - Users can combine flags to customize the output.
   - Example: `wc.py -lwc file.txt`
   - Example Output:

   ```
         10      20     150 file.txt
   ```

3. **Controlling the base object name in `gron`:**

- The `gron.py` program introduces a `--obj` flag to specify a different base object name.
  - Example: `gron.py --obj o example.json`
  - Example Output:
    ```
    o = {};
    o.menu = {};
    o.menu.id = "file"
    o.menu.value = "File"
    o.menu.popup = {};
    o.menu.popup.menuitem = [];
    o.menu.popup.menuitem[0] = {};
    o.menu.popup.menuitem[0].value = "New"
    o.menu.popup.menuitem[0].onclick = "CreateNewDoc()"
    o.menu.popup.menuitem[1] = {};
    o.menu.popup.menuitem[1].value = "Open"
    o.menu.popup.menuitem[1].onclick = "OpenDoc()"
    o.menu.popup.menuitem[2] = {};
    o.menu.popup.menuitem[2].value = "Close"
    o.menu.popup.menuitem[2].onclick = "CloseDoc()"
    ```
