from .models import employee, schedule
import datetime
from collections import defaultdict, deque
from itertools import accumulate


def StringToDatetime(date, times, bg, en) -> datetime:
    """
    ポストパラメータをdatetime型にへんけいする
    """
    year, month, day = map(int, date.split("/"))
    if not bg <= datetime.date(year, month, day) <= en:
        print("WORNG term")
        return False
    times = times.split("-")
    times = [list(map(int, times[i].split(":"))) for i in range(2)]

    if not (0 <= times[0][0] <= 23 and 0 <= times[1][0] <= 23):
        print("WORNG hour")
        return False
    if not (0 <= times[0][1] <= 59 and 0 <= times[1][1] <= 59):
        print("WORNG minute")
        return False

    castedTime = []
    for i in range(2):
        tmp = datetime.datetime(
            year, month, day, hour=times[i][0], minute=times[i][1])
        castedTime.append(tmp)

    if castedTime[1] <= castedTime[0]:
        print("WORNG order")
        return False

    return castedTime


def preSubmit(_id, _dates, bg, en, _terms=1) -> list:
    """
    submitクエリの補助関数
    各情報を分解して型変換する
    """
    _dates = deque(_dates.split())
    # if int(_terms) * 2 != len(_dates):
    #     print(_terms, len(_dates))
    #     return False
    date_times = []
    for _ in range(int(_terms)):
        date = _dates.popleft()
        times = _dates.popleft()
        united_date = StringToDatetime(date, times, bg, en)
        if united_date:
            date_times.append(united_date)
        else:
            return False
    return [_id, _terms, date_times]


def preCancel(_id, _date, bg, en) -> list:
    """
    cancelクエリの補助関数
    各情報を分解して型変換する
    """
    date_times = []
    date, times = _date.split()
    united_date = StringToDatetime(date, times, bg, en)
    if united_date:
        date_times.append(united_date)
    else:
        return False
    return [_id, date_times]


def preProcess(lines) -> dict:
    """
    標準入力やファイルから受け取った
    クエリを先回りして処理する
    """
    queue = deque(lines)
    Y, A, B, D, K, T = 2021, 1, 1, 300, 10, 1
    whole_dates = [datetime.date(Y, A, B) +
                   datetime.timedelta(days=i) for i in range(D)]
    bg, en = whole_dates[0], whole_dates[-1]
    queries = []
    for i in range(T):
        Qtype = queue.popleft()
        _id = queue.popleft()
        if Qtype == "submit":
            # _terms = queue.popleft()
            _dates = queue.popleft()
            subquery = preSubmit(_id, _dates, bg, en)
        elif Qtype == "cancel":
            _date = queue.popleft()
            subquery = preCancel(_id, _date, bg, en)
        elif Qtype == "check":
            subquery = [_id]
        elif Qtype == "calculate":
            subquery = [_id]
        queries.append({'type': Qtype, 'sub': subquery})
    return whole_dates, K, queries


class StoreShift():
    """
    シフト管理と給料計算システム

    メソッド：
    1. Submit(シフト提出)
    2. Cancel(シフト削除)
    3. Check(シフト確認)
    4. Calculate(給料計算)
    """

    def __init__(self, K, TERM, w=900, night=1.2):
        self.employee = defaultdict(dict)
        self.dates = {str(day.month) + "/" + str(day.day): [] for day in TERM}
        self.K = K
        self.w = w
        self.wnight = int(w * night)

    def query_process(self, q):
        if q['type'] == "submit":
            return self.Submit(q)
        elif q['type'] == "cancel":
            return self.Cancel(q)
        elif q['type'] == "check":
            return self.Check(q)
        elif q['type'] == "calculate":
            return self.Calculate(q)
        else:
            print(q['type'])
            return "クエリが正しくありません"

    def Submit(self, q):
        if not q['sub']:
            return "wrong format"

        _id, S, job_dates = q['sub']

        if not employee.objects.filter(name=_id):
            e = employee(name=_id)
            e.save()

        # 出願ごとの処理
        for jdate in job_dates:
            st, en = jdate[0], jdate[1]
            key_day = datetime.date(
                jdate[0].year, jdate[0].month, jdate[0].day)
            print(schedule.getTodayShift(key_day))
            # # TODO K人以上の処理
            # base = st.hour * 60 + st.minute
            # imos = [0 for _ in range(en.hour * 60 + en.minute + 1 - base)]
            # # TODO 8時間以内
            # max_time = datetime.timedelta(hours=8, minutes=0)
            # 当日のシフト
            # new_datas = []
            # for tg_data in schedule.getTodayShift(key_day):
            #     if st <= tg_data[1] < en:
            #         imos[tg_data[1].hour*60 + tg_data[1].minute - base] += 1
            #     if st <= tg_data[2] < en:
            #         imos[tg_data[2].hour*60 +
            #                 tg_data[2].minute - base + 1] -= 1
            #     new_datas.append(tg_data)

            # # 保存処理
            # imos = accumulate(imos)
            # flg = True
            # for num in imos:
            #     if num >= self.K:
            #         # K人以上のときはその時間帯の出願を無視する
            #         flg = False
            # del imos
            # if en - st >= max_time:
            #     en = st + max_time
            # if flg:
            e = employee.objects.get(name=_id)
            s = schedule(emp=e, date=key_day,
                         start_at=datetime.time(st.hour, st.minute), end_at=datetime.time(en.hour, en.minute))
            s.save()
        return "accepted"

    def Cancel(self, q):
        if not q['sub']:
            return "wrong format"

        _id, jdate = q['sub']
        if not self.employee[_id]["schedule"]:
            return 'no schedule'

        flg = False
        for date in jdate:
            st, en = date[0], date[1]
            key_day = str(st.month) + "/" + str(st.day)
            still_work = 0
            new_dates = []
            for tg_data in self.dates[key_day]:
                if tg_data[0] == _id:
                    # その日の予定ごと消す
                    # TODO 指定された時間帯だけ消して、あとは残す
                    if (st <= tg_data[1] <= en or st <= tg_data[2] <= en):
                        flg = True
                        still_work -= 1
                    else:
                        still_work += 1
                        new_dates.append(tg_data)
                else:
                    new_dates.append(tg_data)
        # 予定を見つけて正しく消せたら完了
        if flg:
            self.dates[key_day] = new_dates
            if still_work <= 0:
                self.employee[_id]["schedule"].remove(
                    datetime.date(2021, st.month, st.day)
                )
            print("deleted")
        else:
            print("wrong schedule")

    def Check(self, q):
        _id = q['sub'][0]
        try:
            S = len(self.employee[_id]["schedule"])
            _str = ""
            for date in sorted(list(self.employee[_id]["schedule"])):
                _str += str(date.month) + "/" + str(date.day) + " "
            _str = _str.rstrip()
        except KeyError:
            S = 0
            _str = ""

        print(S)
        print(_str)

    def Calculate(self, q):
        oc4 = datetime.timedelta(hours=4)
        oc22 = datetime.timedelta(hours=22)
        _id = q['sub'][0]
        # 日勤時間と夜勤時間
        DayDelta = datetime.timedelta(hours=0, minutes=0)
        NightDelta = datetime.timedelta(hours=0, minutes=0)
        for day in self.employee[_id]["schedule"]:
            key_day = str(day.month) + "/" + str(day.day)
            for tg_data in self.dates[key_day]:
                if tg_data[0] == _id:
                    st = datetime.timedelta(
                        hours=tg_data[1].hour, minutes=tg_data[1].minute)
                    en = datetime.timedelta(
                        hours=tg_data[2].hour, minutes=tg_data[2].minute)
                    if st <= oc4 <= en:
                        DayDelta += oc4 - st
                        NightDelta += en - oc4
                    elif st <= oc22 <= en:
                        DayDelta += oc22 - st
                        NightDelta += en - oc22
                    elif oc4 <= st <= oc22:
                        DayDelta += en - st
                    else:
                        NightDelta += en - st
        # 特別手当、日勤、夜勤の順に足す
        Y = 10000 if DayDelta.total_seconds() + NightDelta.total_seconds() >= 40*3600 else 0
        Y += (DayDelta.total_seconds()//3600)*self.w
        Y += (NightDelta.total_seconds()//3600)*self.wnight
        print(int(Y))


def main(lines):
    # print(lines)
    TERM, K, queries = preProcess(lines)
    shift = StoreShift(K, TERM)

    for q in queries:
        shift.query_process(q)


if __name__ == '__main__':
    lines = []
    with open(r'C:\Users\heste\OneDrive - Kyushu University\python\Atcoder\ignore\3.txt') as f:
        for line in f.readlines():
            lines.append(line.rstrip('\r\n'))
    main(lines)
