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
"""