from datetime import datetime, date, timezone, timedelta



JST = timezone(timedelta(hours=9))


def today() -> date:
    return datetime.now(JST).date()

def today_iso() -> str:
    return today().isoformat()

def today_jp() -> str:
    return today().strftime("%Y年 %-m月 %-d日")