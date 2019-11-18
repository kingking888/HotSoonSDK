#coding:utf-8

"""
    author : linkin
    date   : 2019-11-18
    QQ     : 949779859
"""

import requests
from settings import API
from deco.hotsoon import choose_api

class HotSoonClient:

    def __init__(self,appkey:str=None):
        self.appkey = appkey

    def GetUserId(self,share_url:str)->dict:
        params = {
            'appkey':self.appkey,
            'url':share_url,
        }
        response = requests.get(API.USERID,params=params)
        data = response.json()
        return data

    @choose_api(API.USER_VIDEOS)
    def GetUserVideos(self,
                      user_id:str=None,
                      share_url:str=None,
                      limits:int=0,
                      next_time:int=0,
                      ):
        '''
        获取火山用户发布的视频
        :param user_id: 火山用户uid，非火山号
        :param share_url: 火山用户主页的分享链接,类似:https://reflow.huoshan.com/hotsoon/s/GiUZbrFy700/
        :param limits: 需要爬取多少该用户发布的视频，默认0表示全部
        :param next_time: 下一页值
        :return: 爬取的用户视频列表
        '''
        return {
            'appkey': self.appkey,
            'uid':user_id,
            'url':share_url,
            'next_time': next_time,
        }

    @choose_api(API.FOLLOWERS)
    def GetUserFollowers(self,
                        user_id:str=None,
                        share_url:str=None,
                        limits:int=0,
                        next_time:int=0
                         ):
        '''
        获取火山用户的粉丝列表
        :param user_id: 火山用户uid，非火山号
        :param share_url: 火山用户主页的分享链接,类似:https://reflow.huoshan.com/hotsoon/s/GiUZbrFy700/
        :param limits: 需要爬取多少该用户的粉丝，默认0表示全部
        :param next_time: 下一页值
        :return: 爬取的用户粉丝列表
        '''
        return {
            'appkey': self.appkey,
            'uid': user_id,
            'url': share_url,
            'next_time': next_time,
        }

    @choose_api(API.FOLLOWINGS)
    def GetUserFollowings(self,
                         user_id: str = None,
                         share_url: str = None,
                         limits: int = 0,
                         next_time: int = 0
                         ):
        '''
        获取火山用户的关注列表
        :param user_id: 火山用户uid，非火山号
        :param share_url: 火山用户主页的分享链接,类似:https://reflow.huoshan.com/hotsoon/s/GiUZbrFy700/
        :param limits: 需要爬取多少该用户的关注，默认0表示全部
        :param next_time: 下一页值
        :return: 爬取的用户关注列表
        '''
        return {
            'appkey': self.appkey,
            'uid': user_id,
            'url': share_url,
            'next_time': next_time,
        }