# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup as BS
import re
import pickle
import glob
import numpy
import os
import os.path
import shutil

#タプルから抽出・置換して配列にする
def replace():
    #競馬場ごとに分けるための配列
    arr_c = []

    f = glob.glob(r"[directory_path]\*_kekka.txt")

    for fi in f:
        #レースごとに分けるための配列
        arr_r = []

        fj = open(fi)
        a = pickle.load(fj)
        fj.close()

        for aa in a:
            #１R分の馬連と馬単の結果と払戻金を入れる配列
            arr = []

            for aaren in aa[0]:
                arr.append(aaren[0].replace("\xef\xbc\x8d", "="))
                arr.append(aaren[1].replace(",", ""))

            for aatan in aa[1]:
                arr.append(aatan[0].replace("\xef\xbc\x8d", "-"))
                arr.append(aatan[1].replace(",", ""))

            arr_r.append(arr)

        arr_c.append(arr_r)

    f1 = open(r"[directory_path]\kekka_final.txt","w")
    pickle.dump(arr_c, f1)
    f1.close()

#replace()



def comp():
    fc = glob.glob(r'[directory_path]\chukyo\*.txt')

    fh = glob.glob(r'[directory_path]\hakodate\*.txt')
    fs = glob.glob(r'[directory_path]\sapporo\*.txt')
    ft = glob.glob(r'[directory_path]\tokyo\*.txt')
    fk = glob.glob(r'[directory_path]\kyoto\*.txt')
    fn = glob.glob(r'[directory_path]\nakayama\*.txt')
    ff = glob.glob(r'[directory_path]\fukushima\*.txt')
    fhan = glob.glob(r'[directory_path]\hanshin\*.txt')
    fko = glob.glob(r'[directory_path]\kokura\*.txt')
    fni = glob.glob(r'[directory_path]\niigata\*.txt')

    fck = glob.glob(r'[directory_path]\chukyo\*.txt')

    fhk = glob.glob(r'[directory_path]\hakodate\*.txt')
    fsk = glob.glob(r'[directory_path]\sapporo\*.txt')
    ftk = glob.glob(r'[directory_path]\tokyo\*.txt')
    fkk = glob.glob(r'[directory_path]\kyoto\*.txt')
    fnk = glob.glob(r'[directory_path]\nakayama\*.txt')
    ffk = glob.glob(r'[directory_path]\fukushima\*.txt')
    fhank = glob.glob(r'[directory_path]\hanshin\*.txt')
    fkok = glob.glob(r'[directory_path]\kokura\*.txt')
    fnik = glob.glob(r'[directory_path]\niigata\*.txt')

    for f in fc:
        for fck1 in fck:
            if os.path.basename(f) == os.path.basename(fck1):
                shutil.copy(fck1, r'[directory_path]\chukyo_kekka')
                break

    for f in fh:
        for fhk1 in fhk:
            if os.path.basename(f) == os.path.basename(fhk1):
                shutil.copy(fhk1, r'[directory_path]\hakodate_kekka')
                break
    for f in fs:
        for fsk1 in fsk:
            if os.path.basename(f) == os.path.basename(fsk1):
                shutil.copy(fsk1, r'[directory_path]\sapporo_kekka')
                break
    for f in ft:
        for ftk1 in ftk:
            if os.path.basename(f) == os.path.basename(ftk1):
                shutil.copy(ftk1, r'[directory_path]\tokyo_kekka')
                break
    for f in fk:
        for fkk1 in fkk:
            if os.path.basename(f) == os.path.basename(fkk1):
                shutil.copy(fkk1, r'[directory_path]\kyoto_kekka')
                break
    for f in fn:
        for fnk1 in fnk:
            if os.path.basename(f) == os.path.basename(fnk1):
                shutil.copy(fnk1, r'[directory_path]\nakayama_kekka')
                break
    for f in ff:
        for ffk1 in ffk:
            if os.path.basename(f) == os.path.basename(ffk1):
                shutil.copy(ffk1, r'[directory_path]\fukushima_kekka')
                break
    for f in fhan:
        for fhank1 in fhank:
            if os.path.basename(f) == os.path.basename(fhank1):
                shutil.copy(fhank1, r'[directory_path]\hanshin_kekka')
                break
    for f in fko:
        for fkok1 in fkok:
            if os.path.basename(f) == os.path.basename(fkok1):
                shutil.copy(fkok1, r'[directory_path]\kokura_kekka')
                break
    for f in fni:
        for fnik1 in fnik:
            if os.path.basename(f) == os.path.basename(fnik1):
                shutil.copy(fnik1, r'[directory_path]\niigata_kekka')
                break

#comp()

#予想配列中の要素を分割
def bunkatsu():
    #分割前のtxtファイル読み込み
    f = glob.glob(r'[directory_path]\*_yosou.txt')

    #予想者ごとの予想を入れる配列
    #[[中京],[福島],...]となる配列
    ota_final = []
    ayae_final = []
    yamada_final = []
    tama_final = []

    for ff in f:
        #競馬場ごとに２次元配列とするため競馬場ごとに初期化
        ota = []
        ayae = []
        yamada = []
        tama = []

        #配列のまま読み込み
        f0 = open(ff, "r")
        fi = pickle.load(f0)
        f0.close()

        for fii in fi:
            count = 0
            for youso in fii:
                #スペースで区切られているのでコンマで区切るようにする
                ysplit = youso.split(' ')
                #予想者ごとに予想を分ける
                #1Rごとに要素をいくつか持った1つの配列とするので２次元配列になる
                if count == 0:
                    ota.append(ysplit)
                if count == 1:
                    ayae.append(ysplit)
                if count == 2:
                    yamada.append(ysplit)
                if count == 3:
                    tama.append(ysplit)
                count += 1

        ota_final.append(ota)
        ayae_final.append(ayae)
        yamada_final.append(yamada)
        tama_final.append(tama)

    #予想者ごとに保存
    f = open(r"[directory_path]\yosou_ota.txt","w")
    pickle.dump(ota_final, f)
    f.close()
    f = open(r"[directory_path]\yosou_ayae.txt","w")
    pickle.dump(ayae_final, f)
    f.close()
    f = open(r"[directory_path]\yosou_yamada.txt","w")
    pickle.dump(yamada_final, f)
    f.close()
    f = open(r"[directory_path]\yosou_tama.txt","w")
    pickle.dump(tama_final, f)
    f.close()

#bunkatsu()


"""
#馬場状態を抽出
def baba(keibajou, soup):
    #馬場状態
    baba = re.compile("spBg ([a-z]*)")

    for link in soup.findAll("p", id="raceTitMeta"):
        #特徴抽出
        aa = link.contents
        aa = baba.findall(str(aa))
        #競馬場ごとに分ける
        if keibajou == ['sapporo']:
            return aa
        if keibajou == ['hakodate']:
            return aa
        if keibajou == ['fukushima']:
            return aa
        if keibajou == ['niigata']:
            return aa
        if keibajou == ['tokyo']:
            return aa
        if keibajou == ['nakayama']:
            return aa
        if keibajou == ['chukyo']:
            return aa
        if keibajou == ['kyoto']:
            return aa
        if keibajou == ['hanshin']:
            return aa
        if keibajou == ['kokura']:
            return aa

#何番人気で決着したかを抽出
def ninki(keibajou, htmltxt):
    #全馬の着順人気
    ninkiba = re.compile("<td class=\"txC fntS\">(\d+)</td>")
    #特徴抽出
    aa = ninkiba.findall(htmltxt)
    #競馬場ごとに分ける
    if keibajou == ['sapporo']:
        return aa
    if keibajou == ['hakodate']:
        return aa
    if keibajou == ['fukushima']:
        return aa
    if keibajou == ['niigata']:
        return aa
    if keibajou == ['tokyo']:
        return aa
    if keibajou == ['nakayama']:
        return aa
    if keibajou == ['chukyo']:
        return aa
    if keibajou == ['kyoto']:
        return aa
    if keibajou == ['hanshin']:
        return aa
    if keibajou == ['kokura']:
        return aa

#コース、距離抽出
def distance(keibajou, htmltxt):
    #コース、距離抽出のための正規表現
    distpat = re.compile("fntSS gryB\">(\w*).+\s(.+)m \[")
    #芝→shiba、ダート→dirt、障害→shougaiに置換
    htmltxt = htmltxt.replace('芝', 'shiba')
    htmltxt = htmltxt.replace('ダート', 'dirt')
    htmltxt = htmltxt.replace('障害', 'shougai')
    #特徴抽出
    aa = distpat.findall(htmltxt)
    #競馬場ごとに分ける
    if keibajou == ['sapporo']:
        return aa
    if keibajou == ['hakodate']:
        return aa
    if keibajou == ['fukushima']:
        return aa
    if keibajou == ['niigata']:
        return aa
    if keibajou == ['tokyo']:
        return aa
    if keibajou == ['nakayama']:
        return aa
    if keibajou == ['chukyo']:
        return aa
    if keibajou == ['kyoto']:
        return aa
    if keibajou == ['hanshin']:
        return aa
    if keibajou == ['kokura']:
        return aa
"""


def yosou(keibajou, htmltxt):
    yoso = re.compile("<td class=\"txL\">(.+)</td></tr>")
    aa = yoso.findall(htmltxt)
    #競馬場ごとに分ける
    if keibajou == ['sapporo']:
        return aa
    if keibajou == ['hakodate']:
        return aa
    if keibajou == ['fukushima']:
        return aa
    if keibajou == ['niigata']:
        return aa
    if keibajou == ['tokyo']:
        return aa
    if keibajou == ['nakayama']:
        return aa
    if keibajou == ['chukyo']:
        return aa
    if keibajou == ['kyoto']:
        return aa
    if keibajou == ['hanshin']:
        return aa
    if keibajou == ['kokura']:
        return aa

def odds(keibajou, htmltxt):
    ren = re.compile("馬連</th>\n<td class=\"txC resultNo\">(.+)</td>\n<td>(\d+[,\d]*)")
    renar = ren.findall(htmltxt)
    tan = re.compile("馬単</th>\n<td class=\"txC resultNo\">(.+)</td>\n<td>(\d+[,\d]*)")
    tanar = tan.findall(htmltxt)
    #競馬場ごとに分ける
    if keibajou == ['sapporo']:
        return renar, tanar
    if keibajou == ['hakodate']:
        return renar, tanar
    if keibajou == ['fukushima']:
        return renar, tanar
    if keibajou == ['niigata']:
        return renar, tanar
    if keibajou == ['tokyo']:
        return renar, tanar
    if keibajou == ['nakayama']:
        return renar, tanar
    if keibajou == ['chukyo']:
        return renar, tanar
    if keibajou == ['kyoto']:
        return renar, tanar
    if keibajou == ['hanshin']:
        return renar, tanar
    if keibajou == ['kokura']:
        return renar, tanar



#抽出
def ext(keibajou, soup, htmltxt):
    """
    #馬場状態
    babastate = baba(keibajou, soup)
    #人気
    ninkii = ninki(keibajou, htmltxt)
    #距離
    kyori = distance(keibajou, htmltxt)
    """
    #予想
    yoso = yosou(keibajou, htmltxt)
    #払戻金(馬連と馬単)
    #odd = odds(keibajou, htmltxt)

    return yoso

    """
    #ファイルを1つずつ見る
    for file in fileglob:
        feature = []
        f0 = open(file, "r")
        htmltxt = f0.read()
        #ファイル命名用
        keibajou = file_re.findall(file)
        #HTMLテキスト抽出
        soup = BS(htmltxt)
    """

#最初に実行
def main():
    #ファイル名抽出
    #予想ファイル
    fileglob = glob.glob(r"[directory_path]\*_yosou\*.txt")
    #結果ファイル
    #fileglob = glob.glob(r"[directory_path]\*_kekka\*.txt")

    #ファイル命名用（競馬場名）
    file_re = re.compile("[directory_path]\\\\.+\\\\(.+)_")

    #特徴を入れるリスト
    sapporoar = []
    hakodatear = []
    fukushimaar = []
    niigataar = []
    tokyoar = []
    nakayamaar = []
    chukyoar = []
    kyotoar = []
    hanshinar = []
    kokuraar = []

    #ファイルを1つずつ見る
    for file in fileglob:
        #featureリストを初期化
        feature = []
        #ファイル読み込み
        f0 = open(file, "r")
        htmltxt = f0.read()#.decode("utf_8")
        f0.close()
        #HTMLテキスト抽出
        soup = BS(htmltxt)
        #ファイル命名用(競馬場名)
        keibajou = file_re.findall(file)
        #main()から返ってきた特徴をリストに追加
        #[[特徴1,特徴2,...,特徴n],[特徴1,...,特徴n]という感じになる
        if keibajou == ['sapporo']:
            sapporoar.append(ext(keibajou, soup, htmltxt))
        if keibajou == ['hakodate']:
            hakodatear.append(ext(keibajou, soup, htmltxt))
        if keibajou == ['fukushima']:
            fukushimaar.append(ext(keibajou, soup, htmltxt))
        if keibajou == ['niigata']:
            niigataar.append(ext(keibajou, soup, htmltxt))
        if keibajou == ['tokyo']:
            tokyoar.append(ext(keibajou, soup, htmltxt))
        if keibajou == ['nakayama']:
            nakayamaar.append(ext(keibajou, soup, htmltxt))
        if keibajou == ['chukyo']:
            chukyoar.append(ext(keibajou, soup, htmltxt))
        if keibajou == ['kyoto']:
            kyotoar.append(ext(keibajou, soup, htmltxt))
        if keibajou == ['hanshin']:
            hanshinar.append(ext(keibajou, soup, htmltxt))
        if keibajou == ['kokura']:
            kokuraar.append(ext(keibajou, soup, htmltxt))


    #保存
    #ファイル名を競馬場名_kekka.txtとして保存(予想の時は_yosouにする)
    #札幌
    f = open(r"[directory_path]\sapporo_yosou.txt","w")
    pickle.dump(sapporoar, f)
    f.close()
    #函館
    f = open(r"[directory_path]\hakodate_yosou.txt","w")
    pickle.dump(hakodatear, f)
    f.close()
    #福島
    f = open(r"[directory_path]\fukushima_yosou.txt","w")
    pickle.dump(fukushimaar, f)
    f.close()
    #新潟
    f = open(r"[directory_path]\niigata_yosou.txt","w")
    pickle.dump(niigataar, f)
    f.close()
    #東京
    f = open(r"[directory_path]\tokyo_yosou.txt","w")
    pickle.dump(tokyoar, f)
    f.close()
    #中山
    f = open(r"[directory_path]\nakayama_yosou.txt","w")
    pickle.dump(nakayamaar, f)
    f.close()
    #中京
    f = open(r"[directory_path]\chukyo_yosou.txt","w")
    pickle.dump(chukyoar, f)
    f.close()
    #京都
    f = open(r"[directory_path]\kyoto_yosou.txt","w")
    pickle.dump(kyotoar, f)
    f.close()
    #阪神
    f = open(r"[directory_path]\hanshin_yosou.txt","w")
    pickle.dump(hanshinar, f)
    f.close()
    #小倉
    f = open(r"[directory_path]\kokura_yosou.txt","w")
    pickle.dump(kokuraar, f)
    f.close()




def analysis():
    #すべての予想のファイル名抽出
    f = glob.glob(r"[directory_path]\yosou_*.txt")

    """
    #予想者全員分の結果を入れる配列
    kaisyuu = []
    tekicyuu = []
    kounyuu = []
    """

    chuushi = []
    syou = []

    #予想者ごとに分けるための配列
    kaisyuu_yosousya = []
    tekicyuu_yosousya = []
    kounyuu_yosousya = []

    #ファイルを１つずつ見る(予想者１人ずつ)
    for file in f:
        f0 = open(file, "r")
        fi = pickle.load(f0)
        f0.close()

        #結果ファイル読み込み
        fk = open(r"[directory_path]\kekka_final.txt")
        fkekka = pickle.load(fk)
        fk.close()



        #競馬場ごとの回収率と的中率用
        kaisyuu_jou = []
        tekicyuu_jou = []

        #購入費用
        kounyuu_jou = []

        #競馬場ごと
        for (jou, jouk) in zip(fi, fkekka):

            #加算していく
            tekicyuu_count = 0
            kaisyuu_count = 0
            kounyuu_count = 0

            #中止したのを数える用
            chuushicount = 0
            #少頭数レース数える用
            syoucount = 0

            #レースごと
            for (race, racek) in zip(jou, jouk):
                if(len(racek) == 2):
                    syoucount += 1

                #買い目ごと
                for kaime in race:
                    #開催中止のときbreak
                    if(len(racek) == 0):
                        chuushicount += 1
                        break

                    #もし少頭数で馬連発売がない時
                    elif(len(racek) == 2):
                        #=を-にして馬単のみの買い目にする
                        if('=' in kaime):
                            kaime.replace('=', '-')
                            if (kaime == racek[0]):
                                #kaisyuu_count += int(racek[1])
                                #1000円単位での購入のとき
                                kaisyuu_count += int(racek[1])*10
                                tekicyuu_count += 1
                        #元から馬単のとき
                        if('-' in kaime):
                            if (kaime == racek[0]):
                                #kaisyuu_count += int(racek[1])
                                #1000円単位での購入のとき
                                kaisyuu_count += int(racek[1])*10
                                tekicyuu_count += 1
                        #kounyuu_count += 100
                        #1000円単位
                        kounyuu_count += 1000



                    #馬連か馬単か
                    else:
                        if ('=' in kaime):
                            if (kaime == racek[0]):
                                #kaisyuu_count += int(racek[1])
                                #1000円単位での購入のとき
                                kaisyuu_count += int(racek[1])*10
                                tekicyuu_count += 1
                            #kounyuu_count += 100
                            #1000円単位
                            kounyuu_count += 1000
                        if ('-' in kaime):
                            if (kaime == racek[2]):
                                #kaisyuu_count += int(racek[3])
                                #1000円単位での購入のとき
                                kaisyuu_count += int(racek[3])*10
                                tekicyuu_count += 1
                            #kounyuu_count += 100
                            #1000円単位
                            kounyuu_count += 1000


            #予想者１人の競馬場ごとの結果
            kaisyuu_jou.append(kaisyuu_count)
            tekicyuu_jou.append(tekicyuu_count)
            kounyuu_jou.append(kounyuu_count)
            chuushi.append(chuushicount)
            syou.append(syoucount)

        #予想者１人分の結果
        kaisyuu_yosousya.append(kaisyuu_jou)
        tekicyuu_yosousya.append(tekicyuu_jou)
        kounyuu_yosousya.append(kounyuu_jou)

    """
    #予想者全員分の結果
    kaisyuu.append(kaisyuu_yosousya)
    tekicyuu.append(tekicyuu_yosousya)
    kounyuu.append(kounyuu_yosousya)
    """

    print kaisyuu_yosousya
    print tekicyuu_yosousya
    print kounyuu_yosousya
    print syou


    fwrite = open("[directory_path]\\kaisyuu1000.txt", "w")
    pickle.dump(kaisyuu_yosousya, fwrite)
    fwrite.close()
    #fwrite1 = open("[directory_path]\\tekicyuu.txt", "w")
    #pickle.dump(tekicyuu_yosousya, fwrite1)
    #fwrite1.close()
    fwrite2 = open("[directory_path]\\kounyuu1000.txt", "w")
    pickle.dump(kounyuu_yosousya, fwrite2)
    fwrite2.close()


def culc():
    f1 = open(r"[directory_path]\kaisyuu1000.txt")
    kaisyuu = pickle.load(f1)
    f1.close()
    f2 = open(r"[directory_path]\tekicyuu.txt")
    tekicyuu = pickle.load(f2)
    f2.close()
    f3 = open(r"[directory_path]\kounyuu1000.txt")
    kounyuu = pickle.load(f3)
    f3.close()

    #的中率計算（tekichuu/下のレース数）
    race = [656, 631, 456, 1236, 723, 1381, 1280, 789, 445, 1339]
    yosousya = []
    for t in tekicyuu:
        keibajou = []
        for (t2, r) in zip(t, race):
            kk = (float(t2) / float(r)) * 100
            keibajou.append(round(kk, 1))
        yosousya.append(keibajou)
    print yosousya

    yosousya_kaisyuuritsu = []
    yosousya_kaisyuu = []

    #回収率計算（kaisyuu/kounyuu）
    for (ka,ko) in zip(kaisyuu, kounyuu):
        keibajou_kaisyuuritsu = []
        keibajou_kaisyuu = []
        for (ka2, ko2) in zip(ka, ko):
            keisan1 = ka2 - ko2
            keisan2 = (float(ka2) / float(ko2)) * 100
            keibajou_kaisyuu.append(keisan1)
            keibajou_kaisyuuritsu.append(round(keisan2, 1))
        yosousya_kaisyuu.append(keibajou_kaisyuu)
        yosousya_kaisyuuritsu.append(keibajou_kaisyuuritsu)
    print yosousya_kaisyuu
    print yosousya_kaisyuuritsu



#中京：656，福島：631，函館：456，阪神：1236，小倉：723，京都：1381，中山：1280，新潟：789，札幌：445，東京：1339

#特徴抽出
#main()
#特徴ベクトル作成
#vector()
#分析
#analysis()
#計算
culc()
