
def prepare_for_display(course):
    course.times.sort(key=lambda time: (time['day'], time['starttime']))

    for time in course.times:
        # create human-readable day field
        if time['day'] == 1:
            time['day_human_readable'] = 'M'
        elif time['day'] == 2:
            time['day_human_readable'] = 'Tu'
        elif time['day'] == 3:
            time['day_human_readable'] = 'W'
        elif time['day'] == 4:
            time['day_human_readable'] = 'Th'
        elif time['day'] == 5:
            time['day_human_readable'] = 'F'
        else:
            time['day_human_readable'] = '?'

        # create human-readable time fields
        time['starttime_human_readable'] = '{}:{:02d}'.format(time['starttime'] // 60, time['starttime'] % 60)
        time['endtime_human_readable'] = '{}:{:02d}'.format(time['endtime'] // 60, time['endtime'] % 60)