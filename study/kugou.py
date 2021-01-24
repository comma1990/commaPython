# @Author  :  comma 
# @Date    :  2020-12-30 22:20

'''
pc_temp_songlist
<ul>
							<li class=" " title="回小仙 - 醒不来的梦" data-index="0">
								<span class="pc_temp_btn_check pc_temp_btn_checked" data-index="0"></span>
								<span class="pc_temp_coverlayer"></span>
								<span class="pc_temp_num">
																											<strong>1</strong>
																	</span>
																<a href="https://www.kugou.com/song/1d82by62.html" data-active="playDwn" data-index="0" class="pc_temp_songname" title="回小仙 - 醒不来的梦" hidefocus="true">回小仙 - 醒不来的梦</a>
								<span class="pc_temp_tips_r">
																		<a href="javascript:;" data-active="play" data-index="0" class="pc_temp_btn_listen" title="播放" hidefocus="true">播放</a>
									<a href="javascript:;" onclick="_hmt.push(['_trackEvent', 'hidedown', 'hidecilick', 'hidepc']);" data-active="download" data-index="0" class="pc_temp_btn_download" title="下载" hidefocus="true">下载</a>
									<a href="javascript:;" data-active="share" data-index="0" class="pc_temp_btn_share" title="分享" hidefocus="true">分享</a>
									<span class="pc_temp_time">
																											3:52
									</span>
								</span>
							</li>
'''


import requests
from bs4 import BeautifulSoup
url='https://www.kugou.com/yy/rank/home/1-8888.html?from=homepage'
headers={'Accept': 'application/json, text/plain, */*',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
           }
resp=requests.get(url,headers=headers)
bs=BeautifulSoup(resp.text,'lxml')
id_list=bs.find_all('span',class_='pc_temp_num')
name_list=bs.find_all('a',class_='pc_temp_songname')
time_list=bs.find_all('span',class_='pc_temp_time')
for i in range(len(name_list)):
    print(id_list[i].text.strip()+'\t'+name_list[i].text.strip()+'\t'+time_list[i].text.strip())