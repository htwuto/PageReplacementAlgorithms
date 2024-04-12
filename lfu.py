def lfu(reference_string, frames):
    result_matrix = [['' for _ in range(frames)] for _ in range(len(reference_string))]
    fault_count = 0
    page = [9999] * frames
    cnt = [0] * frames
    bn = 0

    for i in range(len(reference_string)):
        hit = 0
        for j in range(frames):
            if page[j] == reference_string[i]:
                hit = 1
                cnt[j] += 1
                break

        if hit != 0:
            for j in range(frames):
                result_matrix[i][j] = ''
        else:
            fault_count += 1
            if bn < frames:
                page[bn] = reference_string[i]
                cnt[bn] += 1
                bn += 1
            else:
                least = 9999
                for j in range(frames):
                    if cnt[j] < least:
                        least = cnt[j]
                        rp = j

                page[rp] = reference_string[i]
                cnt2 = 0

                for j in range(i + 1):
                    if reference_string[i] == reference_string[j]:
                        cnt2 += 1

                cnt[rp] = cnt2

            for j in range(frames):
                if page[j] != 9999:
                    result_matrix[i][j] = page[j]

    return result_matrix, fault_count
