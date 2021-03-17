def appearance(intervals: dict) -> int:
    lesson_sec = set(range(intervals['lesson'][0], intervals['lesson'][1]))
    tutor_sec = [
      set(range(intervals['tutor'][i], intervals['tutor'][i+1] + 1)) \
        for i in range(0, len(intervals['tutor']), 2)
    ]
    pupil_sec = [
      set(range(intervals['pupil'][i], intervals['pupil'][i+1] + 1)) \
        for i in range(0, len(intervals['pupil']), 2)
      ]
    result_seconds = len(
      lesson_sec.intersection(set.union(*tutor_sec), set.union(*pupil_sec))
    )
    return result_seconds


if __name__ == '__main__':
    print(appearance({ 
      'lesson': [1594663200, 1594666800], 
      'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472], 
      'tutor': [1594663290, 1594663430, 1594663443, 1594666473] 
    }
    ))
