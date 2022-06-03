from lcu_driver import Connector
from numpy import *
import time
import json
import datetime
from pynput.keyboard import Key, Controller as c_keyboard
# from pynput.mouse import Button, Controller as c_mouse
import time
from xpinyin import Pinyin
import pyperclip
from    tkinter import ttk

import pywintypes
import win32gui



connector = Connector()


summonerId='4120048865'


ChampionList= {"id1":"黑暗之女","id2":"狂战士","id3":"正义巨像","id4":"卡牌大师","id5":"德邦总管","id6":"无畏战车","id7":"诡术妖姬","id8":"猩红收割者","id9":"远古恐惧","id10":"正义天使","id11":"无极剑圣","id12":"牛头酋长","id13":"符文法师","id14":"亡灵战神","id15":"战争女神","id16":"众星之子","id17":"迅捷斥候","id18":"麦林炮手","id19":"祖安怒兽","id20":"雪原双子","id21":"赏金猎人","id22":"寒冰射手","id23":"蛮族之王","id24":"武器大师","id25":"堕落天使","id26":"时光守护者","id27":"炼金术士","id28":"痛苦之拥","id29":"瘟疫之源","id30":"死亡颂唱者","id31":"虚空恐惧","id32":"殇之木乃伊","id33":"披甲龙龟","id34":"冰晶凤凰","id35":"恶魔小丑","id36":"祖安狂人","id37":"琴瑟仙女","id38":"虚空行者","id39":"刀锋舞者","id40":"风暴之怒","id41":"海洋之灾","id42":"英勇投弹手","id43":"天启者","id44":"瓦洛兰之盾","id45":"邪恶小法师","id48":"巨魔之王","id50":"诺克萨斯统领","id51":"皮城女警","id53":"蒸汽机器人","id54":"熔岩巨兽","id55":"不祥之刃","id56":"永恒梦魇","id57":"扭曲树精","id58":"荒漠屠夫","id59":"德玛西亚皇子","id60":"蜘蛛女皇","id61":"发条魔灵","id62":"齐天大圣","id63":"复仇焰魂","id64":"盲僧","id67":"暗夜猎手","id68":"机械公敌","id69":"魔蛇之拥","id72":"水晶先锋","id74":"大发明家","id75":"沙漠死神","id76":"狂野女猎手","id77":"兽灵行者","id78":"圣锤之毅","id79":"酒桶","id80":"不屈之枪","id81":"探险家","id82":"铁铠冥魂","id83":"牧魂人","id84":"离群之刺","id85":"狂暴之心","id86":"德玛西亚之力","id89":"曙光女神","id90":"虚空先知","id91":"刀锋之影","id92":"放逐之刃","id96":"深渊巨口","id98":"暮光之眼","id99":"光辉女郎","id101":"远古巫灵","id102":"龙血武姬","id103":"九尾妖狐","id104":"法外狂徒","id105":"潮汐海灵","id106":"不灭狂雷","id107":"傲之追猎者","id110":"惩戒之箭","id111":"深海泰坦","id112":"机械先驱","id113":"北地之怒","id114":"无双剑姬","id115":"爆破鬼才","id117":"仙灵女巫","id119":"荣耀行刑官","id120":"战争之影","id121":"虚空掠夺者","id122":"诺克萨斯之手","id126":"未来守护者","id127":"冰霜女巫","id131":"皎月女神","id133":"德玛西亚之翼","id134":"暗黑元首","id136":"铸星龙王","id141":"影流之镰","id142":"暮光星灵","id143":"荆棘之兴","id145":"虚空之女","id147":"星籁歌姬","id150":"迷失之牙","id154":"生化魔人","id157":"疾风剑豪","id161":"虚空之眼","id163":"岩雀","id164":"青钢影","id166":"影哨","id201":"弗雷尔卓德之心","id202":"戏命师","id203":"永猎双子","id221":"祖安花火","id222":"暴走萝莉","id223":"河流之王","id234":"破败之王","id235":"涤魂圣枪","id236":"圣枪游侠","id238":"影流之主","id240":"暴怒骑士","id245":"时间刺客","id246":"元素女皇","id254":"皮城执法官","id266":"暗裔剑魔","id267":"唤潮鲛姬","id268":"沙漠皇帝","id350":"魔法猫咪","id360":"沙漠玫瑰","id412":"魂锁典狱长","id420":"海兽祭司","id421":"虚空遁地兽","id427":"翠神","id429":"复仇之矛","id432":"星界游神","id497":"幻翎","id498":"逆羽","id516":"山隐之焰","id517":"解脱者","id518":"万花通灵","id523":"残月之肃","id526":"镕铁少女","id555":"血港鬼影","id711":"愁云使者","id777":"封魔剑魂","id875":"腕豪","id876":"含羞蓓蕾","id887":"灵罗娃娃","id888":"炼金男爵"}
GlobalData=[]
GlobalData_summonerList=[]
Game_Mode_Config={
       'ARAM':{
              'chineseName':'极地大乱斗',
              'assistsScoreRate':0.3, # 助攻得分率，用于修正助攻的占比
       } ,
       'CLASSIC':{
              'chineseName':'召唤师峡谷（匹配、排位）',
              'assistsScoreRate':0.8, # 助攻得分率，用于修正助攻的占比
       },
       'TFT':{
              'chineseName':'云顶之弈',
              'assistsScoreRate':0, # 助攻得分率，用于修正助攻的占比
       },
       'URF':{
              'chineseName':'无限乱斗',
              'assistsScoreRate':0.6, # 助攻得分率，用于修正助攻的占比
       }, 
       'ONEFORALL':{
                'chineseName':'克隆模式',
              'assistsScoreRate':0.6, # 助攻得分率，用于修正助攻的占比
       }
}
Game_Config={
       'win_score':30,
       'firstBlood_score':10,
       'kda_score':40,
       'damage_score':10,
       'fightRate_score':5,
       'money_score':10,
       
       
       'importantGameDeltaHours':4,  # 最近4个小时内的对局变为5倍权重
       'titleRange':{
              '下等马':[0,27],
              '中等马':[27,35],
              '上等马':[35,45], 
              '小代':[45,55],
              '通天代':[50,100]
              
       }
}
GLobal_Data={
       'dataprocess':100,
}




keyboard = c_keyboard()


# ====================== 分行发送 ==============
def sendMessageByLine(messageResultList):  
       title = 'League of Legends (TM) Client'
       hwnd = win32gui.FindWindow(None, title)
       if hwnd == 0:
              return
       
       win32gui.SetForegroundWindow(hwnd)
       
       time.sleep(0.5)
       for oneLine in messageResultList:
              time.sleep(0.1)
              keyboard.press(Key.enter)
              time.sleep(0.1)
              keyboard.release(Key.enter) 
              time.sleep(0.1)
              keyboard.type(oneLine)
              time.sleep(0.1)
              keyboard.press(Key.enter)
              time.sleep(0.1)
              keyboard.release(Key.enter) 
              time.sleep(0.1)
              
              
# ====================== 发送简略消息 ============== {myTeam,enemyTeam}
def sendShortMessage(): 
       guessWinChance= str(getGuessWinChange()*100) +'%'
       result=[]
       result.append('预测胜率'+guessWinChance)
       myTeam=[]
       enemyTeam=[]  
       for oneSummoner in GlobalData_summonerList:
              if oneSummoner['isMyTeam']:
                     myTeam.append(oneSummoner) 
              else:
                     enemyTeam.append(oneSummoner) 
                    
       tpStr=""
       for oneSummoner in myTeam:
              tpStr = tpStr+' 我方【'+oneSummoner['title'] +'】'+oneSummoner['summonerLabel']+'      '        
       
       result.append(tpStr)
       tpStr=""
       for oneSummoner in enemyTeam:
              tpStr = tpStr+' 敌方【'+oneSummoner['title'] +'】'+oneSummoner['summonerLabel']+'      '      
       result.append(tpStr)  
       sendMessageByLine(result)
# ====================== 发送完整消息 ============== {myTeam,enemyTeam}
def sendFullMessage(): 
       myTeam=[]
       enemyTeam=[]
       messageResultList = GlobalData_summonerList
       myTeamSumScore=1
       enemyTeamSumScore=1
       for oneSummoner in messageResultList:
              if oneSummoner['isMyTeam']:
                     myTeam.append(oneSummoner)
                     myTeamSumScore=myTeamSumScore+ float(oneSummoner['score'])
              else:
                     enemyTeam.append(oneSummoner)
                     enemyTeamSumScore=enemyTeamSumScore+ float(oneSummoner['score'])
       
       guessWinChance =  round( (0.5 * (1+(myTeamSumScore-enemyTeamSumScore)/enemyTeamSumScore)    ),3) 
       if guessWinChance > 0.9:
              guessWinChance=0.91
       if guessWinChance < 0.1:
              guessWinChance=0.11
       guessWinChance =  str(guessWinChance*100)+'%'
       
       
       result=[]
       result.append('预估胜率:'+guessWinChance) 
        
       for oneSummoner in messageResultList:
              tpStr=''
              if oneSummoner['isMyTeam']:
                     tpStr=tpStr+'我方'
              else:
                     tpStr=tpStr+'敌方'
              
              tpStr=tpStr+'【'+oneSummoner['title']+'】'
       
            
              
              tpStr=tpStr+' '+str(oneSummoner['summonerLabel'])
              
              tpStr=tpStr+' 得分 '+str(oneSummoner['score'])
              
              tpStr=tpStr+' 近期战绩 '+str(oneSummoner['rencent_5_kda'])
       
              result.append(tpStr)
              print(tpStr)
       sendMessageByLine(result)


# ====================== 计算预测胜率 ========================
def getGuessWinChange():
       myTeam=[]
       enemyTeam=[]
       messageResultList = GlobalData_summonerList
       myTeamSumScore=1
       enemyTeamSumScore=1
       for oneSummoner in GlobalData_summonerList:
              if oneSummoner['isMyTeam']:
                     myTeam.append(oneSummoner)
                     myTeamSumScore=myTeamSumScore+ float(oneSummoner['score'])
              else:
                     enemyTeam.append(oneSummoner)
                     enemyTeamSumScore=enemyTeamSumScore+ float(oneSummoner['score'])
       guessWinChance =  round( (0.5 * (1+(myTeamSumScore-enemyTeamSumScore)/enemyTeamSumScore)    ),3) 
       if guessWinChance > 0.9:
              guessWinChance=0.91
       if guessWinChance < 0.1:
              guessWinChance=0.11 
       return round(guessWinChance,2)



# ================== 生成称号=====================
def getTitle(score):
       mScore = float(score)
       for titleName,titleScoreRange in Game_Config['titleRange'].items():
              if mScore >= titleScoreRange[0] and  mScore <= titleScoreRange[1]:
                     return titleName
       return '牛马'
# ============== 传入championId获得英雄名字================
def getChampionName(id):
       return ChampionList['id'+str(id)]


# ===================== 转化utc时间==============返回秒数
def get_time_stamp(result):
    result = result.replace(' ','')
    result = result.replace('T','')
    result = result.replace('Z','')
    utct_date1 = datetime.datetime.strptime(result, "%Y-%m-%d%H:%M:%S.%f")#2020-12-01 03:21:57.330000+00:00
    utct_date2 = time.strptime(result, "%Y-%m-%d%H:%M:%S.%f")#time.struct_time(tm_year=2020, tm_mon=12, tm_mday=1, tm_hour=3, tm_min=21, tm_sec=57, tm_wday=1, tm_yday=336, tm_isdst=-1)
#     print(utct_date1)
#     print(utct_date2)
    local_date = utct_date1 + datetime.timedelta(hours=8)#加上时区
    local_date_srt = datetime.datetime.strftime(local_date,"%Y-%m-%d %H:%M:%S.%f")#2020-12-01 11:21:57.330000
#     print(local_date_srt)
    time_array1 = time.mktime(time.strptime(local_date_srt,"%Y-%m-%d %H:%M:%S.%f"))#1606792917.0
    time_array2 = int(time.mktime(utct_date2))#1606764117
#     print(time_array1)
#     print(time_array2) 
    return int(time_array1)
get_time_stamp('2022-05-30T12: 41: 00.052Z')


# ================获取目标秒数距离现在的小时数==========
def getDeltaHours(targetTime):
       return int(time.time()-targetTime)/3600

# ==================== 基于gameObj计算单局召唤师得分====================
def getScoreInOneGame(oneParticipantObj,sumParticipantsData,nowGameMode):
         
       
       
       # 输赢得分 0分或1分
       win_score=0
       if(oneParticipantObj['stats']['win']):
              win_score=1
              
       
        
       
       # 计算KDA得分  最高分10。做归一化处理
       
       k_num= oneParticipantObj['stats']['kills']
       d_num= oneParticipantObj['stats']['deaths']
       a_num= oneParticipantObj['stats']['assists']
       kdaScorePacr=d_num
       if kdaScorePacr == 0:
              kdaScorePacr=1
       kda_score= (k_num+ (a_num * Game_Mode_Config[nowGameMode]['assistsScoreRate']) ) / kdaScorePacr 
       if kda_score >10 :
              kda_score==10
       kda_score = kda_score /10 #归一化 
       
       
       
       # 伤害占比得分 最高100%  辅助额外加成50%
       damage_score = oneParticipantObj['stats']['totalDamageDealtToChampions'] / sumParticipantsData ['sumDamage']
       if oneParticipantObj['timeline']['role'] == 'DUO_SUPPORT':
              damage_score=damage_score*1.5
              if (damage_score>1):
                     damage_score=1
       
       
       
       # 一血得分 0分或1分，助攻得分 则按照模式助攻计算比例
       firstBlood_score=0
       if (oneParticipantObj['stats']['firstInhibitorAssist']):
             firstBlood_score=Game_Mode_Config[nowGameMode]['assistsScoreRate'] 
       
       if (oneParticipantObj['stats']['firstBloodKill']):
             firstBlood_score=1 
       
           
       # 参团率得分 总分1 打野则额外增加占比
       sumFightDiv=sumParticipantsData['sumFight']
       if sumFightDiv==0:
              sumFightDiv=1
       fightRate_score= ( k_num + a_num )  /sumFightDiv
       
       
       
       
       # 经济得分 总分1分。 队内第一得1分，队内第二得0.5分，其他不得分
       money_score=0
       if oneParticipantObj['stats']['goldEarned'] >= sumParticipantsData['money_1_num']:
              money_score=1
       elif oneParticipantObj['stats']['goldEarned'] >= sumParticipantsData['money_2_num']:
              money_score=0.5
       
       
       # 计算总分 
       win_score = win_score * Game_Config['win_score'] / 100
       kda_score = kda_score * Game_Config['kda_score'] / 100
       damage_score = damage_score * Game_Config['damage_score'] / 100
       firstBlood_score = firstBlood_score * Game_Config['firstBlood_score'] / 100
       fightRate_score = fightRate_score * Game_Config['fightRate_score'] / 100
       money_score= money_score * Game_Config['money_score'] / 100
       
       
       sumScore=win_score+kda_score+damage_score+firstBlood_score+fightRate_score+money_score
       return sumScore
#  ===================基于gameList生成评价====================
def generateSummonerMsg(gameList,summonerId):
       # print("进入一次generateSummonerMsg",gameList[0]['participantIdentities'][0])
       
       KdaList=[]
       scoreList=[]
       surrenderList=[]
       firstBloodList=[]
       
       for oneGame in gameList:
              participantId=''
              # 找到这局对局中的participantId
              
              for oneParticipant in oneGame['participantIdentities']:
                    if str(oneParticipant['player']['summonerId'])==summonerId:
                           participantId=str(oneParticipant['participantId'])
              thisGameObj=''
              # 找到详细信息
              for oneParticipant in oneGame['participants']:
                     if str(oneParticipant['participantId'])==participantId:
                            thisGameObj=oneParticipant
                            break
              # 汇总所有队友总数据总伤害
              sumParticipantsData={
                     'sumDamage':0,
                     'sumFight':0, # 总击杀，用于计算参团率
                     'money_1_num':0,# 经济第一的钱数
                     'money_2_num':0,# 经济第2的钱数 
              }
              for oneParticipant in oneGame['participants']:
                     if oneParticipant['stats']['win']==thisGameObj['stats']['win']:
                            sumParticipantsData['sumDamage']=sumParticipantsData['sumDamage'] + oneParticipant['stats']['totalDamageDealtToChampions'] 
                            sumParticipantsData['sumFight']=sumParticipantsData['sumFight'] + oneParticipant['stats']['kills'] 
                     # 对经济排名，用于
                     if oneParticipant['stats']['win']==thisGameObj['stats']['win']:
                            if oneParticipant['stats']['goldEarned']>sumParticipantsData['money_1_num']:
                                   sumParticipantsData['money_2_num']=sumParticipantsData['money_1_num']
                                   sumParticipantsData['money_1_num']=oneParticipant['stats']['goldEarned'] 
                            elif oneParticipant['stats']['goldEarned']>sumParticipantsData['money_2_num']:
                                   sumParticipantsData['money_2_num']=oneParticipant['stats']['goldEarned']
                     
                            
              # 击杀-死亡 战绩计入
              KdaList.append(str(thisGameObj['stats']['kills'])+'-'+str(thisGameObj['stats']['deaths']))
              
              
              
              # 计算投降率，不计入总分
              if (thisGameObj['stats']['gameEndedInSurrender'] or thisGameObj['stats']['gameEndedInEarlySurrender'] ) and not thisGameObj['stats']['win']:
                     surrenderList.append(1)
              else:
                     surrenderList.append(0)
                     
              # 计算一血率
              if thisGameObj['stats']['firstBloodKill'] :
                     firstBloodList.append(1)
              else:
                     firstBloodList.append(0)
                     
                     
                     
              
              
              # 计算总分
              sumScore = getScoreInOneGame(thisGameObj,sumParticipantsData,oneGame['gameMode'])  
              # print('thisGameObj',thisGameObj)
              if  getDeltaHours(oneGame['gameCreation']/1000) <= Game_Config['importantGameDeltaHours']: # 近期战绩增加5倍权重
                     scoreList.append(sumScore)
                     scoreList.append(sumScore)
                     scoreList.append(sumScore)
                     scoreList.append(sumScore)
                     scoreList.append(sumScore)
              else:
                     scoreList.append(sumScore)
              
              
              # 本局得分
              
       # print('即将计算平均值',scoreList)
       
       # 近期战绩字符串
       if KdaList.__len__()<5:
              KdaList.append('··')
              KdaList.append('··')
              KdaList.append('··')
              KdaList.append('··')
              KdaList.append('··')
       kdaString=''
       for oKda in KdaList[-5:]:
              kdaString=kdaString+oKda+','
       
       
       finalScore = round(mean(scoreList)*100, 2)        
       
       
       
        
       return {
              "score": str(finalScore),
              "rencent_5_kda":kdaString,
              'surrenderRate': str(round(mean(surrenderList)*100, 0))+'%',          
              'firstBloodRate': str(round(mean(firstBloodList)*100, 0))+'%'          
       }
                            
@connector.ready
async def connect(connection):
       # summonerId='4120048865'
       
  #  获取当前对局
       # nowGameMsg = await connection.request('post', '/Help')
       # nowGameMsg = await nowGameMsg.json()
       # print(nowGameMsg)
       # return 
       
       #  获取当前对局
       nowGameMsg = await connection.request('get', '/lol-gameflow/v1/session')
       nowGameMsg = await nowGameMsg.json()
       print(nowGameMsg)
       Summonerlist=[]
       for oneSummoner in nowGameMsg['gameData']['teamOne']:
              Summonerlist.append(oneSummoner)
       for oneSummoner in nowGameMsg['gameData']['teamTwo']:
              Summonerlist.append(oneSummoner)      
       
       
       
       myTeam={}
       for oneSummoner in nowGameMsg['gameData']['playerChampionSelections']: 
              myTeam[oneSummoner['summonerInternalName']]=ChampionList['id'+str(int(oneSummoner['championId']))]
       
       
       summonerIndex=0
       
       messageResultList=[]
       
       sumNum =Summonerlist.__len__()*13
       
       for oneSummoner in Summonerlist: 
              summonerIndex=summonerIndex+1
              summonerId =str(int(oneSummoner['summonerId']))
              # print("即将查询",summonerId)
              #  获取召唤师历史对局
              summonerHistoryMsg = await connection.request('get', '/lol-match-history/v3/matchlist/account/'+summonerId+'')
              summonerHistoryMsg = await summonerHistoryMsg.json()
              # print("查询结果",summonerHistoryMsg)
              gameList = summonerHistoryMsg['games']['games']
              gameDataList=[]
              ii=0
              if gameList.__len__()>=17:
                     gameList=gameList[-13:]
              for oneGame in gameList:
                     ii=ii+1
                     # print (oneGame['gameId'])
                     time.sleep(0.3)
                     oneGameMsg = await connection.request('get', '/lol-match-history/v1/games/'+str(oneGame['gameId'])+'')
                     oneGameMsg = await oneGameMsg.json()
                     GLobal_Data['dataprocess']=GLobal_Data['dataprocess']+  round(100/sumNum,2)
                     UI_repaint()
                     gameDataList.append(oneGameMsg)  

              
              summonerResult= generateSummonerMsg(gameDataList,summonerId)  
              
              # print("召唤师得分",summonerScore) 
              
              summonerLabel=oneSummoner['summonerInternalName'] 
              if summonerLabel in myTeam:
                     summonerLabel=myTeam[summonerLabel]
                     
                     summonerResult['champion']=summonerLabel
                     summonerResult['isMyTeam']=True
              else:
                     summonerResult['isMyTeam']=False
                     summonerResult['champion']=''
              summonerResult['summonerLabel']=summonerLabel
              summonerResult['title']= getTitle(summonerResult['score'])
              summonerResult['summonerInternalName'] = oneSummoner['summonerInternalName']  
              print('【',summonerResult['score'],'】',summonerLabel,'近期战绩',summonerResult['rencent_5_kda'],'投降率',summonerResult['surrenderRate'],'一血率',summonerResult['firstBloodRate'])
              if(summonerIndex==5):
                     print("--")
       
              if(summonerIndex==10):
                     print("--",myTeam)
              
              messageResultList.append(summonerResult)
              GlobalData_summonerList.append(summonerResult)
              GlobalData.append(summonerResult)
              
       # GlobalData=messageResultList
       # print('已完成',GlobalData)
       GLobal_Data['dataprocess']=100
       UI_repaint()
       # #  获取当前聊天组
       # conversationsObj = await connection.request('get', '/lol-chat/v1/conversations')
       # conversationsObj = await conversationsObj.json()
       # cId=conversationsObj[0]['id']
       # print(conversationsObj[0]['id'])
       
       # 发送消息
       # sendData={
       #        'Body':'aaaaa',
       #        'Type': "chat"
       # }
       # conversationsObj =await connection.request('post', '/lol-chat/v1/conversations/'+str(cId)+'/messages',data=sendData)
       # print(await conversationsObj.json())
       
       
       
       
# connector.start()

import threading

class myThread (threading.Thread):  
    def run(self):
          connector.start() 
         

GLobal_Data['dataprocess']=0
GlobalTitle=['zz']
def btn_sendFullMsg(): 
       if GlobalData_summonerList.__len__() ==0: 
              print('暂无数据')
              return
       sendFullMessage()
def  btn_sendShorMsg(): 
       if GlobalData_summonerList.__len__() ==0: 
              print('暂无数据')
              return 
       sendShortMessage()
    
def  btn_resetData(): 
       for i in range(len(GlobalData_summonerList)):
              GlobalData_summonerList.pop() 
       GLobal_Data['dataprocess']=0
       thread1 = myThread()
       thread1.start()
       print('reset end')




tkinterComponents=[]


from tkinter import * 
def UI_repaint():  
                    
       for oneComponents in tkinterComponents:
              oneComponents.destroy()
                    
       myTeam=[]
       enemyTeam=[] 
       for oneSummoner in GlobalData_summonerList:
              if oneSummoner['isMyTeam']:
                     myTeam.append(oneSummoner) 
              else:
                     enemyTeam.append(oneSummoner)       
                        
                        
                                   
       root.title('下等马查询器')
       root.geometry('650x400')        
       
       
       sendMsgButton1 = Button ( root, text ="发送简略消息", command=btn_sendShorMsg)
       sendMsgButton1.place(x=0)
       sendMsgButton2 = Button ( root, text ="发送详细消息", command=btn_sendFullMsg)
       sendMsgButton2.place(x=90)
       tkinterComponents.append(sendMsgButton1)
       tkinterComponents.append(sendMsgButton2)
       if GLobal_Data['dataprocess'] == 100: 
              sendMsgButton3 = Button ( root, text ="刷新数据", command=btn_resetData)
              sendMsgButton3.place(x=580)
       else:
              sendMsgButton3 = Button ( root, text ="... "+str(round(GLobal_Data['dataprocess'],1))+'%')
              sendMsgButton3.place(x=580)
        
       tkinterComponents.append(sendMsgButton3)
       myTeamLabel = Label(root,text="召唤师信息")
       myTeamLabel.place(x=0,y=40)  
       tkinterComponents.append(myTeamLabel) 
       myTeamList = ttk.Treeview(root,height=10 )
       myTeamList['columns'] = ['champion','name','firstBloodRate','surrenderRate','kda']  
       myTeamList.column('champion',width=59)
       myTeamList.column('name',width=100) 
       myTeamList.column('firstBloodRate',width=44)
       myTeamList.column('surrenderRate',width=44)
       myTeamList.column('kda',width=200) 
       
       myTeamList.heading('champion',text='英雄')
       myTeamList.heading('name',text='名称') 
       myTeamList.heading('firstBloodRate',text='一血率')  
       myTeamList.heading('surrenderRate',text='投降率')  
       myTeamList.heading('kda',text='近期战绩')  
       myTeamList.place(x=0,y=60)              
       tkinterComponents.append(myTeamList) 


       for oneSummoner in GlobalData_summonerList:
              summonerText=''
              if oneSummoner['isMyTeam']:
                     summonerText='我方'
              else:
                     summonerText='敌方'
              summonerText=summonerText+'【'+oneSummoner['title']+'】 '+str(oneSummoner['score'])  
              myTeamList.insert('',0,text=summonerText,values=(oneSummoner['champion'],oneSummoner['summonerInternalName'],oneSummoner['firstBloodRate'],oneSummoner['surrenderRate'],oneSummoner['rencent_5_kda']))
       
       
     
       guessLabel = Label(root,text="胜率预测")
       guessLabel.place(x=500,y=310)  
       tkinterComponents.append(guessLabel) 
       
       guessWinText=str(round(getGuessWinChange()*100,1))+'%'
       guessWinLabel = Label(root,text=guessWinText, font=('Arial', 20), fg="red")
       guessWinLabel.place(x=560,y=300)  
       tkinterComponents.append(guessWinLabel) 
       # root.mainloop()                 # 进入消息循环


GLobal_Data['dataprocess']=100
root = Tk()  
UI_repaint()
root.mainloop()                 # 进入消息循环


# UI_repaint()


print(11)
 