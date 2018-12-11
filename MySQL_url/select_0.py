import pymssql
import hashlib

def getRobotVideoUrl(vid, domain='http://video.idongrong.com/'):
    md5 = hashlib.md5()
    md5.update((str(vid) + 'videoautoman').encode('utf-8'))
    return domain + str(vid) + '_' + md5.hexdigest() + '.mp4'

conn = pymssql.connect('183.131.205.158:2433',
                       'developer',
                       'cahBkaxGMEyybL55',
                       "dr_db")
cursor = conn.cursor()
cursor.execute('select top 10 user_idx from t_user_profile_tmp')
# res是个列表，列表中的每个元素是一个tuple
res = cursor.fetchall()
print(res)
for i in res:
    # print(i[0])
    print(getRobotVideoUrl(i[0]))
# print(res)
# s = (1)
# b = (1,)
# print(type(s), type(b))
# res = [(), (), ()]
# res[0

# # 获取机器人视频url


# if __name__ == '__main__':
#     print(getRobotVideoUrl(res[0][0]))
#  for vl in getRobotVideoUrl(i[0]):

s = pai * 3 * 3
s = pai * 6 * 6
