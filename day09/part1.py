with open('sample.txt', 'r', encoding='UTF-8') as file:
    disk_map = file.readline().rstrip()
    file_id = 0
    blocks = []
    for i in range(0, len(disk_map), 2):
        blocks += [file_id] * int(disk_map[i])
        if i + 1 < len(disk_map):
            blocks += [-1] * int(disk_map[i + 1])
        file_id += 1
    free_blocks = blocks.count(-1)
    next_free_block = 0
    for i in range(len(blocks) - 1, 0, -1):
        if blocks[i] == -1:
            continue
        if not -1 in blocks[next_free_block + 1:i + 1]:
            break
        next_free_block = blocks.index(-1, next_free_block + 1, i)
        blocks[next_free_block] = blocks[i]
    blocks = blocks[:len(blocks) - free_blocks]
    checksum = 0
    for i in range(len(blocks)):
        checksum += i * blocks[i]
    print(checksum)
