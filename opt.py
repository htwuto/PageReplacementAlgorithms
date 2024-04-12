def opt(reference_string, frames):
    result_matrix = [['' for _ in range(frames)] for _ in range(len(reference_string))]
    fault_count = 0
    page = [9999] * frames
    opt = [0] * len(reference_string)

    for i in range(frames):
        page[i] = 9999

    for i in range(len(reference_string)):
        hit = 0
        for j in range(frames):
            if page[j] == reference_string[i]:
                hit = 1
                break

        if hit == 0:
            for j in range(frames):
                page_get = page[j]
                for index in range(i, len(reference_string)):
                    if page_get == reference_string[index]:
                        opt[j] = index
                        cap = 1
                        break
                    else:
                        cap = 0
                if cap == 0:
                    opt[j] = 9999

            maximum = -9999
            for j in range(frames):
                if opt[j] > maximum:
                    maximum = opt[j]
                    repeat = j

            page[repeat] = reference_string[i]
            fault_count += 1

            for j in range(frames):
                if page[j] != 9999:
                    result_matrix[i][j] = page[j]
        else:
            for j in range(frames):
                result_matrix[i][j] = ''

    return result_matrix, fault_count
