

from cx_Freeze import setup, Executable

# Collecting information "metadata" for the .exe setup
nameOfExec = input("Name for Executable: ")
versionNumber = input("Version: ")
auth = input("Name of Author: ")
auth_email = input("Email of Author: ")
descript = input("Description: ")
filename = input("File to Compile(Add .py to file): ")

# Real action happens here
# Using setup() function to build the executable file
setup(
    name = nameOfExec,
    version = versionNumber,
    description = descript, 
    author = auth,
    author_email = auth_email,
    executables = [Executable(filename)]
    )

# Remember
# file must be saved in same directory as the file you want to Compile
# Download cx_Freeze from source forge or run easy_install in power shell

# Instructions to use ->
# run this file in shell/cmd as "python CompileFiles.py build" or "python CompileFiles.py build_exe"
# Enter necessary information and the .exe file will be built!

# Note: This setup in minimialistic
