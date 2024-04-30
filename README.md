# werdl/4bit
## Features
- Custom 4-bit ALU, supporting AND, OR, XOR, NOT, full add and full subtract
- 256 nibbles of general use memory
- Four registers, used for I/O to/from the ALU
- Program counter with jump and jump if zero instructions
## Instruction Set
| Binary Value | Assembly Mnemonic | `A_ARG` value | `B_ARG` value | Operation Description | Implemented |
|-             |-                  |-               |-              | -                     | -         |
|`0000`| `ADD` | None | None | Adds reg 00 to reg 01 and stores in reg 10 | ✅ |
|`0001`| `SUB` | None | None | Subtracts reg 01 from reg 00 and stores in reg 10 | ✅ |
|`0010`| `REG` | 4 bit literal | 2 bit register address | Stores `A_ARG` in reg `B_ARG`| ✅ |
|`0011`| `NOP` | None | None | None | ✅ |
|`0100`| `NOT` | None | None | Logically inverts the contents of reg 00 and stores in reg 10 | ✅ |
|`0101`| `XOR` | None | None | Performs logical XOR on registers 00 and 01 and stores in reg 10 | ✅ |
|`0110`| `OR` | None | None | Performs logical OR on registers 00 and 01 and stores in reg 10 | ✅ |
|`0111`| `AND` | None | None | Performs logical AND on registers 00 and 01 and stores in reg 10 | ✅ |
|`1000`| `SAV` | 8 bit address | 4 bit literal | Saves `B_ARG` to memory address `B_ARG`| ✅ |
|`1001`| `LDA` | 8 bit address | 2 bit register address | Loads memory address `A_ARG` to reg `B_ARG`| ✅ |
|`1010`| `WRIT` | 8 bit address | 2 bit register address | Saves reg `B_ARG` to memory address `A_ARG` | ✅ |
| `1011`| Reserved | - | - | - | ❌ |
| `1100`| `JMP` | 6 bit address | None | Jumps to PC address `A_ARG`| ❌ |
| `1101`| `JZ` | 6 bit address | 2 bit register address | If `B_ARG` is zero, jumps to memory address `A_ARG`| ❌ |
| `1101`| Reserved | - | - | -| ❌ |
| `1111`| Reserved | - | - | -| ❌ |
### Notes on the instruction set
- There are 4 "namespaces" (bitfields)

| `Binary range` | `Use` | `# uses`
|-|-| - |
| `0000` - `0011` | Arithmetic uses | 2 + `NOP`
| `0100` - `0111` | Logical operations | 4
| `1000` - `1011` | Memory manipulation operations | 3
| `1100` - `1111` | Control flow operations | 2 (none implemented)
