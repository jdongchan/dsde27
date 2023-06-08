from datetime import date, datetime, timedelta

# date : 날짜
print(date.today())
today = date.today()
today_year = today.year
today_month = today.month
today_day = today.day
print(f'{today_year}년 {today_month}월 {today_day}일')

# datetime : 날짜 + 시간
print(datetime.now())

now = datetime.now()
now_year = now.year
now_month = now.month
now_day = now.day

time = now.time()
hour = time.hour
minute = time.minute
second = time.second
microsec = time.microsecond
print(f'{now_year}년 {now_month}월 {now_day}일 {hour}시 {second}초 {microsec}밀리초')

# timedelta : 날짜계산
print(today)
print(today + timedelta(days=2))
print(today + timedelta(days=-3))
print(today + timedelta(days=7))
print(today + timedelta(weeks=3))

print(now)
print(now + timedelta(hours=7))
print(now + timedelta(minutes=20))
