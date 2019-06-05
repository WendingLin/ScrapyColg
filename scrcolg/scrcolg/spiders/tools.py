from datetime import datetime, timedelta
import pandas as pd

def time_compare(timestr):
    timethread = datetime.strptime(timestr, '%Y-%m-%d %H:%M')
    timenow = datetime.now()
    diff = timenow-timethread
    if(diff>timedelta(days=7)):
        return False
    return True

def get_page_url(page_elemet, base_url):
    return base_url + page_elemet


def clean_string(dirty_string):

    if "本帖最后由" in dirty_string and "编辑" in dirty_string:
        pos1 = dirty_string.find("编辑")
        dirty_string = dirty_string[pos1+2:]
    if "发表于" in dirty_string:
        pos1 = dirty_string.find("发表于")
        pos2 = pos1+18
        while(dirty_string[pos2:pos2+1].isdigit()):
            pos2+=1
        dirty_string = dirty_string[pos2:]
    if "登录/注册后可看大图" in dirty_string or "guestviewthumb" in dirty_string:
        dirty_string = ""
    return dirty_string.replace('\r', '').replace('\n','')


def get_hour(timestr):
    time = datetime.strptime(timestr, '%Y-%m-%d %H:%M')
    return time.hour

def map_add(info, map):
    if not info in map:
        map[info] = 1
    else:
        map[info] += 1

def sortmap(map):
    return sorted(map.items(),key=lambda x:x[1],reverse=True)


def write_map_to_csv(map, filename):
    key_list = list(map.keys())
    value_list = list(map.values())
    dataframe = pd.DataFrame({'name': key_list, 'value': value_list})
    dataframe.to_csv(filename, index=False, sep=',')