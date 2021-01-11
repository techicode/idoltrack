import pandas as pd
import bar_chart_race as bcr

idol_youtube = ['Endo Hikari', 'Morita Hikaru', 'Onuma Akiho', 'Masumoto Kira', 'Seki Yumiko', 'Matsuda Rina',
                'Tamura Hono', 'Ozono Rei', 'Fujiyoshi Karin', 'Kosaka Marino', 'Inoue Rina', 'Takemoto Yui',
                'Moriya Rena', 'Yamasaki Ten', 'Matsudaira Riko']

idol_views = {}
df = pd.DataFrame()
final_list = []

day = 4
start_day = 1

for i in range(day):
    start_day += 24
end_day = start_day + 25

for index, names in enumerate(idol_youtube):
    with open(str(names + '.txt')) as f:
        content = f.read().splitlines()
        ints = [int(item) for item in content]
        ints = [i - ints[start_day] for i in ints]
        ints = ints[start_day:end_day]
        idol_views = {names: ints}
    df = pd.DataFrame(idol_views)
    df.reset_index(drop=True, inplace=True)
    final_list.append(df)

print(ints)
print(len(ints))
result = pd.concat(final_list, axis=1)
bcr.bar_chart_race(result,
                   filename='test' + str(day) + '.mp4',
                   steps_per_period=50,
                   period_length=1000,
                   title='Youtube views in the last 24 hours',
                   dpi=255
                   )
