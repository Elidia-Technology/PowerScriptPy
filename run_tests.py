#!/usr/bin/env python3
"""
PowerScript Test Suite Runner
Runs all .ps test files in the test_suits directory
"""

import os
import sys
import subprocess
from pathlib import Path

def main():
    # Get test directory
    test_dir = Path(__file__).parent / "test_suits"
    
    if not test_dir.exists():
        print(f"❌ Test directory not found: {test_dir}")
        return 1
    
    # Find all .ps test files
    test_files = sorted(test_dir.glob("test_*.ps"))
    
    if not test_files:
        print(f"❌ No test files found in {test_dir}")
        return 1
    
    print("╔════════════════════════════════════════════════════════╗")
    print("║     PowerScript Test Suite Runner                      ║")
    print("╚════════════════════════════════════════════════════════╝")
    print()
    print(f"Found {len(test_files)} test files")
    print()
    
    passed = 0
    failed = 0
    errors = []
    
    for test_file in test_files:
        test_name = test_file.stem
        print(f"Running {test_name}...", end=" ")
        
        try:
            # Run with tps command
            result = subprocess.run(
                ["tps", "run", str(test_file)],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode == 0:
                print("✅ PASSED")
                passed += 1
            else:
                print("❌ FAILED")
                failed += 1
                errors.append({
                    "test": test_name,
                    "stdout": result.stdout,
                    "stderr": result.stderr
                })
                
        except subprocess.TimeoutExpired:
            print("⏱️  TIMEOUT")
            failed += 1
            errors.append({
                "test": test_name,
                "error": "Test timed out after 10 seconds"
            })
        except FileNotFoundError:
            print("⚠️  TPS NOT FOUND")
            print()
            print("Please install PowerScript:")
            print("  python3 setup.py develop --user")
            print("or")
            print("  pip install -e .")
            return 1
        except Exception as e:
            print(f"⚠️  ERROR: {e}")
            failed += 1
            errors.append({
                "test": test_name,
                "error": str(e)
            })
    
    # Print summary
    print()
    print("╔════════════════════════════════════════════════════════╗")
    print("║                  Test Results                          ║")
    print("╠════════════════════════════════════════════════════════╣")
    print(f"║  Total Tests:  {len(test_files):3d}                                   ║")
    print(f"║  Passed:       {passed:3d}                                   ║")
    print(f"║  Failed:       {failed:3d}                                   ║")
    print("╚════════════════════════════════════════════════════════╝")
    print()
    
    # Print error details
    if errors:
        print("╔════════════════════════════════════════════════════════╗")
        print("║                  Error Details                         ║")
        print("╚════════════════════════════════════════════════════════╝")
        print()
        for error in errors:
            print(f"Test: {error['test']}")
            if 'error' in error:
                print(f"Error: {error['error']}")
            if 'stderr' in error and error['stderr']:
                print("STDERR:")
                print(error['stderr'][:500])
            if 'stdout' in error and error['stdout']:
                print("STDOUT:")
                print(error['stdout'][:500])
            print()
            print("-" * 60)
            print()
    
    # Final message
    if failed == 0:
        print("🎉 All tests passed successfully!")
        return 0
    else:
        print(f"⚠️  {failed} test(s) failed. Please review.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
