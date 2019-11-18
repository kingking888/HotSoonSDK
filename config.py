#coding:utf-8

"""
    author : linkin
    date   : 2019-11-18
    QQ     : 949779859
"""


# ------ 日志设置 ------
#启用日志
LOG_ENABLE = True
#日志显示级别
LOG_LEVEL = 'INFO'
#日志文件编码
LOG_FILE_ENCODING = 'UTF-8'
#日志文件路径
LOG_FILE_SAVE_PATH = r'log/log.txt'
#日志时间格式
LOG_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
#日志级别对应格式
LOG_FORMAT = {
    'DEBUG'     : '%(asctime)s %(name)s(%(levelname)s) - %(message)s',
    'INFO'      : '%(asctime)s %(name)s(%(levelname)s) - %(message)s',
    'WARNING'   : '%(asctime)s %(name)s(%(levelname)s) - %(message)s',
    'ERROR'     : '%(asctime)s %(name)s(%(levelname)s) - %(message)s',
    'CRITICAL'  : '%(asctime)s %(name)s(%(levelname)s) - %(message)s',
}