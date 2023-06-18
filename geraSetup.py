import cx_Freeze
executables =[
    cx_Freeze.Executable(script="main.py", icon="space.ico")
]
cx_Freeze.setup(
    name = "SPACE MARKER",
    options={
        "build_exe":{
            "packages":["pygame"],
            "include_files":["bg.jpg",
                            "space.png",
                            "space.png",
                            "Space_Machine_Power.mp3"]
        }
    }, executables = executables
)