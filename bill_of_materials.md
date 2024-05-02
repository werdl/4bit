# List of materials 
> This is a non-exhaustive list of materials that are used in the construction of the TTL computer. 

## ICs
> All 7400 series ICs, DIP package
- x33 `7408` (quad 2-input AND)
- x10 `7400` (quad 2-input NAND)
- x14 `7432` (quad 2-input OR)
- x1 `7486` (quad 2-input XOR)
- x3 `7421` (dual 4-input AND)
- x2 `74283` (4-bit binary full adder)
- x1 `7411` (triple 3-input AND)
- x1 `7436` (quad 2-input XOR)
- x2 `744072` (dual 4 input OR) 
- x2 `747266` (quad 2-input XNOR, low availability, so could be replaced with `7436` (quad 2-input XOR) and `7400` (quad 2-input NAND, with inputs shorted))

## RAM chips
- x3 `64B x 8` SRAM chips (program memory)
- x1 `256B x 4` SRAM chip (general use memory)
- x4 `4B` SRAM chips (registers), probably constructed manually from `7474` (dual D flip-flop) chips, eight of them which would be used to make the four registers

## Other
- x1 `556` (dual timer, one of which offset by 1/2 period, to operate the `TTL_PC` `CLK` and `GO` signals respectively)
- Somewhere in the order of 500 wires, for breadboarding
- x24 switches, for input (some of which could be replaced with the `556` timer, but would still be present for manual input)
- x53 LEDS (4 for each register, 20 for current instruction, 8 for current memory address, 5 for ALU output, 4 for selected register, and possibly more for debugging)
- A series of large breadboards, for construction

## Useful tools
- A breadboard power supply - probably 5V
- A multimeter (probably a digital one, for ease of use)
- A logic probe
- A soldering iron (optional, but recommended for a more permanent build)
- A wire stripper
- An Arduino or similar, for testing, debugging, and uploading/running programs