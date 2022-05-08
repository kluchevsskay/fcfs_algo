def fcfs(positions, nums, way):
    # positions p0, p1, p2...
    # nums 1, 4, 6
    # way прямой (0) обратный (-1) оптимальный (1)

    lines = []  # строки из Гшек и Ишек
    g_count = 0  # скок Гшек ставить перед Ишками
    sum_g = 0
    if way == -1:
        positions = list(reversed(positions))
        nums = list(reversed(nums))

    elif way == 1:
        lib = {positions[i]: nums[i] for i in range(len(nums))}
        new_lib = dict(sorted(lib.items(), key=lambda x: x[1]))
        nums = list(new_lib.values())
        positions = list(new_lib.keys())

    notes = open("notes.txt", "w")
    for i in range(len(nums)):
        i_count = nums[i]
        line = 'Г' * g_count + 'И' * i_count
        lines.append(line)
        notes.write(positions[i] + ' ' + line + '\n')
        g_count += i_count

    for i in range(len(lines)):
        sum_g += lines[i].count('Г')
    res_1 = round(sum_g / len(nums), 2)
    res_2 = sum_g + len(lines[-1])
    res_3 = round(res_2 / len(nums), 2)
    return res_1, res_2, res_3


pos = ['p0', 'p1', 'p2', 'p3', 'p4', 'p5']
num = [3, 9, 3, 5, 3, 1]
way = 1
print('Ср время ожидания = ' + str(fcfs(pos, num, way)[0]), 'Полное время = ' + str(fcfs(pos, num, way)[1]),
      'Ср время выполнения = ' + str(fcfs(pos, num, way)[2]), sep='\n')
