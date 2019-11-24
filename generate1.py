import pandas as pd
import random


def isleap(y):
    year = y
    if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        return 1
    else:
        return 0


Data = pd.read_excel('MTV1.xlsx')
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
daysl = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month = list(Data.columns)
month = month[1:]
print(month)
writer = 'WeatherDATA1.csv'
c = 0
for i in Data['Year']:
    d1 = Data.loc[Data['Year'] == i]
    df1 = pd.DataFrame(columns=['Average', 'Minimum', 'Maximum', 'Date', 'Month', 'Year'])
    if(c == 0):
        df1.to_csv(writer, mode='a')
        c = c + 1
    if(isleap(int(i))):
        for j in range(0, len(daysl)):
            avg = int(d1[m1])
            for k in range(1, daysl[j] + 1):
                a = 0
                b = 0
                c = 0
                d = 0.1 * random.randint(0, 9) + 0.01 * random.randint(0, 9)
                e = 0.1 * random.randint(0, 9) + 0.01 * random.randint(0, 9)
                a = avg + (random.randint(-1, 4) + d)
                b = a + (random.randint(2, 5) + d)
                c = a + (random.randint(-4, -2) + e)
                df1.loc[len(df1)] = [a] + [c] + [b] + [k] + [j + 1] + [i]
        df1.to_csv(writer, mode='a', header=False)
    else:
        for j in range(0, len(days)):
            m1 = month[j]
            avg = int(d1[m1])
            for k in range(1, days[j] + 1):
                a = 0
                b = 0
                c = 0
                d = 0.1 * random.randint(0, 9) + 0.01 * random.randint(0, 9)
                e = 0.1 * random.randint(0, 9) + 0.01 * random.randint(0, 9)
                a = avg + (random.randint(-1, 4) + d)
                b = a + (random.randint(2, 5) + d)
                c = a + (random.randint(-4, -2) + e)
                df1.loc[len(df1)] = [a] + [c] + [b] + [k] + [j + 1] + [i]
        df1.to_csv(writer, mode='a', header=False)
