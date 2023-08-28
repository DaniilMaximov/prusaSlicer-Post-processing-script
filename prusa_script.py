import sys

input_filename = sys.argv[1]
output_filename = sys.argv[1]

with open(input_filename, 'r') as input_file:
    gcode_lines = input_file.read()
    modified_gcode_lines = gcode_lines.replace("G1 E.7 F1500 ;  ; unretract", "G1 E3.3 F1500 ;  ; unretract\nG92 E.7", 1)

with open(output_filename, 'w') as output_file:
    output_file.writelines(modified_gcode_lines)
