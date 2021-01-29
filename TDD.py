"""
RED > GREEN > REFACTOR


Levels of Testing:
- Unit Testing - testing at the function level
- Component Testing - Testing at the library and cimpiled binary level
- System Testing - Tests the external interfaces of a system which is a collection of sub-systems
- Performance Testing - Testing done at sub-system an system levels to verif timing and resource usages are acceptable

SPECIFICS:
- Test individual functions
- A test should be written for each test case for a function (all positive and negative test cases).
- Groups of tests can be combined into test suites for better organization.
- Executes in the development environment rather than the production environment.
- Execution on the test should be automated.


UnitTest steps:
1.Setup - Create the test variables
2.Action - Perform the action on the test variables
3.Assert - Test validate the source of your actions.


Unit tests should RUN FAST!


*** What is Test Driven Development ?
- A process where the developer takes personal responsibility for the quality of their code.
- Unit tests are written before the production code.
- Don't write all the test or production code at once.
- Tests and production code are both written together in small bits of functionality.

Benefits of TDD?
- Gives you confidence to change the code.
- Gives you immediate feedback.
- Documents what the code is doing.
- Drives good object oriented design.

Uncle BOB 3 laws of TDD:
1. You may not write any production code until you have written a failing unit test.
2. You may not write more of a unit test than is sufficient to fail, and not compiling is failing.
3. You may not write more production code than is sufficient to pass the currently failing unit test.


Test Discovery:
- Pytest will automatically discover tests when you execute base on a standard naming convention.
- Test functions should include "test" at the beginning of the function name.
- Classes with tests in them should have "Test" at the beginning of the class name and not have an "__init__" method.
- Filenames of test modules should start or end with "test".(i.e. test_example.py or example_test.py).

Test Fixtures Scope
- Test Fixtures can have the following four different scopes which specially how often the fixture will be called:
    - Function - Run the fixture once for each test
    - Class - Run the fixture once for each class of tests
    - Module - Run once when the module goes in scope
    - Session - The fixture is run when pytest starts.

Test Fixture Return Objects and Params
- Test Fixtures can optionally return data which can be used in the test.
- The optional "params" array argument in the fixture decorator can be used to specify the data returned to the test.
- When a "params" argument is specified then the test will be called one time with each value specified.

Using the assert Statement
- Pytest allows the use of the built in python assert statement for performing verifications in the unit test.
- Comparison on all the python data types can be performed using the standard comparison operators:
    <, >, <=, >=, ==, and !=
- Pytest expands on the message returned from assert failures to provide more context in the test results.

Comparing Floating point Values
- Validating floating point values can sometimes be difficult as internally the value is binary fractions
    (i.e. 1/3 is internally 0.33333333...)
- Because of this some floating point comparisons that would be expected to pass fail.
- The pytest "approx" functions can be used to verify that two floating point values are "approximately" equivalent
to each other with the default tolerance of 1e-6.

Verifying Exceptions
- In some cases we want to verify tha a function throws an exception under certain conditions.
- Pytest provides the "raises" helper to perform this verification using the "with" keyword.
- If the specified exception is not raised in the code block pointed after the "raises" line then the test fails.


Pytest Command line arguments:
- By default Pytest will automatically discover and run all tests in all properly named modules from the current working
directory and sub directories.
- There are several command line arguments for controlling which discovered tests actually are executed.
    * moduleName - Simply specify the module name to run only the tests in that module.
    * DirectoryName/ - Runs any tests found in the specified directory.
    * -k "expression" - Matches tests found that match the evaluatable expression in the string. The string values can
    * include module, class and function names (i.e. "TestClass and TestFunction").
    * -m "expression" - Matches tests found that have a "pytest.mark" decorator that matches the specified expression.
    * -v: Report in verbose mode.
    * -q: Run in quiet mode(can be helpful when running hundreds or thousands of tests at once.)
    * -s: Don't capture console output(show print statements on the console.)
    * --ignore: ignore the specified path when discovering tests.
    * --maxfail: Stop  after the specified number of failures.

"""