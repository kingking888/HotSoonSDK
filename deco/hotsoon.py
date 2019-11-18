#coding:utf-8

"""
    author : linkin
    date   : 2019-11-18
    QQ     : 949779859
"""

import requests

def choose_api(api,method='get'):
    def outter(func):
        def wrapper(self,*args,**kwargs):
            needs = func(self,*args,**kwargs)
            next_time = kwargs.get('next_time',0)
            limits = kwargs.get('limits',0)
            count = 0
            results = []
            while 1:
                needs.update({
                    'next_time':next_time,
                })
                response = requests.request(method,api, params=needs)
                json_resp = response.json()
                data = json_resp.get('data')
                next_time = json_resp.get('next_time')
                if not data:
                    return results
                for item in data:
                    yield item
                    count += 1
                    results.append(item)
                    if count >= limits > 0:
                        return results
                if not json_resp.get('has_more'):
                    return results
        return wrapper
    return outter