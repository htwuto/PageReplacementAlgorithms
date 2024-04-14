def mru(reference_string, frames):
    result_matrix = [[[] for _ in range(frames)] for _ in range(len(reference_string))]
    fault_count = 0
    cap = 0
    repeat = 0

    page = [9999] * frames
    mru = [0] * frames

    for i in range(len(reference_string)):
        hit = 0
        for j in range(frames):
            if page[j] == reference_string[i]:
                hit = 1
                break

        if hit == 0:
            for j in range(frames):
                page_get = page[j]
                for index in range(i - 1, -1, -1):
                    if page_get == reference_string[index]:
                        mru[j] = index
                        cap = 1
                        break
                    else:
                        cap = 0
                if cap == 0:
                    mru[j] = 9999
            maximum = -9999
            for j in range(frames):
                if mru[j] > maximum:
                    maximum = mru[j]
                    repeat = j
            page[repeat] = reference_string[i]
            fault_count += 1
            for j in range(frames):
                if page[j] != 9999:
                    result_matrix[i][j] = page[j]
                else:
                    result_matrix[i][j] = ''
        else:
            for j in range(frames):
                result_matrix[i][j] = ''
    return result_matrix, fault_count
