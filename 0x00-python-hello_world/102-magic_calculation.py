#!/usr/bin/python3
import dis

def magic_calculation(a, b):
    return 98 + (a ** b)

code_obj = magic_calculation.__code__
bytecode = dis.Bytecode(code_obj)
line_numbers = dict(dis.findlinestarts(code_obj))

for instr in bytecode:
    line_number = line_numbers.get(instr.offset, '')
    print(f"{line_number:2} {instr.offset:2} {instr.opname:20}{instr.argrepr}")