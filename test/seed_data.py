import sqlite3
import time

conn = sqlite3.connect("test.db")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS films")             # 清掉刚才手玩的，从头来
cur.execute("""
CREATE TABLE films (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT, language TEXT, release_date TEXT, created_at TEXT
)
""")

films = [
    ("肖申克的救赎", "英语", "1994-09-23"),
    ("阿甘正传", "英语", "1994-07-06"),
    ("霸王别姬", "汉语", "1993-01-01"),
    ("龙猫", "日语", "1988-04-16"),
    ("天空之城", "日语", "1986-08-02"),
    ("天堂电影院", "意大利语", "1988-11-17"),
    ("泰坦尼克号", "英语", "1997-12-19"),
    ("楚门的世界", "英语", "1998-06-05"),
    ("花样年华", "汉语", "2000-09-29"),
    ("千与千寻", "日语", "2001-07-20"),
    ("无间道", "汉语", "2002-12-12"),
    ("盗梦空间", "英语", "2010-07-16"),
    ("让子弹飞", "汉语", "2010-12-16"),
    ("少年派的奇幻漂流", "英语", "2012-11-21"),
    ("星际穿越", "英语", "2014-11-07"),
    ("疯狂动物城", "英语", "2016-03-04"),
    ("你的名字", "日语", "2016-08-26"),
    ("摔跤吧！爸爸", "印地语", "2016-12-23"),
    ("燃烧", "韩语", "2018-05-17"),
    ("寄生虫", "韩语", "2019-05-30"),
    ("' OR '1'='1", "英语", "2020-01-01"),      # 疯狂导演的“怪片名”
    ("奥德赛", "英语", "2026-07-17"),
    ("牛来", "汉语", "2026-08-05"),
    ("欢迎来龙餐馆", "汉语", "2026-08-11"),
]
for i, (title, language, release_date) in enumerate(films, 1):
    cur.execute(
        "INSERT INTO films (title, language, release_date, created_at) "
        "VALUES (?, ?, ?, datetime('now'))",           # created_at 取此刻的时间
        [title, language, release_date],
    )
    print(f"已灌入 {i}/{len(films)}：{title}")
    time.sleep(1)                                       # 歇 1 秒再插下一部，好让每部的入库时间错开
conn.commit()
print("完成")
