 # Julia
 
 Julia can be helpful for varrious scientific computing tasks. It is easy to write (similar to python) but is compiled JIT by the LLVM compiler which results in the code being super fast. Generally this is helpful. Things like loops which are horribly slow in python (and therefore we do special tricks to avoid) generally are very fast in native julia code with no special tricks. Writing loops is a natural way to think about solving a problem with code, so this is helpful especially in scientific applicaitons where we often iterate over items (potentially a lot of items) to solve a problem. 
 
 ## Enviroment Isolation
 
 * More documentation on Julia env's can be found here. https://pkgdocs.julialang.org/v1/environments/
 * go to a folder, start julia, go to the package manager `]`, then call 
 ```
 activate .
 readdir()
 ```
 * To use an existing project folder, you also call `activate .`
 * To start julia in the env then calle
 ```
 julia --project=.
 ```
 which will start julia in the `.` folder (current folder)


## Workflow

There are various workflows which might work, but this one that I found helpful. 

* Edit your code in the an IDE (like VScode with the julia extension)
* Run the julia REPL (sort of like a shell)
* Everytime you want to run your code again do `include('myfile.jl')` to run it. 
* This prevents restarting your julia instance which often times requires re-compiling a lot of code. 
* The slowest part of julia is at startup when things are loaded and precompiled. So want to avoid this. 


## Helpful hints
* read the current dir (like `ls`) with  `readdir()` 
