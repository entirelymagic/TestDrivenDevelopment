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

Test Doubles:
- Almost all code depends (i.e. collaborates) with other parts of the system.
- Those other parts of the system are not always easy to replicate in the unit test environment
or would make tests slow if used directly.
- Test Doubles are objects that are used in unit tests as replacements of the real production system collaborators.

Types of Test Doubles
- Dummy *
    Objects that can be passed around as necessary but do not have any type of test implementation and shoould
    never be used.(Often generates exceptions if they are called)
- Fake
    * These objects  generally have a simplified functional implementation of a particular interface that is
    adequate for testing but not for production.
- Stubs
    * These objects provide implementations with canned answers that are suitable for the test.
- Spies
    * These objects provide implementations that record the values that were passed in so they can be used
    by the test.
- Mocks
    * These objects are pre-programmed to expect specific calls and parameters and can throw exceptions when
    necessary.

Mock Frameworks
- Most mock frameworks provide easy ways for automatically creating any of these types of test doubles AT RUNTIME.
- They provide a fast means for creating mocking expectations for your tests.
- They can be much more efficient that implementing custom mock object of your own creation.
- Creating mock objects by hand can be tedious and error prone.

unitest.mock
- Python Mockign Framework
- Built in to Python version 3.3 and newer
- Needs to be installed for older versions of Python with the command "pip install mock".

unittest.mock - Mock Class
- unittest.mock provides the mock class which can be used as a fake, stub, spy or true mock for all your tests.
- The Mock class has many initializations parameters for controlling its behavior.
- Once it has been called a Mock object has many buit-in functions for verifying how it was used.
- Mock provides many initialization parameters which can be used to control the mock objects behavior.
    * "spec" parameter specifies the interface that Mock object is implementing.
    * "side_effect" parameters specifies a function that should be called when the mock is called.
    * "return_value" parameter specifies the return value when the Mock is called.
            ! If "side_effect" parameter is set, it's return value is used instead.

Mock - Verification
- Mock provides many built-in functions for verifying how it was used such as following asserts:
    * assert_called- Assert the mock was called
    * assert_called_once - Assert the mock was called once.
    * assert_called_with - Will pass if the Assert was called with the specified parameters.
    * assert_called_once_with - Assert if the mock was called once with the specified parameters.
    * assert_any_call - Assert the mock was eer called with the specified parameters.
    * assert_not_called - Assert the mock was not called
    * assert_has_calls - Assert the mock was called with the list of calls(optionally in order)
    * called - A boolean value indicating if the mock was ever called.
    * call_count - An integer value representing the number of times the mock object was called.
    * call_args - The arguments the mock was last called with.
    * call_args_list - A list containing the arguments that wae used for each call to the mock.

unittest.mock - MagicMock Class
- MagicMock is derived from Mock and provides a default implementation of many of the default "magic"
methods defined for objects in Python(i.e. __str__)
- The following magic methods are not implemented by default in MagicMock:
    *, __del__, __getattr__, __setattr__, __init__, __new__, __prepare__, __instancecheck__, __subclasscheck__

Pytest Monkeypatch Test Ficture
- PyTest provides the monkeypatch text fixture to allow a test to dynamically replace:
     * module and class attributes
     * dictionary entries
     * environment variables
     
"""