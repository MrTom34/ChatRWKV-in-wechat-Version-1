#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import uiautomation as auto


from uiautomation import WindowControl, MenuControl
# from LanguageModel import get_rasa_response
from get_response import get_response


def main():
    # 绑定微信主窗口
    wx = WindowControl(
        Name='微信',
        # searchDepth=1
    )

    # 切换窗口
    wx.SwitchToThisWindow()
    # 寻找会话控件绑定
    hw = wx.ListControl(Name='会话')
    # 通过pd读取数据


    friend_list = ['王骙', '止增笑耳', '贾振东','伍江航']
    # 死循环接受消息
    while True:
        # 从查找未读消息
        we = hw.TextControl(searchDepth=4)

        # 死循环维持，没有超时报错
        while not we.Exists(0):
            pass

        # 存在未读消息
        if we.Name:
            # 点击未读消息
            we.DoubleClick(simulateMove=False)
            agents_window = auto.GetForegroundControl().GetTopLevelControl()
            print(agents_window.Name)
            agents_name = agents_window.Name
            # agents_window.ButtonControl( Name='关闭').Click(simulateMove=False)
            agents_window.GetWindowPattern().Close()
            if agents_name not in friend_list:
                print('此人不是好友')
                continue
            else:
                we.Click(simulateMove=False)

            # 读取最后一条消息
            last_msg = wx.ListControl(Name='消息').GetChildren()[-1].Name
            print(last_msg)
            Assistant_name, pangbai, dialog = get_response(last_msg)
            reply = f'[ {Assistant_name} ]( {pangbai} ){dialog}'


            # 将数据输入
            # 替换换行符号
            wx.SendKeys(reply, waitTime=0)
            # 发送消息
            wx.SendKeys('{Enter}', waitTime=0)


            time.sleep(2)

def get_response(question):


        Edge = auto.WindowControl(ClassName='Chrome_WidgetWin_1')
        print(Edge.Name)
        Edge.Maximize()
        c = auto.GetForegroundControl().GetTopLevelControl()
        print(c.Name)

        RWKV_document = auto.DocumentControl(Depth=0, Name='RWKV角色扮演')
        print('get RWKV_document')

        RWKV_region = Edge.PaneControl(Name='RWKV角色扮演 - Microsoft Edge')
        print(RWKV_region)

        # RWKV_group = RWKV_region.GroupControl(Name = '组')
        # print(RWKV_group)
        # RWKV_send = RWKV_group.EditControl(Name = '整理Token中……')

        RWKV_send = RWKV_region.EditControl(ClassName='scroll-hide svelte-1f354aw')
        # RWKV_region_child = RWKV_region.GetChildren()
        # print(RWKV_region_child)
        RWKV_send.SendKeys(question, waitTime=0)
        # 发送消息
        RWKV_send.SendKeys('{Enter}', waitTime=0)
        print('发送成功，正在生成回答，30s')
        time.sleep(30)

        auto.uiautomation.SetGlobalSearchTimeout(20)
        Assistant_name = Edge.TextControl(foundIndex=105).Name

        pangbai = Edge.TextControl(foundIndex=106).Name
        dialog = Edge.TextControl(foundIndex=107).Name
        return Assistant_name,pangbai,dialog



if __name__ =='__main__':
    main()
