from core.managers import TestManager

def grade():
    # run student code
    passed_case1 = True
    
    test_case1 = TestManager.new_test(score = 10)
    if passed_case1:
        test_case1.pass_test()
    else:
        test_case1.fail_test()