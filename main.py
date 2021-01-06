import os

from youtubesearchpython import Video, ResultMode
import re
import time

list_youtube = ['https://www.youtube.com/watch?v=3RAkGB1-li0', 'https://www.youtube.com/watch?v=WaK9YfYNv2g',
                'https://www.youtube.com/watch?v=FGe84gUNegM', 'https://www.youtube.com/watch?v=R6h0HszBKnQ',
                'https://www.youtube.com/watch?v=QyTa_6Pqibw', 'https://www.youtube.com/watch?v=kLygVwmXREU',
                'https://www.youtube.com/watch?v=lHk9_bG4O7c', 'https://www.youtube.com/watch?v=3E_gdb5G608',
                'https://www.youtube.com/watch?v=D0Cvj4_mzQA', 'https://www.youtube.com/watch?v=KJD4H5CbHpo',
                'https://www.youtube.com/watch?v=NteYAaiUXzE', 'https://www.youtube.com/watch?v=RS16gBu2eT4',
                'https://www.youtube.com/watch?v=ipOfjIiST6A', 'https://www.youtube.com/watch?v=g114GkvmtxI',
                'https://www.youtube.com/watch?v=o6N6zwAnOoI']

idol_youtube = ['Endo Hikari', 'Morita Hikaru', 'Onuma Akiho', 'Masumoto Kira', 'Seki Yumiko', 'Matsuda Rina',
                'Tamura Hono', 'Ozono Rei', 'Fujiyoshi Karin', 'Kosaka Marino', 'Inoue Rina', 'Takemoto Yui',
                'Moriya Rena', 'Yamasaki Ten', 'Matsudaira Riko']


try:
    while True:
        for index, item in enumerate(list_youtube):
            video = Video.getInfo(item, mode=ResultMode.dict)
            string_views = str(video['viewCount'])
            temp = re.findall(r'\d+', string_views)
            res = list(map(int, temp))

            print(f"Views: {res[0]} Idol: {idol_youtube[index]}")

            filename = idol_youtube[index]+'.txt'
            file_exists = os.path.isfile(filename)

            with open(filename, 'a') as file_object:
                file_object.write(str(res[0])+"\n")

        time.sleep(3600)
except Exception as e:
    print("type error: " + str(e))

