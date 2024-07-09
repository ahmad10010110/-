def merge_overlapping_intervals(intervals):
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    merged_intervals = [sorted_intervals[0]]
    for interval in sorted_intervals:

        if merged_intervals[-1][1] >= interval[0]:
          merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
        else:
          merged_intervals.append(interval)

    return merged_intervals


array = [[8,10],[1,3],[2,6]]
print(merge_overlapping_intervals(array))
