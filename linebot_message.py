# coding=gbk
from linebot import LineBotApi, WebhookHandler
from linebot.models import *
import os
import json
import chucard
from linebot.exceptions import InvalidSignatureError



line_bot_api = LineBotApi('QLukr//BlJki9MdmVKRt32Fkdq8X9MozZs4e+ZW4ZbMKlvnlcyheD3j5Qkr0n1tyPG3hyfXrxjU1sm3WcUIEH4jh9japPT7W1qsD3Ap/8YqQIuX1Zca+GANi4ygW+F9PvxAyqFWUQIdfO5JxERGVjgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('90a58874093b3fd1697672737991210e')
user1ID = "Ufc23829f15bf090d6431247100bb7ed2"

#push message to one user
with open(chucard.mypath+"\\dcard.json",'r',encoding="utf-8") as load_f:

    load_dict = json.load(load_f)
    all = load_dict["dcard"]
    image_url = all["avatar"]
    line_bot_api.push_message(user1ID,TextSendMessage(text= "今日時間 : "+ str(chucard.date) + "學校 : " + str(all["school"]) + "\n科系 : " + str(all["department"]) + "\n性別 : " + str(all["gender"]) + "\n專長與興趣 : " + str(all["talent"]) + "\n社團 : " + str(all["club"]) + "\n\n喜歡的課 :" + str(all["lecture"]) + "\n\n喜歡的國家" + str(all["lovedCountry"]) + "\n\n最近的困擾 : " + str(all["trouble"]) + "\n\n可交換的才藝 : " + str(all["exchange"]) + "\n\n想嘗試的事情 : " + str(all["wantToTry"])))
    line_bot_api.push_message(user1ID, ImageSendMessage(original_content_url=image_url, preview_image_url=image_url))
    load_f.close()

