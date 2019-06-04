from datetime import datetime, timedelta

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