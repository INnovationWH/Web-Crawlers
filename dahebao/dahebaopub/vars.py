import time
class glovar():
    ndata = ""
    def set_ndata():
        global ndata
        ndata = time.strftime("%Y-%m/%d")
        return ndata
