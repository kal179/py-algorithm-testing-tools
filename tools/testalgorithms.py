

class TestFunction:
    def __init__(self, tests, func_name, expected_results, detail):
    	"""
	param -> tests, Is the container for list of tests provided for testing
	param -> func_name, Is the parameter is reference for function user want to test
	param -> expected_results, Is the parameter for list of expected results 
	param -> detail, Is the flag for detailed info of tests done
    	"""
        self.tests = tests
        self.compare = expected_results
        self.func_name = func_name
        self.flag = detail

    def test(self):
    	"""
	Pseudocode:
		checks if the given tests is a list or not
		if not a list then TypeError is raised
		if a list then,
		Check every test in that tests
		if test itself is not a list raise TypeError
		if test is a list then 
		get result of function for particular test
		if details are enabled give a detailed info about test performed
		if details are not enabled just determine weather test is passed or not
		
	Thats pretty much everything!
    	"""
        if isinstance(self.tests, list):
            for li in self.tests:
                if not(isinstance(li, list)):
                    raise TypeError("Each particualr test should be an list itself!\nTry again buddy!")

                else:
                    try:
                        case = self.func_name(*li)
                    except TypeError:
                        print("\nTest #{} has conflicts:\nThe number of args provided does not match the requirement of function\n".format(
                            self.tests.index(li) + 1))

                    if self.flag:
                        if case == self.compare[self.tests.index(li)]:
                            print("#{} Test {}, Expected {}:\n\tstatus => passed, result => {}\n".format(
                                self.tests.index(li) + 1, li, self.compare[self.tests.index(li)], case))
                        else:
                            print("#{} Test {}, Expected {}:\n\tstatus => falied, result => {}\n".format(
                                self.tests.index(li) + 1, li, self.compare[self.tests.index(li)], case))
                    else:
                        if case == self.compare[self.tests.index(li)]:
                            print("Test #{}: status => passed".format(self.tests.index(li) + 1))
                        else:
                            print("Test #{}: status => failed".format(self.tests.index(li) + 1))

        else:
            raise TypeError("The tests should be a list of individual test!")
  
