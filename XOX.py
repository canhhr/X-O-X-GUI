from tkinter import *
import random



class Window:
    def StartUp():
        Window.Settings()
        Window.Main()


    def Settings():
        global title, geometry
        title = "X O X Oyun"
        geometry = "750x590+550+150"


    def Squares():
        global kutu1, kutu2, kutu3, kutu4, kutu5, kutu6, kutu7, kutu8, kutu9
        #---------------- İLK SATIR

        kutu1 = Canvas(p, width=100, height=100, bg="gray")
        kutu1.place(x = 130, y = 150)

        kutu2 = Canvas(p, width=100, height=100, bg="gray")
        kutu2.place(x = 250, y = 150)

        kutu3 = Canvas(p, width=100, height=100, bg="gray")
        kutu3.place(x = 370, y = 150)

        # ---------------- İKİNCİ SATIR

        kutu4 = Canvas(p, width=100, height=100, bg="gray")
        kutu4.place(x = 130, y = 270)

        kutu5 = Canvas(p, width=100, height=100, bg="gray")
        kutu5.place(x = 250, y = 270)

        kutu6 = Canvas(p, width=100, height=100, bg="gray")
        kutu6.place(x = 370, y = 270)

        # ---------------- ÜÇÜNCÜ SATIR

        kutu7 = Canvas(p, width=100, height=100, bg="gray")
        kutu7.place(x = 130, y = 390)

        kutu8 = Canvas(p, width=100, height=100, bg="gray")
        kutu8.place(x = 250, y = 390)

        kutu9 = Canvas(p, width=100, height=100, bg="gray")
        kutu9.place(x = 370, y = 390)

        #---------------- YAZILAR
        global alan1, alan2, alan3, alan4, alan5, alan6, alan7, alan8, alan9

        alan1 = Label(p,
                   text="",
                   font=("arial",50,"bold"),
                   bg="gray")
        alan1.place(x = 155, y = 160)

        alan2 = Label(p,
                   text="",
                   font=("arial",50,"bold"),
                   bg="gray")
        alan2.place(x = 275, y = 160)

        alan3 = Label(p,
                   text="",
                   font=("arial",50,"bold"),
                   bg="gray")
        alan3.place(x = 395, y = 160)


        alan4 = Label(p,
                   text="",
                   font=("arial",50,"bold"),
                   bg="gray")
        alan4.place(x = 155, y = 280)

        alan5 = Label(p,
                   text="",
                   font=("arial",50,"bold"),
                   bg="gray")
        alan5.place(x = 275, y = 280)


        alan6 = Label(p,
                   text="",
                   font=("arial",50,"bold"),
                   bg="gray")
        alan6.place(x = 395, y = 280)


        alan7 = Label(p,
                   text="",
                   font=("arial",50,"bold"),
                   bg="gray")
        alan7.place(x = 155, y = 400)

        alan8 = Label(p,
                   text="",
                   font=("arial",50,"bold"),
                   bg="gray")
        alan8.place(x = 275, y = 400)

        alan9 = Label(p,
                   text="",
                   font=("arial",50,"bold"),
                   bg="gray")
        alan9.place(x = 395, y = 400)


    def InfoArea():
        infotext1 = Label(p,
                          text="YOU:   X",
                          font=("arial",20,"bold"))
        infotext1.place(x = 550, y = 200)

        infotext2 = Label(p,
                          text="PC:     O",
                          font=("arial",20,"bold"))
        infotext2.place(x = 553, y = 250)


    def AreaCheck():
        global a1,a2,a3,a4,a5,a6,a7,a8,a9, alanlar
        a1, a2, a3 = alan1.cget("text"), alan2.cget("text"), alan3.cget("text")
        a4, a5, a6 = alan4.cget("text"), alan5.cget("text"), alan6.cget("text")
        a7, a8, a9 = alan7.cget("text"), alan8.cget("text"), alan9.cget("text")

        alanlar = [a1, a2, a3, a4, a5, a6, a7, a8, a9]


    def SayıHesaplama():
        global x_sayı, o_sayı
        #X SAYI BULMA
        for i in alanlar:
            if i == "O":
                pass
            elif i == "":
                pass
            elif i == "X":
                x_sayı = x_sayı + i

        x_sayı = len(x_sayı)

        #Y SAYI BULMA
        for i in alanlar:
            if i == "X":
                pass
            elif i == "":
                pass
            elif i == "O":
                o_sayı = o_sayı + i

        o_sayı = len(o_sayı)


    def SıraBulma():
        global oyuncu_sirasi, pc_sirasi
        if((x_sayı)%2 == 0):
            oyuncu_sirasi = True
            pc_sirasi = False

        else:
            oyuncu_sirasi = False
            pc_sirasi = True


    def SıraYazma():
        global sıra_yazısı
        global yazı

        yazı = ""

        if(oyuncu_sirasi == True):
            yazı = "SENDE"

        elif(pc_sirasi == True):
            yazı = "PC'DE"

        sıra_yazısı = Label(p,
                            text="SIRA: "+yazı,
                            font=("arial",20,"bold"))
        sıra_yazısı.place(x = 250, y = 50)


    def Sıra():
        Window.SayıHesaplama()
        Window.SıraBulma()
        Window.SıraYazma()


    def ClickDetect():
        kutu1.bind("<Button-1>", Oyun.callback)
        kutu2.bind("<Button-1>", Oyun.callback)
        kutu3.bind("<Button-1>", Oyun.callback)
        kutu4.bind("<Button-1>", Oyun.callback)
        kutu5.bind("<Button-1>", Oyun.callback)
        kutu6.bind("<Button-1>", Oyun.callback)
        kutu7.bind("<Button-1>", Oyun.callback)
        kutu8.bind("<Button-1>", Oyun.callback)
        kutu9.bind("<Button-1>", Oyun.callback)


    def FillArea():
        pass


    def Game():
        global oyuncu_sirasi, pc_sirasi
        global x_sayı, o_sayı
        Window.AreaCheck()

        oyuncu_sirasi = None
        pc_sirasi = None

        oyun = True

        x_sayı = ""
        o_sayı = ""



        Window.Sıra()
        Oyun.İlkHamle()


    def Main():
        global p
        p = Tk()

        p.title(title)
        p.geometry(geometry)
        p.resizable(FALSE, FALSE)


        Window.Squares()
        Window.InfoArea()

        Window.Game()




        p.mainloop()





class Oyun:
    def callback(event):
        global clicked

        clicked = str(event.widget)

        clicked = clicked[-1]

        if(clicked == "s"):
            clicked = "1"

        Oyun.FillArea(kutu=clicked)

    def callback2(event):
        global clicked

        clicked = str(event.widget)

        clicked = clicked[-1]

        if(clicked == "s"):
            clicked = "1"

        Oyun.FillArea2(kutu=clicked)

    def callback3(event):
        global clicked

        clicked = str(event.widget)

        clicked = clicked[-1]

        if(clicked == "s"):
            clicked = "1"

        Oyun.FillArea3(kutu=clicked)

    def callback4(event):
        global clicked

        clicked = str(event.widget)

        clicked = clicked[-1]

        if(clicked == "s"):
            clicked = "1"

        Oyun.FillArea4(kutu=clicked)

    def callback5(event):
        global clicked

        clicked = str(event.widget)

        clicked = clicked[-1]

        if(clicked == "s"):
            clicked = "1"

        Oyun.FillArea5(kutu=clicked)


    def İlkHamle():
        if(oyuncu_sirasi == True):
            Window.ClickDetect()


    def FillArea(kutu):
        if(kutu == "1"):
            alan1['text'] = "X"
        elif(kutu == "2"):
            alan2['text'] = "X"
        elif(kutu == "3"):
            alan3['text'] = "X"
        elif(kutu == "4"):
            alan4['text'] = "X"
        elif(kutu == "5"):
            alan5['text'] = "X"
        elif(kutu == "6"):
            alan6['text'] = "X"
        elif(kutu == "7"):
            alan7['text'] = "X"
        elif(kutu == "8"):
            alan8['text'] = "X"
        elif(kutu == "9"):
            alan9['text'] = "X"

        Oyun.PCSırası()


    def PCSırası():
        kutu1.unbind("<Button-1>")
        kutu2.unbind("<Button-1>")
        kutu3.unbind("<Button-1>")
        kutu4.unbind("<Button-1>")
        kutu5.unbind("<Button-1>")
        kutu6.unbind("<Button-1>")
        kutu7.unbind("<Button-1>")
        kutu8.unbind("<Button-1>")
        kutu9.unbind("<Button-1>")

        sıra_yazısı['text'] = "SIRA: " + "PC'DE"
        Oyun.PCDüşünme()


    def PCDüşünme():
        global a1,a2,a3,a4,a5,a6,a7,a8,a9, alanlar
        a1, a2, a3 = alan1.cget("text"), alan2.cget("text"), alan3.cget("text")
        a4, a5, a6 = alan4.cget("text"), alan5.cget("text"), alan6.cget("text")
        a7, a8, a9 = alan7.cget("text"), alan8.cget("text"), alan9.cget("text")

        alanlar = [a1, a2, a3, a4, a5, a6, a7, a8, a9]
        kutu_alanlar = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9"]

        a1dolu, a2dolu, a3dolu = None, None, None
        a4dolu, a5dolu, a6dolu = None, None, None
        a7dolu, a8dolu, a9dolu = None, None, None

        if(a1 == "X"):a1dolu=True, kutu_alanlar.remove("a1")
        elif(a2 == "X"):a2dolu=True, kutu_alanlar.remove("a2")
        elif(a3 == "X"):a3dolu=True, kutu_alanlar.remove("a3")
        elif(a4 == "X"):a4dolu=True, kutu_alanlar.remove("a4")
        elif(a5 == "X"):a5dolu = True, kutu_alanlar.remove("a5")
        elif(a6 == "X"):a6dolu = True, kutu_alanlar.remove("a6")
        elif(a7 == "X"):a7dolu = True, kutu_alanlar.remove("a7")
        elif(a8 == "X"):a8dolu = True, kutu_alanlar.remove("a8")
        elif(a9 == "X"):a9dolu = True, kutu_alanlar.remove("a9")

        oynanılacak_kutu = random.choice(kutu_alanlar)

        if(oynanılacak_kutu == "a1"):
            alan1['text'] = "O"
        elif(oynanılacak_kutu == "a2"):
            alan2['text'] = "O"
        elif(oynanılacak_kutu == "a3"):
            alan3['text'] = "O"
        elif(oynanılacak_kutu == "a4"):
            alan4['text'] = "O"
        elif(oynanılacak_kutu == "a5"):
            alan5['text'] = "O"
        elif(oynanılacak_kutu == "a6"):
            alan6['text'] = "O"
        elif(oynanılacak_kutu == "a7"):
            alan7['text'] = "O"
        elif(oynanılacak_kutu == "a8"):
            alan8['text'] = "O"
        elif(oynanılacak_kutu == "a9"):
            alan9['text'] = "O"

        sıra_yazısı['text'] = "SIRA: " + "SENDE"

        Oyun.İkinciHamle()


    def PCSırası2():
        kutu1.unbind("<Button-1>")
        kutu2.unbind("<Button-1>")
        kutu3.unbind("<Button-1>")
        kutu4.unbind("<Button-1>")
        kutu5.unbind("<Button-1>")
        kutu6.unbind("<Button-1>")
        kutu7.unbind("<Button-1>")
        kutu8.unbind("<Button-1>")
        kutu9.unbind("<Button-1>")

        sıra_yazısı['text'] = "SIRA: " + "PC'DE"
        Oyun.PCDüşünme2()


    def PCDüşünme2():
        global a1,a2,a3,a4,a5,a6,a7,a8,a9, alanlar, kutu_alanlar
        a1, a2, a3 = alan1.cget("text"), alan2.cget("text"), alan3.cget("text")
        a4, a5, a6 = alan4.cget("text"), alan5.cget("text"), alan6.cget("text")
        a7, a8, a9 = alan7.cget("text"), alan8.cget("text"), alan9.cget("text")
        alanlar = [a1, a2, a3, a4, a5, a6, a7, a8, a9]
        kutu_alanlar = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9"]

        if(a1 == "X"):kutu_alanlar.remove("a1")
        if(a2 == "X"):kutu_alanlar.remove("a2")
        if(a3 == "X"):kutu_alanlar.remove("a3")
        if(a4 == "X"):kutu_alanlar.remove("a4")
        if(a5 == "X"):kutu_alanlar.remove("a5")
        if(a6 == "X"):kutu_alanlar.remove("a6")
        if(a7 == "X"):kutu_alanlar.remove("a7")
        if(a8 == "X"):kutu_alanlar.remove("a8")
        if(a9 == "X"):kutu_alanlar.remove("a9")

        korunması_gereken_yer = ""


        #İHTİMAL BİR
        if("a1" not in kutu_alanlar and "a4" not in kutu_alanlar):
            korunması_gereken_yer = a7
            if(alan7.cget('text') == ""):
                #SAVUNMA
                alan7['text'] = "O"
            else:
                #SALDIRI
                hücum_alanlar = ["a2", "a3", "a5", "a6", "a8", "a9"]
                oynanılacak_alan = random.choice(hücum_alanlar)
                if(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a3"):alan3['text'] = "O"
                elif(oynanılacak_alan == "a5"):alan5['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"
                elif(oynanılacak_alan == "a9"):alan9['text'] = "O"

        #İHTİMAL İKİ
        elif('a4' not in kutu_alanlar and 'a7'not in kutu_alanlar):
            korunması_gereken_yer = a1
            if(alan1.cget('text') == ""):
                #SAVUNMA
                alan1['text'] = "O"
            else:
                #SALDIRI
                hücum_alanlar = ["a2", "a3", "a5", "a6", "a8", "a9"]
                oynanılacak_alan = random.choice(hücum_alanlar)
                if(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a3"):alan3['text'] = "O"
                elif(oynanılacak_alan == "a5"):alan5['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"
                elif(oynanılacak_alan == "a9"):alan9['text'] = "O"

        #İHTİMAL ÜÇ
        elif("a5" not in kutu_alanlar and 'a2' not in kutu_alanlar):
            korunması_gereken_yer = a8
            if(alan8.cget('text') == ""):
                #SAVUNMA
                alan8['text'] = "O"
            else:
                #SALDIRI
                hücum_alanlar = ["a1", "a3", "a5", "a6", "a7", "a9"]
                oynanılacak_alan = random.choice(hücum_alanlar)
                if(oynanılacak_alan == "a1"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a3"):alan3['text'] = "O"
                elif(oynanılacak_alan == "a5"):alan5['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"
                elif(oynanılacak_alan == "a7"):alan7['text'] = "O"
                elif(oynanılacak_alan == "a9"):alan9['text'] = "O"

        #İHTİMAL DÖRT
        elif("a6" not in kutu_alanlar and 'a3' not in kutu_alanlar):
            korunması_gereken_yer = a9
            if(alan9.cget('text') == ""):
                #SAVUNMA
                alan9['text'] = "O"
            else:
                #SALDIRI
                hücum_alanlar = ["a1", "a2", "a4", "a5", "a7", "a8"]
                oynanılacak_alan = random.choice(hücum_alanlar)
                if(oynanılacak_alan == "a1"):alan1['text'] = "O"
                elif(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a5"):alan5['text'] = "O"
                elif(oynanılacak_alan == "a7"):alan7['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"

        #İHTİMAL BEŞ
        elif("a8" not in kutu_alanlar and 'a5' not in kutu_alanlar):
            korunması_gereken_yer = a2
            if(alan2.cget('text') == ""):
                #SAVUNMA
                alan2['text'] = "O"
            else:
                #SALDIRI
                hücum_alanlar = ["a1", "a3", "a4", "a6", "a7", "a9"]
                oynanılacak_alan = random.choice(hücum_alanlar)
                if(oynanılacak_alan == "a1"):alan1['text'] = "O"
                elif(oynanılacak_alan == "a3"):alan3['text'] = "O"
                elif(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"
                elif(oynanılacak_alan == "a7"):alan7['text'] = "O"
                elif(oynanılacak_alan == "a9"):alan9['text'] = "O"

        #İHTİMAL ALTI
        elif("a9" not in kutu_alanlar and 'a6'not in kutu_alanlar):
            korunması_gereken_yer = a3
            if(alan3.cget('text') == ""):
                #SAVUNMA
                alan3['text'] = "O"
            else:
                #SALDIRI
                hücum_alanlar = ["a1", "a2", "a4", "a5", "a7", "a8"]
                oynanılacak_alan = random.choice(hücum_alanlar)
                if(oynanılacak_alan == "a1"):alan1['text'] = "O"
                elif(oynanılacak_alan == "a3"):alan3['text'] = "O"
                elif(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"
                elif(oynanılacak_alan == "a7"):alan7['text'] = "O"
                elif(oynanılacak_alan == "a9"):alan9['text'] = "O"

        #İHTİMAL YEDİ
        elif("a8" not in kutu_alanlar and 'a7' not in kutu_alanlar):
            korunması_gereken_yer = a9
            if(alan9.cget('text') == ""):
                #SAVUNMA
                alan9['text'] = "O"
            else:
                #SALDIRI
                hücum_alanlar = ["a1", "a2", "a3", "a4", "a5", "a6"]
                oynanılacak_alan = random.choice(hücum_alanlar)
                if(oynanılacak_alan == "a1"):alan1['text'] = "O"
                elif(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a3"):alan3['text'] = "O"
                elif(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a5"):alan5['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"

        #İHTİMAL SEKİZ
        elif("a4" not in kutu_alanlar and 'a5' not in kutu_alanlar):
            korunması_gereken_yer = a6
            if(alan6.cget('text') == ""):
                #SAVUNMA
                alan6['text'] = "O"
            else:
                #SALDIRI
                hücum_alanlar = ["a1", "a2", "a3", "a7", "a8", "a9"]
                oynanılacak_alan = random.choice(hücum_alanlar)
                if(oynanılacak_alan == "a1"):alan1['text'] = "O"
                elif(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a3"):alan3['text'] = "O"
                elif(oynanılacak_alan == "a7"):alan7['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"
                elif(oynanılacak_alan == "a9"):alan9['text'] = "O"

        #İHTİMAL DOKUZ
        elif("a1" not in kutu_alanlar and 'a2' not in kutu_alanlar):
            korunması_gereken_yer = a3
            if(alan3.cget('text') == ""):
                #SAVUNMA
                alan3['text'] = "O"
            else:
                #SALDIRI
                hücum_alanlar = ["a4", "a5", "a6", "a7", "a8", "a9"]
                oynanılacak_alan = random.choice(hücum_alanlar)
                if(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a5"):alan5['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"
                elif(oynanılacak_alan == "a7"):alan7['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"
                elif(oynanılacak_alan == "a9"):alan9['text'] = "O"

        #İHTİMAL ON
        elif("a2" not in kutu_alanlar and 'a3' not in kutu_alanlar):
            korunması_gereken_yer = a1
            if(alan1.cget('text') == ""):
                #SAVUNMA
                alan1['text'] = "O"
            else:
                #SALDIRI
                hücum_alanlar = ["a4", "a5", "a6", "a7", "a8", "a9"]
                oynanılacak_alan = random.choice(hücum_alanlar)
                if(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a5"):alan5['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"
                elif(oynanılacak_alan == "a7"):alan7['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"
                elif(oynanılacak_alan == "a9"):alan9['text'] = "O"

        #İHTİMAL ONBİR
        elif("a5" not in kutu_alanlar and 'a6' not in kutu_alanlar):
            korunması_gereken_yer = a4
            if(alan4.cget('text') == ""):
                #SAVUNMA
                alan4['text'] = "O"
            else:
                #SALDIRI
                hücum_alanlar = ["a1", "a2", "a3", "a7", "a8", "a9"]
                oynanılacak_alan = random.choice(hücum_alanlar)
                if(oynanılacak_alan == "a1"):alan1['text'] = "O"
                elif(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a3"):alan3['text'] = "O"
                elif(oynanılacak_alan == "a7"):alan7['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"
                elif(oynanılacak_alan == "a9"):alan9['text'] = "O"

        #İHTİMAL ONİKİ
        elif("a8" not in kutu_alanlar and 'a9' not in kutu_alanlar):
            korunması_gereken_yer = a7
            if(alan7.cget('text') == ""):
                #SAVUNMA
                alan7['text'] = "O"
            else:
                #SALDIRI
                hücum_alanlar = ["a1", "a2", "a3", "a4", "a5", "a6"]
                oynanılacak_alan = random.choice(hücum_alanlar)
                if(oynanılacak_alan == "a1"):alan1['text'] = "O"
                elif(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a3"):alan3['text'] = "O"
                elif(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a5"):alan5['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"

        #İHTİMAL ONÜÇ
        elif("a1" not in kutu_alanlar and 'a5' not in kutu_alanlar):
            korunması_gereken_yer = a9
            if(alan9.cget('text') == ""):
                #SAVUNMA
                alan9['text'] = "O"
            else:
                #SALDIRI
                hücum_alanlar = ["a2", "a3", "a4", "a6", "a7", "a8"]
                oynanılacak_alan = random.choice(hücum_alanlar)
                if(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a3"):alan3['text'] = "O"
                elif(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"
                elif(oynanılacak_alan == "a7"):alan7['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"

        #İHTİMAL ONDÖRT
        elif("a5" not in kutu_alanlar and 'a9' not in kutu_alanlar):
            korunması_gereken_yer = a1
            if(alan1.cget('text') == ""):
                #SAVUNMA
                alan1['text'] = "O"
            else:
                #SALDIRI
                hücum_alanlar = ["a2", "a3", "a4", "a6", "a7", "a8"]
                oynanılacak_alan = random.choice(hücum_alanlar)
                if(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a3"):alan3['text'] = "O"
                elif(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"
                elif(oynanılacak_alan == "a7"):alan7['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"

        #İHTİMAL ONBEŞ
        elif("a7" not in kutu_alanlar and 'a5' not in kutu_alanlar):
            korunması_gereken_yer = a3
            if(alan3.cget('text') == ""):
                #SAVUNMA
                alan3['text'] = "O"
            else:
                #SALDIRI
                hücum_alanlar = ["a1", "a2", "a4", "a6", "a8", "a9"]
                oynanılacak_alan = random.choice(hücum_alanlar)
                if(oynanılacak_alan == "a1"):alan1['text'] = "O"
                elif(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"
                elif(oynanılacak_alan == "a9"):alan9['text'] = "O"

        #İHTİMAL ONALTI
        elif("a3" not in kutu_alanlar and 'a5' not in kutu_alanlar):
            korunması_gereken_yer = a7
            if(alan7.cget('text') == ""):
                #SAVUNMA
                alan7['text'] = "O"
            else:
                #SALDIRI
                hücum_alanlar = ["a1", "a2", "a4", "a6", "a8", "a9"]
                oynanılacak_alan = random.choice(hücum_alanlar)
                if(oynanılacak_alan == "a1"):alan1['text'] = "O"
                elif(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"
                elif(oynanılacak_alan == "a9"):alan9['text'] = "O"

        #İHTİMAL ONYEDİ
        elif("a1" not in kutu_alanlar and 'a7' not in kutu_alanlar):
            korunması_gereken_yer = a4
            if(alan4.cget('text') == ""):
                #SAVUNMA
                alan4['text'] = "O"
            else:
                #SALDIRI
                hücum_alanlar = ["a2", "a3", "a5", "a6", "a8", "a9"]
                oynanılacak_alan = random.choice(hücum_alanlar)
                if(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a3"):alan3['text'] = "O"
                elif(oynanılacak_alan == "a5"):alan5['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"
                elif(oynanılacak_alan == "a9"):alan9['text'] = "O"

        #İHTİMAL ONSEKİZ
        elif("a2" not in kutu_alanlar and 'a5' not in kutu_alanlar):
            korunması_gereken_yer = a8
            if(alan8.cget('text') == ""):
                #SAVUNMA
                alan8['text'] = "O"
            else:
                #SALDIRI
                hücum_alanlar = ["a1", "a3", "a4", "a6", "a7", "a9"]
                oynanılacak_alan = random.choice(hücum_alanlar)
                if(oynanılacak_alan == "a1"):alan1['text'] = "O"
                elif(oynanılacak_alan == "a3"):alan3['text'] = "O"
                elif(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"
                elif(oynanılacak_alan == "a7"):alan7['text'] = "O"
                elif(oynanılacak_alan == "a9"):alan9['text'] = "O"

        #İHTİMAL ONDOKUZ
        elif("a3" not in kutu_alanlar and 'a9' not in kutu_alanlar):
            korunması_gereken_yer = a6
            if(alan6.cget('text') == ""):
                #SAVUNMA
                alan6['text'] = "O"
            else:
                #SALDIRI
                hücum_alanlar = ["a1", "a2", "a4", "a5", "a7", "a8"]
                oynanılacak_alan = random.choice(hücum_alanlar)
                if(oynanılacak_alan == "a1"):alan1['text'] = "O"
                elif(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a5"):alan5['text'] = "O"
                elif(oynanılacak_alan == "a7"):alan7['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"

        #İHTİMAL YİRMİ
        elif("a1" not in kutu_alanlar and 'a3' not in kutu_alanlar):
            korunması_gereken_yer = a2
            if(alan2.cget('text') == ""):
                #SAVUNMA
                alan2['text'] = "O"
            else:
                #SALDIRI
                hücum_alanlar = ["a4", "a5", "a6", "a7", "a8", "a9"]
                oynanılacak_alan = random.choice(hücum_alanlar)
                if(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a5"):alan5['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"
                elif(oynanılacak_alan == "a7"):alan7['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"
                elif(oynanılacak_alan == "a9"):alan9['text'] = "O"

        #İHTİMAL YİRMİBİR
        elif("a4" not in kutu_alanlar and 'a6' not in kutu_alanlar):
            korunması_gereken_yer = a5
            if(alan5.cget('text') == ""):
                #SAVUNMA
                alan5['text'] = "O"
            else:
                #SALDIRI
                hücum_alanlar = ["a1", "a2", "a3", "a7", "a8", "a9"]
                oynanılacak_alan = random.choice(hücum_alanlar)
                if(oynanılacak_alan == "a1"):alan1['text'] = "O"
                elif(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a3"):alan3['text'] = "O"
                elif(oynanılacak_alan == "a7"):alan7['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"
                elif(oynanılacak_alan == "a9"):alan9['text'] = "O"

        #İHTİMAL YİRMİİKİ
        elif("a7" not in kutu_alanlar and 'a9' not in kutu_alanlar):
            korunması_gereken_yer = a8
            if(alan8.cget('text') == ""):
                #SAVUNMA
                alan8['text'] = "O"
            else:
                #SALDIRI
                hücum_alanlar = ["a1", "a2", "a3", "a4", "a5", "a6"]
                oynanılacak_alan = random.choice(hücum_alanlar)
                if(oynanılacak_alan == "a1"):alan1['text'] = "O"
                elif(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a3"):alan3['text'] = "O"
                elif(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a5"):alan5['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"

        #İHTİMAL YİRMİÜÇ
        elif("a3" not in kutu_alanlar and 'a7' not in kutu_alanlar):
            korunması_gereken_yer = a5
            if(alan5.cget('text') == ""):
                #SAVUNMA
                alan5['text'] = "O"
            else:
                #SALDIRI
                hücum_alanlar = ["a1", "a2", "a4", "a6", "a8", "a9"]
                oynanılacak_alan = random.choice(hücum_alanlar)
                if(oynanılacak_alan == "a1"):alan1['text'] = "O"
                elif(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"
                elif(oynanılacak_alan == "a9"):alan9['text'] = "O"

        #İHTİMAL YİRMİDÖRT
        elif("a1" not in kutu_alanlar and 'a9' not in kutu_alanlar):
            korunması_gereken_yer = a5
            if(alan5.cget('text') == ""):
                #SAVUNMA
                alan5['text'] = "O"
            else:
                #SALDIRI
                hücum_alanlar = ["a2", "a3", "a4", "a6", "a7", "a8"]
                oynanılacak_alan = random.choice(hücum_alanlar)
                if(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a3"):alan3['text'] = "O"
                elif(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"
                elif(oynanılacak_alan == "a7"):alan7['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"

        #İHTİMAL YİRMİBEŞ
        elif("a2" not in kutu_alanlar and 'a8' not in kutu_alanlar):
            korunması_gereken_yer = a5
            if(alan5.cget('text') == ""):
                #SAVUNMA
                alan5['text'] = "O"
            else:
                #SALDIRI
                hücum_alanlar = ["a2", "a3", "a4", "a6", "a7", "a8"]
                oynanılacak_alan = random.choice(hücum_alanlar)
                if(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a3"):alan3['text'] = "O"
                elif(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"
                elif(oynanılacak_alan == "a7"):alan7['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"

        #DİĞER İHTİMALLER
        else:
            oynanılacak_yer = random.choice(kutu_alanlar)
            if(oynanılacak_yer == "a1"):alan1['text'] = "O"
            elif(oynanılacak_yer == "a2"):alan2['text'] = "O"
            elif(oynanılacak_yer == "a3"):alan3['text'] = "O"
            elif(oynanılacak_yer == "a4"):alan4['text'] = "O"
            elif(oynanılacak_yer == "a5"):alan5['text'] = "O"
            elif(oynanılacak_yer == "a6"):alan6['text'] = "O"
            elif(oynanılacak_yer == "a7"):alan7['text'] = "O"
            elif(oynanılacak_yer == "a8"):alan8['text'] = "O"
            elif(oynanılacak_yer == "a9"):alan9['text'] = "O"


        sıra_yazısı['text'] = "SIRA: " + "SENDE"



        Oyun.ÜçüncüHamle()


    def FillArea2(kutu):
        if(kutu == "1"):
            alan1['text'] = "X"
        elif(kutu == "2"):
            alan2['text'] = "X"
        elif(kutu == "3"):
            alan3['text'] = "X"
        elif(kutu == "4"):
            alan4['text'] = "X"
        elif(kutu == "5"):
            alan5['text'] = "X"
        elif(kutu == "6"):
            alan6['text'] = "X"
        elif(kutu == "7"):
            alan7['text'] = "X"
        elif(kutu == "8"):
            alan8['text'] = "X"
        elif(kutu == "9"):
            alan9['text'] = "X"

        Oyun.PCSırası2()


    def İkinciHamle():
        Oyun.ClickDetect()


    def ÜçüncüHamle():
        Oyun.ClickDetect2()


    def ClickDetect2():
        kutu1.bind("<Button-1>", Oyun.callback3)
        kutu2.bind("<Button-1>", Oyun.callback3)
        kutu3.bind("<Button-1>", Oyun.callback3)
        kutu4.bind("<Button-1>", Oyun.callback3)
        kutu5.bind("<Button-1>", Oyun.callback3)
        kutu6.bind("<Button-1>", Oyun.callback3)
        kutu7.bind("<Button-1>", Oyun.callback3)
        kutu8.bind("<Button-1>", Oyun.callback3)
        kutu9.bind("<Button-1>", Oyun.callback3)


    def ClickDetect():
        kutu1.bind("<Button-1>", Oyun.callback2)
        kutu2.bind("<Button-1>", Oyun.callback2)
        kutu3.bind("<Button-1>", Oyun.callback2)
        kutu4.bind("<Button-1>", Oyun.callback2)
        kutu5.bind("<Button-1>", Oyun.callback2)
        kutu6.bind("<Button-1>", Oyun.callback2)
        kutu7.bind("<Button-1>", Oyun.callback2)
        kutu8.bind("<Button-1>", Oyun.callback2)
        kutu9.bind("<Button-1>", Oyun.callback2)


    def FillArea3(kutu):
        if(kutu == "1"):
            alan1['text'] = "X"
        elif(kutu == "2"):
            alan2['text'] = "X"
        elif(kutu == "3"):
            alan3['text'] = "X"
        elif(kutu == "4"):
            alan4['text'] = "X"
        elif(kutu == "5"):
            alan5['text'] = "X"
        elif(kutu == "6"):
            alan6['text'] = "X"
        elif(kutu == "7"):
            alan7['text'] = "X"
        elif(kutu == "8"):
            alan8['text'] = "X"
        elif(kutu == "9"):
            alan9['text'] = "X"

        Oyun.PCSırası3()


    def PCSırası3():
        kutu1.unbind("<Button-1>")
        kutu2.unbind("<Button-1>")
        kutu3.unbind("<Button-1>")
        kutu4.unbind("<Button-1>")
        kutu5.unbind("<Button-1>")
        kutu6.unbind("<Button-1>")
        kutu7.unbind("<Button-1>")
        kutu8.unbind("<Button-1>")
        kutu9.unbind("<Button-1>")

        sıra_yazısı['text'] = "SIRA: " + "PC'DE"
        Oyun.PCDüşünme3()


    def PCDüşünme3():
        global a1, a2, a3, a4, a5, a6, a7, a8, a9, alanlar, x_kutu_alanlar, o_kutu_alanlar
        a1, a2, a3 = alan1.cget("text"), alan2.cget("text"), alan3.cget("text")
        a4, a5, a6 = alan4.cget("text"), alan5.cget("text"), alan6.cget("text")
        a7, a8, a9 = alan7.cget("text"), alan8.cget("text"), alan9.cget("text")
        alanlar = [a1, a2, a3, a4, a5, a6, a7, a8, a9]
        x_kutu_alanlar = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9"]
        o_kutu_alanlar = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9"]
        boş_kutular = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9"]

        #X KUTU KONUMU BULMA
        if (a1 == "X"): x_kutu_alanlar.remove("a1"), boş_kutular.remove("a1")
        if (a2 == "X"): x_kutu_alanlar.remove("a2"), boş_kutular.remove("a2")
        if (a3 == "X"): x_kutu_alanlar.remove("a3"), boş_kutular.remove("a3")
        if (a4 == "X"): x_kutu_alanlar.remove("a4"), boş_kutular.remove("a4")
        if (a5 == "X"): x_kutu_alanlar.remove("a5"), boş_kutular.remove("a5")
        if (a6 == "X"): x_kutu_alanlar.remove("a6"), boş_kutular.remove("a6")
        if (a7 == "X"): x_kutu_alanlar.remove("a7"), boş_kutular.remove("a7")
        if (a8 == "X"): x_kutu_alanlar.remove("a8"), boş_kutular.remove("a8")
        if (a9 == "X"): x_kutu_alanlar.remove("a9"), boş_kutular.remove("a9")

        #O KUTU KONUMU BULMA
        if (a1 == "O"): o_kutu_alanlar.remove("a1"), boş_kutular.remove("a1")
        if (a2 == "O"): o_kutu_alanlar.remove("a2"), boş_kutular.remove("a2")
        if (a3 == "O"): o_kutu_alanlar.remove("a3"), boş_kutular.remove("a3")
        if (a4 == "O"): o_kutu_alanlar.remove("a4"), boş_kutular.remove("a4")
        if (a5 == "O"): o_kutu_alanlar.remove("a5"), boş_kutular.remove("a5")
        if (a6 == "O"): o_kutu_alanlar.remove("a6"), boş_kutular.remove("a6")
        if (a7 == "O"): o_kutu_alanlar.remove("a7"), boş_kutular.remove("a7")
        if (a8 == "O"): o_kutu_alanlar.remove("a8"), boş_kutular.remove("a8")
        if (a9 == "O"): o_kutu_alanlar.remove("a9"), boş_kutular.remove("a9")

        #BOŞ ALAN BULMA

        #O KAZANIYOR MU BAK VE ONUN KAZANMAK İÇİN KOYACAĞI KUTU BOŞ MU BAK

        #PC KAZANMA İHTİMALLERİ

        #İHTİMAL BİR
        if("a1" not in o_kutu_alanlar and 'a2' not in o_kutu_alanlar):
            hedef_yer = a3
            if(alan3.cget('text') == ""):
                #SALDIRI
                alan3['text'] = "O"
            else:
                #RANDOM
                oynanılacak_alan = random.choice(boş_kutular)
                if(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a5"):alan5['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"
                elif(oynanılacak_alan == "a7"):alan7['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"
                elif(oynanılacak_alan == "a9"):alan9['text'] = "O"

        #İHTİMAL İKİ
        elif("a2" not in o_kutu_alanlar and 'a3' not in o_kutu_alanlar):
            hedef_yer = a1
            if(alan1.cget('text') == ""):
                #SALDIRI
                alan1['text'] = "O"
            else:
                #RANDOM
                oynanılacak_alan = random.choice(boş_kutular)
                if(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a5"):alan5['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"
                elif(oynanılacak_alan == "a7"):alan7['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"
                elif(oynanılacak_alan == "a9"):alan9['text'] = "O"

        #İHTİMAL ÜÇ
        elif("a4" not in o_kutu_alanlar and 'a5' not in o_kutu_alanlar):
            hedef_yer = a6
            if(alan6.cget('text') == ""):
                #SALDIRI
                alan6['text'] = "O"
            else:
                #RANDOM
                oynanılacak_alan = random.choice(boş_kutular)
                if(oynanılacak_alan == "a1"):alan1['text'] = "O"
                elif(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a3"):alan3['text'] = "O"
                elif(oynanılacak_alan == "a7"):alan7['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"
                elif(oynanılacak_alan == "a9"):alan9['text'] = "O"

        #İHTİMAL DÖRT
        elif("a5" not in o_kutu_alanlar and 'a6' not in o_kutu_alanlar):
            hedef_yer = a4
            if(alan4.cget('text') == ""):
                #SALDIRI
                alan4['text'] = "O"
            else:
                #RANDOM
                oynanılacak_alan = random.choice(boş_kutular)
                if(oynanılacak_alan == "a1"):alan1['text'] = "O"
                elif(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a3"):alan3['text'] = "O"
                elif(oynanılacak_alan == "a7"):alan7['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"
                elif(oynanılacak_alan == "a9"):alan9['text'] = "O"

        #İHTİMAL BEŞ
        elif("a7" not in o_kutu_alanlar and 'a8' not in o_kutu_alanlar):
            hedef_yer = a9
            if(alan9.cget('text') == ""):
                #SALDIRI
                alan9['text'] = "O"
            else:
                #RANDOM
                oynanılacak_alan = random.choice(boş_kutular)
                if(oynanılacak_alan == "a1"):alan1['text'] = "O"
                elif(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a3"):alan3['text'] = "O"
                elif(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a5"):alan5['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"

        #İHTİMAL ALTI
        elif("a8" not in o_kutu_alanlar and 'a9' not in o_kutu_alanlar):
            hedef_yer = a7
            if(alan7.cget('text') == ""):
                #SALDIRI
                alan7['text'] = "O"
            else:
                #RANDOM
                oynanılacak_alan = random.choice(boş_kutular)
                if(oynanılacak_alan == "a1"):alan1['text'] = "O"
                elif(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a3"):alan3['text'] = "O"
                elif(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a5"):alan5['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"

        #İHTİMAL YEDİ
        elif("a7" not in o_kutu_alanlar and 'a8' not in o_kutu_alanlar):
            hedef_yer = a9
            if(alan9.cget('text') == ""):
                #SALDIRI
                alan9['text'] = "O"
            else:
                #RANDOM
                oynanılacak_alan = random.choice(boş_kutular)
                if(oynanılacak_alan == "a1"):alan1['text'] = "O"
                elif(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a3"):alan3['text'] = "O"
                elif(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a5"):alan5['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"

        #İHTİMAL SEKİZ
        elif("a1" not in o_kutu_alanlar and 'a4' not in o_kutu_alanlar):
            hedef_yer = a7
            if(alan7.cget('text') == ""):
                #SALDIRI
                alan7['text'] = "O"
            else:
                #RANDOM
                oynanılacak_alan = random.choice(boş_kutular)
                if(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a3"):alan3['text'] = "O"
                elif(oynanılacak_alan == "a5"):alan5['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"
                elif(oynanılacak_alan == "a9"):alan9['text'] = "O"

        #İHTİMAL DOKUZ
        elif("a4" not in o_kutu_alanlar and 'a7' not in o_kutu_alanlar):
            hedef_yer = a1
            if(alan1.cget('text') == ""):
                #SALDIRI
                alan1['text'] = "O"
            else:
                #RANDOM
                oynanılacak_alan = random.choice(boş_kutular)
                if(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a3"):alan3['text'] = "O"
                elif(oynanılacak_alan == "a5"):alan5['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"
                elif(oynanılacak_alan == "a9"):alan9['text'] = "O"

        #İHTİMAL ON
        elif("a2" not in o_kutu_alanlar and 'a5' not in o_kutu_alanlar):
            hedef_yer = a8
            if(alan8.cget('text') == ""):
                #SALDIRI
                alan8['text'] = "O"
            else:
                #RANDOM
                oynanılacak_alan = random.choice(boş_kutular)
                if(oynanılacak_alan == "a1"):alan1['text'] = "O"
                elif(oynanılacak_alan == "a3"):alan3['text'] = "O"
                elif(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"
                elif(oynanılacak_alan == "a7"):alan7['text'] = "O"
                elif(oynanılacak_alan == "a9"):alan9['text'] = "O"

        #İHTİMAL ONBİR
        elif("a5" not in o_kutu_alanlar and 'a8' not in o_kutu_alanlar):
            hedef_yer = a2
            if(alan2.cget('text') == ""):
                #SALDIRI
                alan2['text'] = "O"
            else:
                #RANDOM
                oynanılacak_alan = random.choice(boş_kutular)
                if(oynanılacak_alan == "a1"):alan1['text'] = "O"
                elif(oynanılacak_alan == "a3"):alan3['text'] = "O"
                elif(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"
                elif(oynanılacak_alan == "a7"):alan7['text'] = "O"
                elif(oynanılacak_alan == "a9"):alan9['text'] = "O"

        #İHTİMAL ONİKİ
        elif("a3" not in o_kutu_alanlar and 'a6' not in o_kutu_alanlar):
            hedef_yer = a9
            if(alan9.cget('text') == ""):
                #SALDIRI
                alan9['text'] = "O"
            else:
                #RANDOM
                oynanılacak_alan = random.choice(boş_kutular)
                if(oynanılacak_alan == "a1"):alan1['text'] = "O"
                elif(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a5"):alan5['text'] = "O"
                elif(oynanılacak_alan == "a7"):alan7['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"

        #İHTİMAL ONÜÇ
        elif("a6" not in o_kutu_alanlar and 'a9' not in o_kutu_alanlar):
            hedef_yer = a3
            if(alan3.cget('text') == ""):
                #SALDIRI
                alan3['text'] = "O"
            else:
                #RANDOM
                oynanılacak_alan = random.choice(boş_kutular)
                if(oynanılacak_alan == "a1"):alan1['text'] = "O"
                elif(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a5"):alan5['text'] = "O"
                elif(oynanılacak_alan == "a7"):alan7['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"

        #İHTİMAL ONDÖRT
        elif("a1" not in o_kutu_alanlar and 'a5' not in o_kutu_alanlar):
            hedef_yer = a9
            if(alan9.cget('text') == ""):
                #SALDIRI
                alan9['text'] = "O"
            else:
                #RANDOM
                oynanılacak_alan = random.choice(boş_kutular)
                if(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a3"):alan3['text'] = "O"
                elif(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"
                elif(oynanılacak_alan == "a7"):alan7['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"

        #İHTİMAL ONBEŞ
        elif("a5" not in o_kutu_alanlar and 'a9' not in o_kutu_alanlar):
            hedef_yer = a1
            if(alan1.cget('text') == ""):
                #SALDIRI
                alan1['text'] = "O"
            else:
                #RANDOM
                oynanılacak_alan = random.choice(boş_kutular)
                if(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a3"):alan3['text'] = "O"
                elif(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"
                elif(oynanılacak_alan == "a7"):alan7['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"

        #İHTİMAL ONALTI
        elif("a7" not in o_kutu_alanlar and 'a5' not in o_kutu_alanlar):
            hedef_yer = a3
            if(alan3.cget('text') == ""):
                #SALDIRI
                alan3['text'] = "O"
            else:
                #RANDOM
                oynanılacak_alan = random.choice(boş_kutular)
                if(oynanılacak_alan == "a1"):alan1['text'] = "O"
                elif(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"
                elif(oynanılacak_alan == "a9"):alan9['text'] = "O"

        #İHTİMAL ONALTI
        elif("a3" not in o_kutu_alanlar and 'a5' not in o_kutu_alanlar):
            hedef_yer = a7
            if(alan7.cget('text') == ""):
                #SALDIRI
                alan7['text'] = "O"
            else:
                #RANDOM
                oynanılacak_alan = random.choice(boş_kutular)
                if(oynanılacak_alan == "a1"):alan1['text'] = "O"
                elif(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"
                elif(oynanılacak_alan == "a9"):alan9['text'] = "O"

        #İHTİMAL ONYEDİ
        elif("a1" not in o_kutu_alanlar and 'a3' not in o_kutu_alanlar):
            hedef_yer = a2
            if(alan2.cget('text') == ""):
                #SALDIRI
                alan2['text'] = "O"
            else:
                #RANDOM
                oynanılacak_alan = random.choice(boş_kutular)
                if(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a5"):alan5['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"
                elif(oynanılacak_alan == "a7"):alan7['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"
                elif(oynanılacak_alan == "a9"):alan9['text'] = "O"

        #İHTİMAL ONSEKİZ
        elif("a4" not in o_kutu_alanlar and 'a6' not in o_kutu_alanlar):
            hedef_yer = a5
            if(alan5.cget('text') == ""):
                #SALDIRI
                alan5['text'] = "O"
            else:
                #RANDOM
                oynanılacak_alan = random.choice(boş_kutular)
                if(oynanılacak_alan == "a1"):alan1['text'] = "O"
                elif(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a3"):alan3['text'] = "O"
                elif(oynanılacak_alan == "a7"):alan7['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"
                elif(oynanılacak_alan == "a9"):alan9['text'] = "O"

        #İHTİMAL ONSEKİZ
        elif("a7" not in o_kutu_alanlar and 'a9' not in o_kutu_alanlar):
            hedef_yer = a8
            if(alan8.cget('text') == ""):
                #SALDIRI
                alan8['text'] = "O"
            else:
                #RANDOM
                oynanılacak_alan = random.choice(boş_kutular)
                if(oynanılacak_alan == "a1"):alan1['text'] = "O"
                elif(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a3"):alan3['text'] = "O"
                elif(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a5"):alan5['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"

        #İHTİMAL ONDOKUZ
        elif("a1" not in o_kutu_alanlar and 'a7' not in o_kutu_alanlar):
            hedef_yer = a4
            if(alan4.cget('text') == ""):
                #SALDIRI
                alan4['text'] = "O"
            else:
                #RANDOM
                oynanılacak_alan = random.choice(boş_kutular)
                if(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a3"):alan3['text'] = "O"
                elif(oynanılacak_alan == "a5"):alan5['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"
                elif(oynanılacak_alan == "a9"):alan9['text'] = "O"

        #İHTİMAL YİRMİ
        elif("a2" not in o_kutu_alanlar and 'a8' not in o_kutu_alanlar):
            hedef_yer = a5
            if(alan5.cget('text') == ""):
                #SALDIRI
                alan5['text'] = "O"
            else:
                #RANDOM
                oynanılacak_alan = random.choice(boş_kutular)
                if(oynanılacak_alan == "a1"):alan1['text'] = "O"
                elif(oynanılacak_alan == "a3"):alan3['text'] = "O"
                elif(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"
                elif(oynanılacak_alan == "a7"):alan7['text'] = "O"
                elif(oynanılacak_alan == "a9"):alan9['text'] = "O"

        #İHTİMAL YİRMİBİR
        elif("a3" not in o_kutu_alanlar and 'a9' not in o_kutu_alanlar):
            hedef_yer = a6
            if(alan6.cget('text') == ""):
                #SALDIRI
                alan6['text'] = "O"
            else:
                #RANDOM
                oynanılacak_alan = random.choice(boş_kutular)
                if(oynanılacak_alan == "a1"):alan1['text'] = "O"
                elif(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a5"):alan5['text'] = "O"
                elif(oynanılacak_alan == "a7"):alan7['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"

        #İHTİMAL YİRMİKİ
        elif("a1" not in o_kutu_alanlar and 'a9' not in o_kutu_alanlar):
            hedef_yer = a5
            if(alan5.cget('text') == ""):
                #SALDIRI
                alan5['text'] = "O"
            else:
                #RANDOM
                oynanılacak_alan = random.choice(boş_kutular)
                if(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a3"):alan3['text'] = "O"
                elif(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"
                elif(oynanılacak_alan == "a7"):alan7['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"

        #İHTİMAL YİRMİÜÇ
        elif("a3" not in o_kutu_alanlar and 'a7' not in o_kutu_alanlar):
            hedef_yer = a5
            if(alan5.cget('text') == ""):
                #SALDIRI
                alan5['text'] = "O"
            else:
                #RANDOM
                oynanılacak_alan = random.choice(boş_kutular)
                if(oynanılacak_alan == "a1"):alan1['text'] = "O"
                elif(oynanılacak_alan == "a2"):alan2['text'] = "O"
                elif(oynanılacak_alan == "a4"):alan4['text'] = "O"
                elif(oynanılacak_alan == "a6"):alan6['text'] = "O"
                elif(oynanılacak_alan == "a8"):alan8['text'] = "O"
                elif(oynanılacak_alan == "a9"):alan9['text'] = "O"

        #DİĞER İHTİMALLER
        else:
            #RANDOM
            oynanılacak_alan = random.choice(boş_kutular)
            if (oynanılacak_alan == "a1"):alan1['text'] = "O"
            elif (oynanılacak_alan == "a2"):alan2['text'] = "O"
            elif (oynanılacak_alan == "a3"):alan3['text'] = "O"
            elif (oynanılacak_alan == "a4"):alan4['text'] = "O"
            elif (oynanılacak_alan == "a5"):alan5['text'] = "O"
            elif (oynanılacak_alan == "a6"):alan6['text'] = "O"
            elif (oynanılacak_alan == "a7"):alan7['text'] = "O"
            elif (oynanılacak_alan == "a8"):alan8['text'] = "O"
            elif (oynanılacak_alan == "a9"):alan9['text'] = "O"


        a1, a2, a3 = alan1.cget("text"), alan2.cget("text"), alan3.cget("text")
        a4, a5, a6 = alan4.cget("text"), alan5.cget("text"), alan6.cget("text")
        a7, a8, a9 = alan7.cget("text"), alan8.cget("text"), alan9.cget("text")

        global PC_Yendi
        PC_Yendi = None

        #O YENDİ Mİ BAK
        #YENME DURUMLARI
        #İHTİMAL BİR
        if(a1 == "O" and a2 == "O" and a3 == "O"):
            alan1.config(foreground = "red")
            alan2.config(foreground="red")
            alan3.config(foreground="red")
            Oyun.PCKazandı()

        #İHTİMAL İKİ
        elif(a4 == "O" and a5 == "O" and a6 == "O"):
            alan4.config(foreground = "red")
            alan5.config(foreground="red")
            alan6.config(foreground="red")
            Oyun.PCKazandı()

        #İHTİMAL ÜÇ
        elif(a7 == "O" and a8 == "O" and a9 == "O"):
            alan7.config(foreground = "red")
            alan8.config(foreground="red")
            alan9.config(foreground="red")
            Oyun.PCKazandı()

        #İHTİMAL DÖRT
        elif(a1 == "O" and a4 == "O" and a7 == "O"):
            alan1.config(foreground = "red")
            alan4.config(foreground="red")
            alan7.config(foreground="red")
            Oyun.PCKazandı()

        #İHTİMAL BEŞ
        elif(a2 == "O" and a5 == "O" and a8 == "O"):
            alan2.config(foreground = "red")
            alan5.config(foreground="red")
            alan8.config(foreground="red")
            Oyun.PCKazandı()

        #İHTİMAL ALTI
        elif(a3 == "O" and a6 == "O" and a9 == "O"):
            alan3.config(foreground = "red")
            alan6.config(foreground="red")
            alan9.config(foreground="red")
            Oyun.PCKazandı()

        #İHTİMAL YEDİ
        elif(a1 == "O" and a5 == "O" and a9 == "O"):
            alan2.config(foreground = "red")
            alan5.config(foreground="red")
            alan9.config(foreground="red")
            Oyun.PCKazandı()

        #İHTİMAL SEKİZ
        elif(a3 == "O" and a5 == "O" and a7 == "O"):
            alan3.config(foreground = "red")
            alan5.config(foreground="red")
            alan7.config(foreground="red")
            Oyun.PCKazandı()

        if(PC_Yendi == True):
            pass

        else:
            Oyun.DördüncüHamle()


    def PCKazandı():
        global PC_Yendi
        sıra_yazısı.config(foreground = "red")
        sıra_yazısı['text'] = "PC WON THE GAME!"

        PC_Yendi = True


    def FillArea4(kutu):
        if(kutu == "1"):
            alan1['text'] = "X"
        elif(kutu == "2"):
            alan2['text'] = "X"
        elif(kutu == "3"):
            alan3['text'] = "X"
        elif(kutu == "4"):
            alan4['text'] = "X"
        elif(kutu == "5"):
            alan5['text'] = "X"
        elif(kutu == "6"):
            alan6['text'] = "X"
        elif(kutu == "7"):
            alan7['text'] = "X"
        elif(kutu == "8"):
            alan8['text'] = "X"
        elif(kutu == "9"):
            alan9['text'] = "X"

        Oyun.PCSırası4()


    def FillArea5(kutu):
        if(kutu == "1"):
            alan1['text'] = "X"
        elif(kutu == "2"):
            alan2['text'] = "X"
        elif(kutu == "3"):
            alan3['text'] = "X"
        elif(kutu == "4"):
            alan4['text'] = "X"
        elif(kutu == "5"):
            alan5['text'] = "X"
        elif(kutu == "6"):
            alan6['text'] = "X"
        elif(kutu == "7"):
            alan7['text'] = "X"
        elif(kutu == "8"):
            alan8['text'] = "X"
        elif(kutu == "9"):
            alan9['text'] = "X"

        Oyun.PCSırası5()


    def PCSırası4():
        kutu1.unbind("<Button-1>")
        kutu2.unbind("<Button-1>")
        kutu3.unbind("<Button-1>")
        kutu4.unbind("<Button-1>")
        kutu5.unbind("<Button-1>")
        kutu6.unbind("<Button-1>")
        kutu7.unbind("<Button-1>")
        kutu8.unbind("<Button-1>")
        kutu9.unbind("<Button-1>")

        sıra_yazısı['text'] = "SIRA: " + "PC'DE"
        Oyun.PCDüşünme4()


    def PCSırası5():
        kutu1.unbind("<Button-1>")
        kutu2.unbind("<Button-1>")
        kutu3.unbind("<Button-1>")
        kutu4.unbind("<Button-1>")
        kutu5.unbind("<Button-1>")
        kutu6.unbind("<Button-1>")
        kutu7.unbind("<Button-1>")
        kutu8.unbind("<Button-1>")
        kutu9.unbind("<Button-1>")

        sıra_yazısı['text'] = "SIRA: " + "PC'DE"
        Oyun.PCDüşünme5()


    def ClickDetect3():
        kutu1.bind("<Button-1>", Oyun.callback4)
        kutu2.bind("<Button-1>", Oyun.callback4)
        kutu3.bind("<Button-1>", Oyun.callback4)
        kutu4.bind("<Button-1>", Oyun.callback4)
        kutu5.bind("<Button-1>", Oyun.callback4)
        kutu6.bind("<Button-1>", Oyun.callback4)
        kutu7.bind("<Button-1>", Oyun.callback4)
        kutu8.bind("<Button-1>", Oyun.callback4)
        kutu9.bind("<Button-1>", Oyun.callback4)


    def DördüncüHamle():
        Oyun.ClickDetect3()


    def PCDüşünme4():
        a1, a2, a3 = alan1.cget("text"), alan2.cget("text"), alan3.cget("text")
        a4, a5, a6 = alan4.cget("text"), alan5.cget("text"), alan6.cget("text")
        a7, a8, a9 = alan7.cget("text"), alan8.cget("text"), alan9.cget("text")

        global X_Yendi
        X_Yendi = None

        #İHTİMAL BİR
        if(a1 == "X" and a2 == "X" and a3 == "X"):
            alan1.config(foreground = "red")
            alan2.config(foreground="red")
            alan3.config(foreground="red")
            Oyun.XKazandı()
        #İHTİMAL İKİ
        elif(a4 == "X" and a5 == "X" and a6 == "X"):
            alan4.config(foreground = "red")
            alan5.config(foreground="red")
            alan6.config(foreground="red")
            Oyun.XKazandı()
        #İHTİMAL ÜÇ
        elif(a7 == "X" and a8 == "X" and a9 == "X"):
            alan7.config(foreground = "red")
            alan8.config(foreground="red")
            alan9.config(foreground="red")
            Oyun.XKazandı()
        #İHTİMAL DÖRT
        elif(a1 == "X" and a4 == "X" and a7 == "X"):
            alan1.config(foreground = "red")
            alan4.config(foreground="red")
            alan7.config(foreground="red")
            Oyun.XKazandı()
        #İHTİMAL BEŞ
        elif(a2 == "X" and a5 == "X" and a8 == "X"):
            alan2.config(foreground = "red")
            alan5.config(foreground="red")
            alan8.config(foreground="red")
            Oyun.XKazandı()
        #İHTİMAL ALTI
        elif(a3 == "X" and a6 == "X" and a9 == "X"):
            alan3.config(foreground = "red")
            alan6.config(foreground="red")
            alan9.config(foreground="red")
            Oyun.XKazandı()
        #İHTİMAL YEDİ
        elif(a1 == "X" and a5 == "X" and a9 == "X"):
            alan1.config(foreground = "red")
            alan5.config(foreground="red")
            alan9.config(foreground="red")
            Oyun.XKazandı()
        #İHTİMAL SEKİZ
        elif(a3 == "X" and a5 == "X" and a7 == "X"):
            alan3.config(foreground = "red")
            alan5.config(foreground="red")
            alan7.config(foreground="red")
            Oyun.XKazandı()

        #YENDİ Mİ BAK
        if(X_Yendi == True):
            pass

        else:
            #İHTİMAL BİR
            if (a1 == "O" and a2 == "O" and a3 == "O"):
                alan1.config(foreground="red")
                alan2.config(foreground="red")
                alan3.config(foreground="red")
                Oyun.PCKazandı()
            # İHTİMAL İKİ
            elif (a4 == "O" and a5 == "O" and a6 == "O"):
                alan4.config(foreground="red")
                alan5.config(foreground="red")
                alan6.config(foreground="red")
                Oyun.PCKazandı()
            # İHTİMAL ÜÇ
            elif (a7 == "O" and a8 == "O" and a9 == "O"):
                alan7.config(foreground="red")
                alan8.config(foreground="red")
                alan9.config(foreground="red")
                Oyun.PCKazandı()
            # İHTİMAL DÖRT
            elif (a1 == "O" and a4 == "O" and a7 == "O"):
                alan1.config(foreground="red")
                alan4.config(foreground="red")
                alan7.config(foreground="red")
                Oyun.PCKazandı()
            # İHTİMAL BEŞ
            elif (a2 == "O" and a5 == "O" and a8 == "O"):
                alan2.config(foreground="red")
                alan5.config(foreground="red")
                alan8.config(foreground="red")
                Oyun.PCKazandı()
            # İHTİMAL ALTI
            elif (a3 == "O" and a6 == "O" and a9 == "O"):
                alan3.config(foreground="red")
                alan6.config(foreground="red")
                alan9.config(foreground="red")
                Oyun.PCKazandı()
            # İHTİMAL YEDİ
            elif (a1 == "O" and a5 == "O" and a9 == "O"):
                alan2.config(foreground="red")
                alan5.config(foreground="red")
                alan9.config(foreground="red")
                Oyun.PCKazandı()
            # İHTİMAL SEKİZ
            elif (a3 == "O" and a5 == "O" and a7 == "O"):
                alan3.config(foreground="red")
                alan5.config(foreground="red")
                alan7.config(foreground="red")
                Oyun.PCKazandı()

            if (PC_Yendi == True):
                pass

            else:
                #SALDIRI
                #SALDIRI
                if (a1 == "O" and a2 == "O" and a3 == ""):alan3['text'] = "O"
                elif(a2 == "O" and a3 == "O" and a1 == ""):alan1['text'] = "O"
                elif(a4 == "O" and a5 == "O" and a6 == ""):alan6['text'] = "O"
                elif(a5 == "O" and a6 == "O" and a4 == ""):alan4['text'] = "O"
                elif (a7 == "O" and a8 == "O" and a9 == ""):alan9['text'] = "O"
                elif (a8 == "O" and a9 == "O" and a7 == ""):alan7['text'] = "O"
                elif (a1 == "O" and a4 == "O" and a7 == ""):alan7['text'] = "O"
                elif (a4 == "O" and a7 == "O" and a1 == ""):alan1['text'] = "O"
                elif (a2 == "O" and a5 == "O" and a8 == ""):alan8['text'] = "O"
                elif (a8 == "O" and a5 == "O" and a2 == ""):alan2['text'] = "O"
                elif (a3 == "O" and a6 == "O" and a9 == ""):alan9['text'] = "O"
                elif (a3 == "O" and a5 == "O" and a7 == ""):alan7['text'] = "O"
                elif (a5 == "O" and a7 == "O" and a3 == ""):alan3['text'] = "O"
                elif (a1 == "O" and a5 == "O" and a9 == ""):alan9['text'] = "O"
                elif (a9 == "O" and a5 == "O" and a1 == ""):alan1['text'] = "O"
                elif (a6 == "O" and a9 == "O" and a3 == ""):alan3['text'] = "O"
                elif (a1 == "O" and a3 == "O" and a2 == ""):alan2['text'] = "O"
                elif (a4 == "O" and a6 == "O" and a5 == ""):alan5['text'] = "O"
                elif (a7 == "O" and a9 == "O" and a8 == ""):alan8['text'] = "O"
                elif (a1 == "O" and a7 == "O" and a4 == ""):alan4['text'] = "O"
                elif (a2 == "O" and a8 == "O" and a5 == ""):alan5['text'] = "O"
                elif (a3 == "O" and a9 == "O" and a6 == ""):alan6['text'] = "O"
                elif (a3 == "O" and a7 == "O" and a5 == ""):alan5['text'] = "O"
                elif (a1 == "O" and a9 == "O" and a5 == ""):alan5['text'] = "O"

                #PC YENDİ Mİ BAK
                if (a1 == "O" and a2 == "O" and a3 == "O"):
                    alan1.config(foreground="red")
                    alan2.config(foreground="red")
                    alan3.config(foreground="red")
                    Oyun.PCKazandı()
                # İHTİMAL İKİ
                elif (a4 == "O" and a5 == "O" and a6 == "O"):
                    alan4.config(foreground="red")
                    alan5.config(foreground="red")
                    alan6.config(foreground="red")
                    Oyun.PCKazandı()
                # İHTİMAL ÜÇ
                elif (a7 == "O" and a8 == "O" and a9 == "O"):
                    alan7.config(foreground="red")
                    alan8.config(foreground="red")
                    alan9.config(foreground="red")
                    Oyun.PCKazandı()
                # İHTİMAL DÖRT
                elif (a1 == "O" and a4 == "O" and a7 == "O"):
                    alan1.config(foreground="red")
                    alan4.config(foreground="red")
                    alan7.config(foreground="red")
                    Oyun.PCKazandı()
                # İHTİMAL BEŞ
                elif (a2 == "O" and a5 == "O" and a8 == "O"):
                    alan2.config(foreground="red")
                    alan5.config(foreground="red")
                    alan8.config(foreground="red")
                    Oyun.PCKazandı()
                # İHTİMAL ALTI
                elif (a3 == "O" and a6 == "O" and a9 == "O"):
                    alan3.config(foreground="red")
                    alan6.config(foreground="red")
                    alan9.config(foreground="red")
                    Oyun.PCKazandı()
                # İHTİMAL YEDİ
                elif (a1 == "O" and a5 == "O" and a9 == "O"):
                    alan2.config(foreground="red")
                    alan5.config(foreground="red")
                    alan9.config(foreground="red")
                    Oyun.PCKazandı()
                # İHTİMAL SEKİZ
                elif (a3 == "O" and a5 == "O" and a7 == "O"):
                    alan3.config(foreground="red")
                    alan5.config(foreground="red")
                    alan7.config(foreground="red")
                    Oyun.PCKazandı()

                if (PC_Yendi == True):
                    pass

                else:
                    #SAVUNMA
                    #İHTİMAL BİR
                    if(a1 == "X" and a2 == "X" and a3 == ""):alan3['text'] = "O"
                    #İHTİMAL İKİ
                    elif(a2 == "X" and a3 == "X" and a1 == ""):alan1['text'] = "O"
                    #İHTİMAL ÜÇ
                    elif(a4 == "X" and a5 == "X" and a6 == ""):alan6['text'] = "O"
                    #İHTİMAL DÖRT
                    elif(a5 == "X" and a6 == "X" and a4 == ""):alan4['text'] = "O"
                    #İHTİMAL BEŞ
                    elif(a7 == "X" and a8 == "X" and a9 == ""):alan9['text'] = "O"
                    #İHTİMAL ALTI
                    elif(a8 == "X" and a9 == "X" and a7 == ""):alan7['text'] = "O"
                    #İHTİMAL YEDİ
                    elif(a1 == "X" and a4 == "X" and a7 == ""):alan7['text'] = "O"
                    #İHTİMAL SEKİZ
                    elif(a7 == "X" and a8 == "X" and a1 == ""):alan1['text'] = "O"
                    #İHTİMAL DOKUZ
                    elif(a2 == "X" and a5 == "X" and a8 == ""):alan8['text'] = "O"
                    #İHTİMAL ON
                    elif(a5 == "X" and a8 == "X" and a2 == ""):alan2['text'] = "O"
                    #İHTİMAL ONBİR
                    elif(a3 == "X" and a6 == "X" and a9 == ""):alan9['text'] = "O"
                    #İHTİMAL ONİKİ
                    elif(a6 == "X" and a9 == "X" and a3 == ""):alan3['text'] = "O"
                    #İHTİMAL ONÜÇ
                    elif(a1 == "X" and a5 == "X" and a9 == ""):alan9['text'] = "O"
                    #İHTİMAL ONDÖRT
                    elif(a5 == "X" and a9 == "X" and a1 == ""):alan1['text'] = "O"
                    #İHTİMAL ONBEŞ
                    elif(a3 == "X" and a5 == "X" and a7 == ""):alan7['text'] = "O"
                    #İHTİMAL ONALTI
                    elif(a7 == "X" and a5 == "X" and a3 == ""):alan3['text'] = "O"
                    #İHTİMAL ONYEDİ
                    elif(a1 == "X" and a3 == "X" and a2 == ""):alan2['text'] = "O"
                    #İHTİMAL ONSEKİZ
                    elif(a4 == "X" and a6 == "X" and a5 == ""):alan5['text'] = "O"
                    #İHTİMAL ONDOKUZ
                    elif(a7 == "X" and a9 == "X" and a8 == ""):alan8['text'] = "O"
                    #İHTİMAL YİRMİ
                    elif(a1 == "X" and a7 == "X" and a4 == ""):alan4['text'] = "O"
                    #İHTİMAL YİRMİBİR
                    elif(a2 == "X" and a8 == "X" and a5 == ""):alan5['text'] = "O"
                    #İHTİMAL YİRMİÜÇ
                    elif(a3 == "X" and a9 == "X" and a6 == ""):alan6['text'] = "O"
                    #İHTİMAL YİRMİDÖRT
                    elif(a1 == "X" and a9 == "X" and a5 == ""):alan5['text'] = "O"
                    #İHTİMAL YİRİMBEŞ
                    elif(a3 == "X" and a7 == "X" and a5 == ""):alan5['text'] = "O"

                    else:
                        # RANDOM
                        a1, a2, a3 = alan1.cget("text"), alan2.cget("text"), alan3.cget("text")
                        a4, a5, a6 = alan4.cget("text"), alan5.cget("text"), alan6.cget("text")
                        a7, a8, a9 = alan7.cget("text"), alan8.cget("text"), alan9.cget("text")
                        alanlar = [a1, a2, a3, a4, a5, a6, a7, a8, a9]
                        boş_kutular = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9"]
                        # X KUTU KONUMU BULMA
                        if (a1 == "X"):boş_kutular.remove("a1")
                        if (a2 == "X"):boş_kutular.remove("a2")
                        if (a3 == "X"):boş_kutular.remove("a3")
                        if (a4 == "X"):boş_kutular.remove("a4")
                        if (a5 == "X"):boş_kutular.remove("a5")
                        if (a6 == "X"):boş_kutular.remove("a6")
                        if (a7 == "X"):boş_kutular.remove("a7")
                        if (a8 == "X"):boş_kutular.remove("a8")
                        if (a9 == "X"):boş_kutular.remove("a9")
                        # O KUTU KONUMU BULMA
                        if (a1 == "O"):boş_kutular.remove("a1")
                        if (a2 == "O"):boş_kutular.remove("a2")
                        if (a3 == "O"):boş_kutular.remove("a3")
                        if (a4 == "O"):boş_kutular.remove("a4")
                        if (a5 == "O"):boş_kutular.remove("a5")
                        if (a6 == "O"):boş_kutular.remove("a6")
                        if (a7 == "O"):boş_kutular.remove("a7")
                        if (a8 == "O"):boş_kutular.remove("a8")
                        if (a9 == "O"):boş_kutular.remove("a9")

                        oynanılacak_alan = random.choice(boş_kutular)

                        if (oynanılacak_alan == "a1"):alan1['text'] = "O"
                        elif (oynanılacak_alan == "a2"):alan2['text'] = "O"
                        elif (oynanılacak_alan == "a3"):alan3['text'] = "O"
                        elif (oynanılacak_alan == "a4"):alan4['text'] = "O"
                        elif (oynanılacak_alan == "a5"):alan5['text'] = "O"
                        elif (oynanılacak_alan == "a6"):alan6['text'] = "O"
                        elif (oynanılacak_alan == "a7"):alan7['text'] = "O"
                        elif (oynanılacak_alan == "a8"):alan8['text'] = "O"
                        elif (oynanılacak_alan == "a9"):alan9['text'] = "O"

        if(PC_Yendi == True):
            pass
        elif(X_Yendi == True):
            pass
        else:
            Oyun.BeşinciHamle()


    def ClickDetect4():
        kutu1.bind("<Button-1>", Oyun.callback5)
        kutu2.bind("<Button-1>", Oyun.callback5)
        kutu3.bind("<Button-1>", Oyun.callback5)
        kutu4.bind("<Button-1>", Oyun.callback5)
        kutu5.bind("<Button-1>", Oyun.callback5)
        kutu6.bind("<Button-1>", Oyun.callback5)
        kutu7.bind("<Button-1>", Oyun.callback5)
        kutu8.bind("<Button-1>", Oyun.callback5)
        kutu9.bind("<Button-1>", Oyun.callback5)


    def BeşinciHamle():
        Oyun.ClickDetect4()


    def PCDüşünme5():
        global a1, a2, a3, a4, a5, a6, a7, a8, a9, alanlar, x_kutu_alanlar, o_kutu_alanlar
        a1, a2, a3 = alan1.cget("text"), alan2.cget("text"), alan3.cget("text")
        a4, a5, a6 = alan4.cget("text"), alan5.cget("text"), alan6.cget("text")
        a7, a8, a9 = alan7.cget("text"), alan8.cget("text"), alan9.cget("text")
        alanlar = [a1, a2, a3, a4, a5, a6, a7, a8, a9]
        x_kutu_alanlar = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9"]
        o_kutu_alanlar = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9"]

        X_Yendi = None

        #İHTİMAL BİR
        if (a1 == "X" and a2 == "X" and a3 == "X"):
            alan1.config(foreground="red")
            alan2.config(foreground="red")
            alan3.config(foreground="red")
            Oyun.XKazandı()
        # İHTİMAL İKİ
        elif (a4 == "X" and a5 == "X" and a6 == "X"):
            alan4.config(foreground="red")
            alan5.config(foreground="red")
            alan6.config(foreground="red")
            Oyun.XKazandı()
        # İHTİMAL ÜÇ
        elif (a7 == "X" and a8 == "X" and a9 == "X"):
            alan7.config(foreground="red")
            alan8.config(foreground="red")
            alan9.config(foreground="red")
            Oyun.XKazandı()
        # İHTİMAL DÖRT
        elif (a1 == "X" and a4 == "X" and a7 == "X"):
            alan1.config(foreground="red")
            alan4.config(foreground="red")
            alan7.config(foreground="red")
            Oyun.XKazandı()
        # İHTİMAL BEŞ
        elif (a2 == "X" and a5 == "X" and a8 == "X"):
            alan2.config(foreground="red")
            alan5.config(foreground="red")
            alan8.config(foreground="red")
            Oyun.XKazandı()
        # İHTİMAL ALTI
        elif (a3 == "X" and a6 == "X" and a9 == "X"):
            alan3.config(foreground="red")
            alan6.config(foreground="red")
            alan9.config(foreground="red")
            Oyun.XKazandı()
        # İHTİMAL YEDİ
        elif (a1 == "X" and a5 == "X" and a9 == "X"):
            alan2.config(foreground="red")
            alan5.config(foreground="red")
            alan9.config(foreground="red")
            Oyun.XKazandı()
        # İHTİMAL SEKİZ
        elif (a3 == "X" and a5 == "X" and a7 == "X"):
            alan3.config(foreground="red")
            alan5.config(foreground="red")
            alan7.config(foreground="red")
            Oyun.XKazandı()

        if (X_Yendi == True):
            pass

        else:
            sıra_yazısı.config(foreground="red")
            sıra_yazısı['text'] = "BERABERE!"


    def XKazandı():
        global X_Yendi
        sıra_yazısı.config(foreground="red")
        sıra_yazısı['text'] = "YOU WON THE GAME!"

        X_Yendi = True




if(__name__ == '__main__'):
    Window.StartUp()