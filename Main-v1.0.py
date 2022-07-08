# -*- coding: utf-8 -*-
# Copyright (c) 2022, Harry Huang
# @ BSD 3-Clause License
import os, time
from src.osTool    import *
from src.colorTool import *
from src import ResolveAB       as AU_Rs
from src import CombineRGBwithA as AU_Cb
'''
ArkUnpacker主程序
'''
AU_ver='v1.0'


def prt_homepage():
    '''
    #### 打印主页
    :returns: (none);
    '''
    os.system('cls')
    print(color(7)+'欢迎使用ArkUnpacker '+AU_ver)

def prt_subtitle(msg:str):
    '''
    #### 打印子标题
    :param msg: 标题;
    :returns: (none);
    '''
    os.system('cls')
    os.chdir('.')
    print("")
    print(color(7,0,1)+'='*10)
    print(color(7,0,1)+msg)
    print(color(7,0,1)+'='*10)
    print(color(7))

def input_allow(msg:str,allow:list,excpt:str):
    '''
    #### 获取合规的键盘命令输入
    :param msg:   提示信息;
    :param allow: 包含了合规的输入的列表;
    :param excpt: 输入不合规时的提示信息;
    :returns:     (str) 一个合规的输入;
    '''
    inpt = input(msg)
    while not (inpt in allow):
        inpt = input(excpt)
    return inpt

def input_path(msg:str,excpt:str):
    '''
    #### 获取合规的目录路径输入
    :param msg:   提示信息;
    :param excpt: 输入目录不存在时的提示信息;
    :returns:     (str) 一个合规的输入;
    '''
    inpt = input(msg)
    while not (os.path.isdir(inpt)):
        inpt = input(excpt)
    return inpt

def run_quickaccess():
    '''
    #### 启动一键执行模式
    :returns: (none);
    '''
    prt_subtitle('步骤1|解包')
    AU_Rs.main(["test"],"test",dotxt=False,doaud=False,detail=False)
    prt_subtitle('步骤2|合并')
    AU_Cb.main(["temp\\test"],"temp2",docover=True,detail=False)
    exit()

def run_costm_Rs():
    '''
    #### 启动自定义解包模式
    :returns: (none);
    '''
    prt_subtitle('自定义解包')
    ###
    print(color(7)+'\n请输入要解包的目录后按回车')
    print('  支持相对路径，\".\"表示解包当前目录')
    rootdir = input_path(color(2)+'> ','  该目录似乎不存在\n> ')
    print('您选择的解包目录是：\n  '+color(6)+os.path.abspath(rootdir))
    ###
    print(color(7)+'\n请输入导出的目的地后按回车')
    print('  支持相对路径，留空表示自动创建')
    destdir = input(color(2)+'> ')
    if not destdir:
        destdir = "Unpacked_"+str(int(time.time()))
    print('您选择的导出目录是：\n  '+color(6)+os.path.abspath(destdir))
    ###
    dodel = False
    if os.path.isdir(destdir):
        print(color(7)+'\n该导出目录已存在，您要删除它里面的全部文件吗？')
        print(color(3)+'  请!慎重!选择：y=删除，n=保留')
        dodel = input(color(2)+'> ')
        dodel = True if dodel in ['y','Y'] else False
    ###
    print(color(7)+'\n您希望进行同名文件覆盖吗？')
    print(color(3)+'  我们!强烈建议!跳过：y=覆盖，n=跳过')
    docover = input(color(2)+'> ')
    docover = True if docover in ['y','Y'] else False
    ###
    print(color(7)+'\n您希望的回显模式是？')
    print(color(3)+'  y=详细，n=简洁')
    detail = input(color(2)+'> ')
    detail = True if detail in ['y','Y'] else False
    ###
    print(color(7)+'\n请输入要导出的资源类型后按回车')
    print('  可多选：i=图片，t=文本，a=音频')
    print('  示例输入：\"ita\"，\"ia\"')
    dothem = input(color(2)+'> ')
    doimg = True if 'i' in dothem or 'I' in dothem else False
    dotxt = True if 't' in dothem or 'T' in dothem else False
    doaud = True if 'a' in dothem or 'A' in dothem else False
    ###
    input(color(2)+'\n再按一次回车以开始任务...')
    AU_Rs.main([rootdir],destdir,dodel,doimg,dotxt,doaud,docover,detail)


if __name__ == '__main__':
    prt_homepage()
    run_costm_Rs()
    input()