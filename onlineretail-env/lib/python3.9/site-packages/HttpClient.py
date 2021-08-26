#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/24 上午8:15
# @Author  : Dirk Zhao
import requests
import Log
import os


METHODS = ['GET', 'POST', 'HEAD', 'TRACE', 'PUT', 'DELETE', 'OPTIONS', 'CONNECT']


class UnSupportMethodException(Exception):
    pass


class HttpClient():

    def __init__(self, url, method='GET', headers=None, cookies=None, log_file_name='test.log', log_path=os.path.curdir,
                 logger_name='bulma'):
        '''__init__方法必须传入url，默认请求方式为GET。logger的参数也需要定义'''
        self.url = url
        self.session = requests.session()
        self.method = method.upper()
        if self.method not in METHODS:
            raise UnSupportMethodException('不支持的method:{0},请检查传入参数'.format(self.method))
        self.set_headers(headers)
        self.set_cookies(headers)
        self.logger = Log.Logger(log_file_name=log_file_name, log_path=log_path, logger_name=logger_name).get_logger()

    def set_headers(self, headers):
        if headers:
            self.session.headers.update(headers)

    def set_cookies(self, cookies):
        if cookies:
            self.session.cookies.update(cookies)

    def send(self, params=None, data=None, **kwargs):
        '''GET方法传入params，POST方法传入data'''
        response = self.session.request(method=self.method, url=self.url, params=params, data=data, **kwargs)
        response.encoding = 'utf-8'
        self.logger.debug('{0}{1}'.format(self.method, self.url))
        self.logger.debug('请求成功：{0}\n{1}'.format(response, response.text))
        return response
