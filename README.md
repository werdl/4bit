# 4bit
> A 4 bit computer built with logic gates in Logisim.
## Features
- [x] 256 nibbles of primary memory
- [x] 4 bit ALU
- [x] control unit
- [x] CPU cycle
    - [x] fetch
    - [x] decode
    - [x] execute
- [ ] conditional jumps
- [ ] lcd display (will be implemented in a similar manner to VGA, with a framebuffer in RAM)
    - [x] display for calculation result / content of a memory address
- [ ] stack
- [ ] interrupts and input
## How will programs get flashed to the computer?
- Programs will be written in assembly
- Then assembled by a simple Arduino (Nano) program
- The Arduino will then flash the program to the computer
## Opening the project
- Open Logisim (evolution, I haven't tested it with the original)
- Open the 4bit.circ file
- Enjoy!
- If you are interested in contributing, please drop me a line at [`werdl_@outlook.com`](mailto:werdl_@outlook.com)
