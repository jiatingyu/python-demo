from datetime import datetime, timedelta, timezone

# 获取当前日期和时间
now = datetime.now()
print(f"当前日期和时间: {now}")
dt = now.timestamp() # 把datetime转换为timestamp , timestamp是一个浮点数，整数位表示秒。
print(dt)

print(f'当地时区：{datetime.fromtimestamp(dt)}') # 要把timestamp转换为datetime
print(f'utc时区：{datetime.fromtimestamp(dt, timezone.utc)}') # 要把timestamp转换为datetime

# 增加日期
#timedelta(days=2, hours=12) # 2 天 12 小时
one_day = timedelta(days=1)
tomorrow = now + one_day
print(f"明天的日期: {tomorrow}")

# 格式化日期
formatted_date = now.strftime('%Y年%m月%d日 %H时%M分%S秒')
print(f"格式化的日期: {formatted_date}")

#字符串转时间
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
