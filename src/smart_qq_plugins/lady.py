#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
 User: raphaelsoul
"""

from random import randint
import time
import datetime

from smart_qq_bot.messages import GroupMsg, PrivateMsg
from smart_qq_bot.signals import on_all_message, on_bot_inited
from smart_qq_bot.logger import logger


class LadyWrapper(object):
    def __init__(self):
        self.observe_target = '' # put watch target here
        self.interval = 600 # second
        self.GroupMap = {} #exp: {'groupID': last_reply_time}

_ladyWrapper = LadyWrapper()

@on_bot_inited("PluginManager")
def manager_init(bot):
    logger.info("Plugin Manager is available now:)")


@on_all_message(name="lady")
def lady(msg, bot):
    """
    :type bot: smart_qq_bot.bot.QQBot
    :type msg: smart_qq_bot.messages.GroupMsg
    """
    msg_id = randint(1, 10000)

    global _ladyWrapper

    logger.debug('sender:{0} QQ Number:{1}'
                 .format(msg.src_sender_name, msg.src_sender_id))
    logger.info(_ladyWrapper.GroupMap)
    # 发送一条群消息
    if isinstance(msg, GroupMsg):
        now = time.mktime(datetime.datetime.now().timetuple())

        if msg.src_sender_id == _ladyWrapper.observe_target:
            if msg.src_group_id in _ladyWrapper.GroupMap:
                if now > _ladyWrapper.GroupMap[msg.src_group_id] + _ladyWrapper.interval:
                    _ladyWrapper.GroupMap[msg.src_group_id] = now
                    bot.send_group_msg("少妇肛肛", msg.from_uin, msg_id)
                else:
                    logger.info("too frequent... Can't reply until {0}"
                                .format(_ladyWrapper.GroupMap[msg.src_group_id] + _ladyWrapper.interval))
            else:
                bot.send_group_msg("少妇肛肛", msg.from_uin, msg_id)
                _ladyWrapper.GroupMap[msg.src_group_id] = now