#coding:utf-8

"""
    author : linkin
    date   : 2019-11-18
    QQ     : 949779859
"""

from hsapi import HotSoonClient
from log import getLogger

LOG = getLogger(__name__)

if __name__ == '__main__':
    #服务器鉴权appkey,联系QQ949779859获取
    appkey = 'fb13ac5c8254fe4962f717af9a85da7a'
    a = HotSoonClient(appkey=appkey)
    limits = 10
    uid_data = a.GetUserId('https://reflow.huoshan.com/hotsoon/s/GiUZbrFy700/')
    useVideos = a.GetUserFollowers('73237777518',limits=limits)
    userFollowers = a.GetUserFollowers('73237777518',limits=limits)
    userFollowings = a.GetUserFollowings('73237777518',limits=limits)
    LOG.info(f'获取到的用户uid数据:\n{uid_data}')
    LOG.info(f'获取到的用户视频数据(前{limits}条样例):\n')
    for i in useVideos:
        LOG.info(f'{i}\n')
    LOG.info(f'获取到的用户粉丝数据(前{limits}条样例):\n')
    for i in userFollowers:
        LOG.info(f'{i}\n')
    LOG.info(f'获取到的用户关注数据(前{limits}条样例):\n')
    for i in userFollowings:
        LOG.info(f'{i}\n')
