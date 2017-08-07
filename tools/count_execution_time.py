
def count_exec_time(func_name, *args):
	tmp = [i for i in args]
	t1 = datetime.now().microsecond
	func_name(*tmp)
	time_took = datetime.now().microsecond - t1
	return round(time_took, 5)
	
# Measures algorithm execution time micro seconds
# Use:
# from count_execution_time import count_exectime
# result = count_exectime(function_name, arg1, arg2, argN) 
# print(str(result) +  " microsecond")
# # simple isn't it but useful!

# Source of script: https://github.com/AsciiKay/Beginners-Python-Examples/blob/master/count_algorithm_execution_time.py
