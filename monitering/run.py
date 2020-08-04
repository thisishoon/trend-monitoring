import threading
from collect import collect_ranking


def run():
    interval_second = 600
    timer = threading.Timer(interval_second, run)
    timer.start()
    collect_ranking()


if __name__ == '__main__':
    run()
