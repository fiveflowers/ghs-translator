#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/19
# @Author  : Yifeng Huang
# @Github  : https://github.com/yifer97/ghs-translator.git
# @FileName: translator.py
# @Function: 调用谷歌翻译接口


from googletrans import Translator, urls, utils
from googletrans.compat import PY3
from googletrans.constants import DEFAULT_USER_AGENT


class MyTranslator(Translator):
    def __init__(self, service_urls=['translate.google.cn'], user_agent=DEFAULT_USER_AGENT,  # 改为中国源
                 proxies=None, timeout=None):
        super().__init__(service_urls, user_agent, proxies, timeout)

    def _translate(self, text, dest, src):
        if not PY3 and isinstance(text, str):  # pragma: nocover
            text = text.decode('utf-8')

        token = self.token_acquirer.do(text)
        params = utils.build_params(query=text, src=src, dest=dest,
                                    token=token)
        params['client'] = 'webapp'  # FFFFFFUCK,直接调用谷歌翻译的API结果和网页翻译的不一样
        url = urls.TRANSLATE.format(host=self._pick_service_url())
        r = self.session.get(url, params=params)

        data = utils.format_json(r.text)
        return data
