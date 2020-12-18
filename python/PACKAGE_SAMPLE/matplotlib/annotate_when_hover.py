import matplotlib.pyplot as plt
import numpy as np


x = [1,2,3]
y = [1,2,3]
c = [1,2,3]
cmap = "name"

fig,ax = plt.subplots()
sc = plt.scatter(x,y,c=c, s=100)

#[CLS] 建構全系統唯一的annot物件
annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

def update_annot(ind):
    pos = sc.get_offsets()[ind["ind"][0]]   #[CLS]:ind是scatter artist的特定資料結構
                                            #[CLS]:ind["ind"] 存放的是index, = [ indexes of selected point ] 
                                            #[CLS]:get_offsets() ==> all data in this scatter artist , 真正的offset
    annot.xy = pos  #[CLS] 直接更新annotate的座標
    # text = "{}, {}".format(" ".join(list(map(str,ind["ind"]))), 
    #                        " ".join([names[n] for n in ind["ind"]]))
    text = "{}: ({}, {})".format( " ".join(list(map(str,ind["ind"]))), pos[0], pos[1]     )
    # text = "clouds"
    annot.set_text(text)
    annot.get_bbox_patch().set_facecolor("r")
    annot.get_bbox_patch().set_alpha(0.4)


def hover(event): #[CLS] canvas會回傳event物件 event 物件
    vis = annot.get_visible()
    if event.inaxes == ax: #[CLS] 這個ax的event物件才處理
        cont, ind = sc.contains(event)  #[CLS] 用scatter artist來解釋這個event (因爲也有可能是plot artist物件)
                                        #[CLS] ind 是 scatter artist特定的資料結構
        if cont: #[CLS]: boolean. 假如就是點在這個scatter artist裏面
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()

fig.canvas.mpl_connect("motion_notify_event", hover)

plt.show()
