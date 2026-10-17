times = '1h 45m,360s,25m,30m 120s,2h 60s'
times = times.replace(' ',',')
times = times.split(',')
minutes=0
for time in times:
    if 'h' in time:
        minutes += int(time.replace('h',''))*60
    elif 's' in time:
        minutes += int(time.replace('s',''))//60
    else:
        minutes += int(time.replace('m',''))    
print(minutes)
