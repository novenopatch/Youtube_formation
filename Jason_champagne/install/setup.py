from cx_Freeze import setup, Executable

setup(
    name = "MONSUper programme math",
    version = "0.1",
    description = " N'affiche rien juste un test",
    executables = [Executable("menu.py")]
)