import pandas as pd
import bar_chart_race as bcr

idol_youtube = ['Endo Hikari', 'Morita Hikaru', 'Onuma Akiho', 'Masumoto Kira', 'Seki Yumiko', 'Matsuda Rina',
                'Tamura Hono', 'Ozono Rei', 'Fujiyoshi Karin', 'Kosaka Marino', 'Inoue Rina', 'Takemoto Yui',
                'Moriya Rena', 'Yamasaki Ten', 'Matsudaira Riko']

idol_views = {}
df = pd.DataFrame()
final_list = []

for index, names in enumerate(idol_youtube):
    with open(str(names + '.txt')) as f:
        content = f.read().splitlines()
        ints = [int(item) for item in content]
        ints = [i - ints[0] for i in ints]
        idol_views = {names: ints}
    df = pd.DataFrame(idol_views)
    df.reset_index(drop=True, inplace=True)
    final_list.append(df)

result = pd.concat(final_list, axis=1)
bcr.bar_chart_race(result,
                   filename='test.mp4',
                   steps_per_period=50,
                   period_length=1000,
                   title='Youtube views in the last 24 hours',
                   )
