from datetime import datetime, timedelta

def time_compare(timestr):
    timethread = datetime.strptime(timestr, '%Y-%m-%d %H:%M')
    timenow = datetime.now()
    diff = timenow-timethread
    if(diff>timedelta(days=7)):
        return False
    return True