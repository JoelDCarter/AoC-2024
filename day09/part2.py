import sys

if sys.version_info < (3, 7):
    print("Python 3.7 or higher is required for ordered dictionary behavior.")
    sys.exit(1)

with open('sample.txt', 'r', encoding='UTF-8') as file:
    disk_map = file.readline().rstrip()
    file_id = 0
    blocks = []
    used_blocks_map = {}
    free_blocks_map = {}
    for i in range(0, len(disk_map), 2):
        used_blocks_map[(file_id, len(blocks))] = int(disk_map[i])
        blocks += [file_id] * int(disk_map[i])
        if i + 1 < len(disk_map) and int(disk_map[i + 1]) > 0:
            free_blocks_map[len(blocks)] = int(disk_map[i + 1])
            blocks += [-1] * int(disk_map[i + 1])
        file_id += 1
    for block_info in reversed(used_blocks_map.keys()):
        file_id, block_position = block_info
        block_length = used_blocks_map[block_info]
        for free_block_position in sorted(free_blocks_map.keys()):
            free_block_length = free_blocks_map[free_block_position]
            if free_block_position < block_position and block_length <= free_block_length:                
                blocks[free_block_position:free_block_position + block_length] = blocks[block_position:block_position + block_length]
                del free_blocks_map[free_block_position]
                if free_block_length > block_length:
                    free_blocks_map[free_block_position + block_length] = free_block_length - block_length
                blocks[block_position:block_position + block_length] = [-1] * block_length
                break
    checksum = 0
    for i in range(len(blocks)):
        if blocks[i] > -1:
            checksum += i * blocks[i]
    print(checksum)
