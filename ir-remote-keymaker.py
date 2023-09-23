with open('demo.ir', 'w') as f:
    protocol = "NECext"
    address = "05 00 00 00"
    cmd_min = 0x4000
    cmd_max = 0x40FF

    f.write("Filetype: IR signals file\nVersion: 1\n")
    for i in range(cmd_min, cmd_max+1):
        cmd_hex_1 = hex(i % 256)[2:].zfill(2).upper()
        cmd_hex_2 = hex((i>>8) % 256)[2:].zfill(2).upper()
        cmd_hex_3 = hex((i>>16) % 256)[2:].zfill(2).upper()
        cmd_hex_4 = hex((i>>24) % 256)[2:].zfill(2).upper()
        cmd_str = f"#\nname: Cmd {cmd_hex_1} {cmd_hex_2} {cmd_hex_3} {cmd_hex_4}\n" \
                  "type: parsed\n" \
                  f"protocol: {protocol}\n" \
                  f"address: {address}\n" \
                  f"command: {cmd_hex_1} {cmd_hex_2} {cmd_hex_3} {cmd_hex_4}\n"
        f.write(cmd_str)
