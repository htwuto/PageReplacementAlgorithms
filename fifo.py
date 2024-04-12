def fifo(reference_string, frames):
    result_matrix = [['' for _ in range(frames)] for _ in range(len(reference_string))]
    fault_count = 0
    page = [9999] * frames
    queue = []
    for i in range(frames):
        page[i] = 9999

    for i in range(len(reference_string)):
        hit = 0
        for j in range(frames):
            if page[j] == reference_string[i]:
                hit = 1
                break

        if hit == 0:
            for count in range(frames - 1):
                if len(queue) == frames:
                    page[page.index(queue.pop(0))] = 9999

            for index in range(frames):
                if page[index] == 9999:
                    page[index] = reference_string[i]
                    queue.append(page[index])
                    break

            fault_count += 1
            for j in range(frames):
                if page[j] != 9999:
                    result_matrix[i][j] = page[j]
        else:
            for j in range(frames):
                result_matrix[i][j] = ''

    return result_matrix, fault_count
