import threading
from collect import collect_ranking
from esmodule import insert

def run():
    interval_second = 600
    timer = threading.Timer(interval_second, run)
    timer.start()
    dicts = collect_ranking()
    print(dicts)
    insert(dicts)



if __name__ == '__main__':
    run()
