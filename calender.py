
inp = 2344
years = inp // 365

leap_year = years // 4

remaining_days = inp - leap_year
year, m = divmod(remaining_days, 365)
month, w = divmod(m, 30)
week, d = divmod(w, 7)
days = d

print(f'{year} year {month} month {week} week {days} days')

# print(year)
# print(month)
# print(week)
# print(days)

