def utc_date_start_timeinISO(year,month,day):
    return datetime.utcfromtimestamp(datetime(year, month, day, 0, 0).timestamp()).isoformat() + 'Z'

def utc_date_end_timeinISO(year, month, day):
    return datetime.utcfromtimestamp(datetime(year, month, day, 23, 59).timestamp()).isoformat() + 'Z'

def date_from_ymd(year, month, day):
    return datetime(year, month, day)

def date_in_file():
    with open("tasks_list.txt", 'r') as b:
            k = b.readlines()
    b = k[1].replace('\n', '').split(',')
    c = [int(i) for i in b]
    return c

def list_of_grouped_tasks():
    with open("tasks_list.txt", 'r') as b:
        k = b.readlines()[2:]
    l = []
    curr = []
    for i in k:
        if i == '\n':
            l.append(curr)
            curr = []
        else:
            if i is not '' or ' ':
                m = i.replace('\n','').split('.')
                p = m[1].replace(' ','')
                n = m[0].split('>')
                curr.append([int(n[1][0]),p])
    if curr != []:
        l.append(curr)
    return l

def time_add(start_time, weight):
    b = start_time
    m = datetime.fromisoformat(b)
    if weight == 1:
        return (m + timedelta(minutes = 11)).isoformat()
    elif weight == 2:
        return (m + timedelta(minutes = 22)).isoformat()
    elif weight == 'Break':
        return (m + timedelta(minutes = 2)).isoformat()
    else:
        print('Unknow time add')

def one_task(event,task, start_time,serv, cal, timezone):
    task = task[0][1]
    today = start_time
    break_start1 = today.isoformat()
    break_end1 = (today + timedelta(minutes=2)).isoformat()

    break_start2 = (today + timedelta(minutes=47)).isoformat()
    break_end2 = (today+ timedelta(minutes = 50)).isoformat()

    start = (today + timedelta(minutes=2)).isoformat()
    end = (today + timedelta(minutes=47)).isoformat()
    insert_event(task,start,end, serv, '45', cal, timezone)
    insert_event('Break', break_start1, break_end1, serv, 'b2', cal, timezone)
    insert_event('Break', break_start2, break_end2, serv , 'b3', cal, timezone)


def two_tasks(event, tasks, start_time, serv, cal, timezone):
    tasks = [i[1] for i in tasks]
    today = start_time
    #Breaks(2)
    break_start1 = today.isoformat()
    break_end1 = (today + timedelta(minutes=2)).isoformat()
    break_start2 = (today + timedelta(minutes=48)).isoformat()
    break_end2 = (today+ timedelta(minutes = 50)).isoformat()

    start1 = (today + timedelta(minutes=2)).isoformat()
    end1 = (today + timedelta(minutes=24)).isoformat()
    start2 = (today + timedelta(minutes=26)).isoformat()
    end2 = (today+ timedelta(minutes = 48)).isoformat()
    insert_event(tasks[0], start1, end1, serv, '22-22', cal, timezone)
    insert_event(tasks[1], start2, end2, serv, '22-22', cal, timezone)
    insert_event('Break', end1, start2, serv, 'b2', cal, timezone)
    insert_event('Break', break_start1, break_end1, serv, 'b2', cal, timezone)
    insert_event('Break', break_start2, break_end2, serv , 'b2', cal, timezone)

def task_description(weight):
    if weight == 4:
        return '45'
    elif weight == 2:
        return '22-22'
    elif weight == 1:
        return '11-11'
    else:
        return ':)'

def three_tasks(event, tasks, start_time, serv, cal, timezone):
    today = start_time

    break_start1 = today.isoformat()
    break_end1 = time_add(break_start1, 'Break')
    insert_event('Break', break_start1, break_end1, serv, 'b2', cal, timezone)

    start1 = break_end1
    end1 = time_add(start1, tasks[0][0])
    insert_event(tasks[0][1], start1, end1, serv, task_description(tasks[0][0]), cal, timezone)

    break_start2 = end1
    break_end2 = time_add(break_start2, 'Break')
    insert_event('Break', break_start2, break_end2, serv, 'b2' , cal, timezone)

    start2 = break_end2
    end2 = time_add(start2, tasks[1][0])
    insert_event(tasks[1][1], start2, end2, serv, task_description(tasks[1][0]), cal, timezone)

    break_start3 = end2
    break_end3 = time_add(break_start3, 'Break')
    insert_event('Break', break_start3, break_end3, serv, 'b2' , cal, timezone)

    start3 = break_end3
    end3 = time_add(start3, tasks[2][0])
    insert_event(tasks[2][1], start3, end3, serv, task_description(tasks[2][0]), cal, timezone)


def four_tasks(event, tasks, start_time, serv, cal, timezone):
    tasks = [i[1] for i in tasks]
    today = start_time
    start1 = today.isoformat()
    end1 = (today + timedelta(minutes=11)).isoformat()


    start2 = (today + timedelta(minutes=13)).isoformat()
    end2 = (today+ timedelta(minutes = 24)).isoformat()


    start3 = (today + timedelta(minutes = 26)).isoformat()
    end3 = (today + timedelta(minutes=37)).isoformat()

    start4 = (today + timedelta(minutes=39)).isoformat()
    end4 = (today+ timedelta(minutes = 50)).isoformat()
    insert_event(tasks[0], start1, end1, serv, '11-11', cal, timezone)

    insert_event('Break', end1, start2, serv, 'b2', cal, timezone)

    insert_event(tasks[1], start2, end2, serv, '11-11', cal, timezone)

    insert_event('Break', end2, start3, serv, 'b2', cal, timezone)

    insert_event(tasks[2], start3, end3, serv, '11-11', cal, timezone)

    insert_event('Break', end3, start4, serv, 'b2', cal, timezone)

    insert_event(tasks[3], start4, end4, serv, '11-11', cal, timezone)

def incomplete_tasks(event, tasks, start_time, serv, cal, timezone):
    Today = start_time.isoformat()
    for i in tasks:
        break_start1 = Today
        break_end1 = time_add(break_start1, 'Break')
        insert_event('Break', break_start1, break_end1, serv, 'b2' , cal, timezone)

        start1 = break_end1
        end1 = time_add(start1, i[0])
        insert_event(i[1], start1, end1, serv, task_description(i[0]), cal, timezone)
        Today = end1

#DUMMY
def insert_eventD(task, startTime, endTime,serv, description = ''):
    print("created dummy event: " + task)


#input your email here
def insert_event(task, startTime, endTime,serv, cal_ID, timeZone, description = ''):
    event_result = serv.events().insert(calendarId=cal_ID,
           body={
               "summary": task,
               "description": description,
               "start": {"dateTime": startTime, "timeZone": timeZone},
               "end": {"dateTime": endTime, "timeZone": timeZone},
           }
        ).execute()
    print("created event")
    print("summary: ", event_result['summary'])

def is_scheduled(tasks):
    b = False
    for i in tasks:
        if '*' in i[1]:
            b = True
    return b

def unscheduled_tasks(list_of_tasks):
    return [i for i in list_of_tasks if not is_scheduled(i)]

def scheduled_tasks(list_of_tasks):
    return [i for i in list_of_tasks if is_scheduled(i)]

def new_tasks_list(scheduled_T, unscheduled_T, N):
    k = unscheduled_T
    if len(k)-1 < N:
        N = len(k)
    for i in range(N):
        k[i][0][1] += '*'
    return scheduled_T + k


def list_of_time_blocks(cal):
    year = date_in_file()[0]
    month = date_in_file()[1]
    day = date_in_file()[2]
    service = get_calendar_service()
    # Call the Calendar API
    #now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    now = utc_date_start_timeinISO(year, month, day)
    dayEnd = utc_date_end_timeinISO(year, month, day)
    print('Getting list of time blocks')
    events_result = service.events().list(
       calendarId=cal, timeMin=now, timeMax=dayEnd,
       maxResults=12, singleEvents=True,
       orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
       print('No upcoming events found.')
    count = 1
    for event in events:
       start = event['start'].get('dateTime', event['start'].get('date'))
       try:
           print('block ' + str(count) + ' ',start, event['summary'])
       except KeyError:
           print('block ' + str(count) + ' ',start)
       except:
           print("Unexpected error:", sys.exc_info()[0])
           raise
       count += 1
    return events

def full_weight(Tasks):
    return 4 == sum([i[0] for i in Tasks])

def create_events(timeBlocks, tasksList, calendar, time_zone):
    service = get_calendar_service()
    count = 0
    notcounted = True
    for i in timeBlocks:
        if count < len(tasksList):
            print('#############')
            tasks = tasksList[count]
            date_inFile = date_in_file()
            d = date_from_ymd(date_inFile[0], date_inFile[1], date_inFile[2])
            today = datetime(d.year, d.month, d.day, int(i['start']['dateTime'][11:][:2]), int(i['start']['dateTime'][14:][:2]))
            if full_weight(tasks):
                if len(tasks) == 1:
                    one_task(i, tasks, today, service, calendar,time_zone)
                elif len(tasks) == 2:
                    two_tasks(i, tasks, today, service, calendar, time_zone)
                elif len(tasks) == 3:
                    three_tasks(i, tasks, today, service, calendar, time_zone)
                elif len(tasks) == 4:
                    four_tasks(i, tasks, today, service, calendar, time_zone)
                else:
                    pass
            else:
                incomplete_tasks(i, tasks, today, service, calendar, time_zone)

            if notcounted:
                count += 1
                notcounted = False
            print('###########\n')
            notcounted = True
            time.sleep(3)

def hours_vs_events(events, tasks):
    if len(events) == len(tasks):
        print('Calendar Events equals Task hours, Great! :)')
    elif len(events) < len(tasks):
        print('You have ' + str(len(events)) + ' calendar hours and the tasks take ' + str(len(tasks)) + ' hours.')
        print(':( You need ' + str(len(tasks) - len(events)) + ' more calendar hours.')
    else:
        print('You have ' + str(len(events)) + ' calendar hours and the tasks take ' + str(len(tasks)) + ' hours.')
        print(':( You need ' + str(len(events) - len(tasks)) + ' more task hours.')

def write_tasks_to_file(my_tasks):
    with open("tasks_list.txt", "r") as m:
        first_lines_2 = m.readlines()[0:2]

    with open("tasks_list.txt", "w") as my_file:
        my_file.writelines(first_lines_2)
        k = 1
        j = 1
        space = ''
        for i in my_tasks:
            if k > 9:
                space = ' '
            if len(i) == 1:
                my_file.writelines(str(k) + '---->' + str(i[0][0]) + '<----->'+ str(j)+ '. ' + i[0][1] + '\n\n')

                k += 1
                j += 1

            elif len(i) == 2:
                h = str(k) + '---->' + str(i[0][0]) + '<----->'+ str(j)+ '. ' \
                + i[0][1] + '\n ' + space + '---->' + str(i[1][0]) + '<----->'+ str(j + 1) + '. ' \
                + i[1][1] + '\n\n'
                my_file.writelines(h)
                k += 1
                j += 2

            if len(i) == 3:
                h = str(k) + '---->' + str(i[0][0]) + '<----->'+ str(j)+ '. ' \
                + i[0][1] + '\n ' + space + '---->' + str(i[1][0]) + '<----->'+ str(j + 1) + '. ' \
                + i[1][1] + '\n ' + space + '---->' + str(i[2][0]) + '<----->'+ str(j + 2)+ '. ' \
                + i[2][1] + '\n\n'
                my_file.writelines(h)
                k += 1
                j += 3

            elif len(i) == 4:
                h = str(k) + '---->' + str(i[0][0]) + '<----->'+ str(j)+ '. ' \
                + i[0][1] + '\n ' + space + '---->' + str(i[1][0]) + '<----->'+ str(j + 1) + '. ' \
                + i[1][1] + '\n ' + space + '---->' + str(i[2][0]) + '<----->'+ str(j + 2)+ '. ' \
                + i[2][1] + '\n ' + space + '---->' + str(i[3][0]) + '<----->'+ str(j + 3) + '. ' \
                + i[3][1] + '\n\n'
                my_file.writelines(h)
                k += 1
                j += 4
        print('Rewriting tasks done!\n')




if __name__ == "__main__":
    from cal_setup import get_calendar_service
    from datetime import datetime, timedelta
    import os
    import sys
    import time
    import copy
    import config
    stubs_calendar = config.calendar_IDs['stubs']
    schedule_calendar = config.calendar_IDs['schedule']
    mytimeZone = config.time_Zone
    undecided = True
    while undecided:
        time_blocks = list_of_time_blocks(stubs_calendar)
        all_Tasks = list_of_grouped_tasks()
        scheduled_Tasks = scheduled_tasks(all_Tasks)
        unscheduled_Tasks = unscheduled_tasks(all_Tasks)
        m = copy.deepcopy(unscheduled_Tasks)
        new_Task_list = new_tasks_list(scheduled_Tasks, m, len(time_blocks))
        if len(time_blocks) == 0:
            k = input('You have 0 time blocks. Please select some time blocks and then press 1, or exit by pressing 2.(1/2)\n')
            if k == '2':
                undecided = False
        else:
            hours_vs_events(time_blocks, unscheduled_Tasks)
            k = input('Would you like to schedule tasks?(y/n)\n')
            if k == 'y':
                create_events(time_blocks, unscheduled_Tasks, schedule_calendar, mytimeZone)
                write_tasks_to_file(new_Task_list)
                undecided = False
            elif k == 'n':
                k = input('Would you like to exit?(y/n)\n')
                if k == 'y':
                    undecided = False
                if k == 'n':
                    pass
            else:
                print('Invalid input. Try again\n')
