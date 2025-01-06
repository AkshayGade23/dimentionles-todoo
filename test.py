import unittest
import test_todo  

if __name__ == "__main__":
    
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(test_todo)

   
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

  
    print("\nTest Results Summary:")
    print(f"Tests Run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")

    if result.wasSuccessful():
        exit(0)  
    else:
        exit(1)  
