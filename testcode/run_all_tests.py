import sys
import os
import unittest

# Add parent directory to path to import from app.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def run_all_tests():
    """Run all test modules"""
    print("=" * 70)
    print("RUNNING ALL TESTS FOR app.py")
    print("=" * 70)
    print()
    
    # Import and run test modules
    try:
        from test_core_functions import test_quaternion, test_cube_simulator, test_cube, test_cube_states
        from test_activity_cases import test_activity_cases, test_sequence_parsing
        
        print("1. Running core functionality tests...")
        print("-" * 50)
        test_quaternion()
        test_cube_simulator()
        test_cube()
        test_cube_states()
        
        print("2. Running activity case tests...")
        print("-" * 50)
        test_activity_cases()
        test_sequence_parsing()

        print("3. Running unit/system/acceptance unittest suites...")
        print("-" * 50)
        loader = unittest.TestLoader()
        suite = unittest.TestSuite()
        suite.addTests(loader.discover(os.path.dirname(os.path.abspath(__file__)), pattern="test_unit_*.py"))
        suite.addTests(loader.discover(os.path.join(os.path.dirname(os.path.abspath(__file__)), "system"), pattern="test_system_*.py"))
        suite.addTests(loader.discover(os.path.join(os.path.dirname(os.path.abspath(__file__)), "acceptance"), pattern="test_acceptance_*.py"))
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        if not result.wasSuccessful():
            sys.exit(1)
        
        print("=" * 70)
        print("🎉 ALL TESTS PASSED SUCCESSFULLY!")
        print("app.py is working correctly!")
        print("=" * 70)
        
    except Exception as e:
        print("=" * 70)
        print(f"❌ TEST FAILED WITH ERROR:")
        print(f"{e}")
        print("=" * 70)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    run_all_tests()
