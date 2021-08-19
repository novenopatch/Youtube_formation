from cx_Freeze import setup, Executable 
# On appelle la fonction setup 
setup(
  name = "salut",    
  version = "0.1",    
  description = "Ce programme vous dit bonjour",    
  executables = [Executable("test_f.py")], 
)
