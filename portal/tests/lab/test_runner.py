import unittest
import json
import importlib
import os

MODULE_PATH = 'portal.utils.lab.'
# Get the directory where this test file is located
TEST_DIR = os.path.dirname(__file__)
PROBLEMS = os.path.join(TEST_DIR, 'problems.json')

class LabTests(unittest.TestCase):
    """Test case for lab problems using problems.json"""

    def test_all_problems(self):
        """Test all problems from problems.json"""
        with open(PROBLEMS, 'r') as f:
            problems = json.load(f)
        
        for problem in problems:
            with self.subTest(problem=problem['func']):
                func_name = problem['func']
                args = problem['args']
                expected = problem['expected']
                
                # Import the specific module containing the function
                module_name = f"{MODULE_PATH}{func_name}"
                try:
                    module = importlib.import_module(module_name)
                    func = getattr(module, func_name, None)
                    if func is None:
                        self.skipTest(f"Function {func_name} not found in module {module_name}")
                except ImportError as e:
                    self.skipTest(f"Module {module_name} not found: {e}")
                    continue
                
                try:
                    # Run the function with args
                    result = json.loads(json.dumps(func(*args)))
                    print('------------------', result, '-------------', expected)
                    # Assert the result matches expected
                    self.assertEqual(result, expected,
                                   f"Function {func_name} with args {args} returned {result}, expected {expected}")
                except Exception as e:
                    self.fail(f"Function {func_name} with args {args} raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()
