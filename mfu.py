from collections import defaultdict


def mfu(reference_string, frames):
    result_matrix = [['' for _ in range(frames)] for _ in range(len(reference_string))]
    fault_count = 0
    page = [9999] * frames
    map_cnt = defaultdict(lambda: 0)
    rp = 0
    queue = []

    for i in range(len(reference_string)):
        hit = 0
        for j in range(frames):
            if page[j] == reference_string[i]:
                hit = 1
                break

        if hit != 0:
            for j in range(frames):
                result_matrix[i][j] = ''

        else:
            fault_count += 1
            most = -9999
            old = 9999
            if 9999 in page:
                page[rp] = reference_string[i]
                rp += 1
            else:
                for j in range(frames):
                    if map_cnt[page[j]] >= most and map_cnt[page[j]] != 0:
                        most = map_cnt[page[j]]
                        old = queue.index(page[j])
                        rp = j
                    elif map_cnt[page[j]] == most and queue.index(page[j]) < old:
                        most = map_cnt[page[j]]
                        old = queue.index(page[j])
                        rp = j
                page[rp] = reference_string[i]

            for j in range(frames):
                if page[j] != 9999:
                    result_matrix[i][j] = page[j]

        map_cnt[reference_string[i]] += 1
        if reference_string[i] not in queue:
            queue.append(reference_string[i])
        else:
            queue.pop(queue.index(reference_string[i]))
            queue.append(reference_string[i])

    return result_matrix, fault_count
