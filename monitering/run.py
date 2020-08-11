import sys
import threading
from collect import collect_ranking
from esmodule import insert


def run(es_flag=True):
    interval_second = 600
    timer = threading.Timer(interval_second, run)
    timer.start()
    dicts = collect_ranking()

    print(dicts)
    if es_flag:
        insert(dicts)

    return dicts


if __name__ == '__main__':
    es_flag = True
    if sys.argv[0] == 2:
        es_flag = sys.argv[1]

    run(es_flag)
