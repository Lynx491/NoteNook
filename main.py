"""
metin düzenleyici

version: 0.3.2
"""
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
from base64 import b64encode,b64decode
import screeninfo
import time
import os
from threading import Thread
# char = ["""
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Document</title>
# </head>
# <body>
    
# </body>
# </html>
# ""","<!DOCTYPE html>"]
full_screen = False
class Language():
    def __init__(self,evet,hayır,dosya_henüz_kaydedilmedi,
                eminmisiniz,tema,dosya,dil,beyaz,siyah,kontrast,yüksek,
                mavi,pembe,mor,yeşil,yenidosya,kaydet,farklıkaydet,dosyaaç
                ,onay,satır_büyüt,satır_küçült,metni_büyüt,metni_küçült,satırı_kalınlaştır,
                düzenle,kaydediliyor):
        self.dosya = dosya
        self.evet = evet
        self.hayır = hayır
        self.dosya_henüz_kaydedilmedi = dosya_henüz_kaydedilmedi
        self.eminmisiniz = eminmisiniz
        self.tema = tema
        self.dil = dil
        self.beyaz = beyaz
        self.siyah = siyah
        self.kontrast = kontrast
        self.yüksek = yüksek
        self.mavi = mavi
        self.pembe = pembe
        self.mor = mor
        self.yeşil = yeşil
        self.ingilizce = "English"
        self.türkçe = "Türkçe"
        self.azerbaycanca = "Azərbaycan"
        self.uygurca = "ئۇيغۇر"
        self.ukraynaca = "українська"
        self.rusça = "Русский"
        self.arapça = "عربي"
        self.bulgarca = "България"
        self.romanca = "România"
        self.almanca = "Deutschland"
        self.ispanyolca = "España"
        self.yenidosya = yenidosya
        self.kaydet = kaydet
        self.farklıkaydet = farklıkaydet
        self.dosyaaç = dosyaaç
        self.onay = onay
        self.satır_kalın = satırı_kalınlaştır
        self.satır_büyüt = satır_büyüt
        self.satır_küçült = satır_küçült
        self.metin_büyüt = metni_büyüt
        self.metin_küçült = metni_küçült
        self.düzenle = düzenle
        self.kaydediliyor = kaydediliyor
#diller
TÜRKÇE = Language("Evet","Hayır","Dosya Henüz Kaydedilmedi","Eminmisiniz","Tema","Dosya"
                  ,"Dil","beyaz","siyah","kontrast","yüksek","mavi","pembe","mor","yeşil",
                  "Yeni dosya","Kaydet","Farklı kaydet","Dosya aç","Onay","Satırı büyüt","Satırı küçült"
                  ,"Metni büyüt","Metni küçült","Satırı kalınlaştır / incelt","Düzenle","Kaydediliyor ")

İNGİLİZCE = Language("Yes","No","The File Has not Been Saved Yet","Are You Sure","Theme","File"
                  ,"Language","white","black","contrast","high","blue","pink","purple","green",
                  "New file","Save","Save as","Open file","Approve","Enlarge row","Reduce row"
                  ,"Enlarge text","Reduce text","Thicken / thin row","Edit","Recording")

ARAPÇA = Language("نعم","لا","لم يتم حفظ الملف بعد","هل أنت متأكد","الموضوع","ملف"
                  ,"اللغة","أبيض","أسود","التباين","عالية","الأزرق","الوردي","الأرجواني","الأخضر",
                  "ملف جديد","حفظ","حفظ بشكل مختلف","افتح ملف","التأكيد", "تكبير الخط", "تصغير الخط"
                  , "تكبير النص", "تقليص النص", "تكثيف / ترقيق الخط","تحرير","تسجيل")

ALMANCA = Language("Ja","Nein","Datei Noch Nicht Gespeichert","Sind Sie sicher?","Design","Datei"
                  ,"Sprache","weiß","schwarz","kontrast","hoch","blau","Rosa","Purpur","grün",
                  "Neue Datei","Speichern","Speichern unter","Datei öffnen","Bestätigen", "Zeile vergrößern", "Zeile verkleinern"
                  , "Text vergrößern","Text verkleinern", "Zeile dicker / dünner machen","Bearbeiten","Speichern")

İSPANYOLCA = Language("Sí","No","El Archivo Aún No Se Ha Guardado","Estás Seguro","Tema","Archivo"
                  ,"Idioma","blanco","negro","contraste","alto","azul","rosa","púrpura","verde",
                  "Nuevo archivo","Guardar","Ahorre de manera diferente","Abrir un archivo","Confirmación","Ampliar la línea", "Reducir la línea"
                  , "Ampliar texto", "Reducir texto", "Espesar /adelgazar línea","Editar","Grabación")

RUSÇA = Language("Да","Нет","Файл еще не сохранен","Вы уверены","Тема","Файл"
                  ,"Язык","белый","черный","контраст","высокий","синий","розовый","фиолетовый","зеленый",
                  "Новый файл","Сохранить","Сохранить как","Открыть файл","Подтверждение","Увеличить строку","Уменьшить строку"
                  ,"Увеличить текст","Уменьшить текст","Выделить строку жирным шрифтом / уменьшить","Редактировать","Сохранение")

UKRAYNA = Language("Так","Ні","Файл ще не збережено","Ви впевнені","Тема","Файл"
                  ,"Мова","білий","чорний","контраст","високий","синій","трояндовий","фіолетовий","зелений",
                  "Новий файл","Зберігши","Зберегти як","Відкрити файл","Підтвердження", "збільшити рядок", "зменшити рядок"
                  , "Збільшити текст","зменшити текст", "виділити рядок жирним шрифтом / зменшити","Редагувати","Збереження")

AZERBAYCANCA = Language("Bəli","Yox","Fayl hələ saxlanılmayıb","Əminsən","Mövzu","Fayl"
                  ,"Dil","ağ","qara","kontrast","yüksək","mavi","çəhrayı","bənövşəyi","yaşıl",
                  "Yeni fayl","Saxla","Kimi saxla","Faylı açın","Təsdiq", "sətri böyüt", "sətri kiçilt"
                  , "Mətni böyüt","mətni kiçilt","xətti qalın / kiçilt","Redaktə edin","Qoruma")

BULGARCA = Language("А","Няма","Файлът все още не е запазен","Сигурен ли сте","Тема","Файл"
                  ,"Език","бял","черен","контраст","висок","син","розов","лилав","зелен",
                  "Нов файл","Запазя","Запазване като","Отворя","Потвърждение", "увеличаване на реда", "намаляване на реда"
                  , "Увеличаване на текста","намаляване на текста","удебеляване на реда / намаляване","Редактирам","Запазване")

ROMANCA = Language("Da","Nu","Fișierul nu a fost încă salvat","Ești Sigur","Tema","Fișier"
                  ,"Limba","alb","negru","contrast","mare","albastru","roz","violet","verde",
                  "Fișier nou","Salvați","Salvați diferit","Deschide un fișier","Confirmare", "măriți linia", "reduceți linia"
                  , "Măriți textul", "micșorați textul","îngroșați /linia subțire","Editează","Înregistrare")

UYGURCA = Language("ھەئە","ياق","ھۆججەت تېخى ساقلانمىدى","جەزملەشتۈرەمسىز","باشتېما","ھۆججەت"
                  ,"تىل","ئاق","قاراڭغۇلۇق","سېلىشتۇرما","ئېگىز","كۆك","ھالرەڭ","بىنەپشە","يېشىل",
                  "يېڭى ھۆججەت","ساقلاش","ساقلاڭ","ھۆججەتنى ئېچىڭ","تەكشۈرۈش", "قۇرنى چوڭايتىش", "قۇرنى كىچىكلىتىش", "تېكىستنى چوڭراق قىلىڭ", "تېكىستنى كىچىكلىتىڭ", "قۇرنى قېلىن / قېلىن قىلىڭ"
                  ,"تەھرىر","خاتىرىلەش"
)





class Tema():
    def __init__(self,metinRengi,pencereRengi,metinDüzenleyiciRengi,menuRengi,menuhover):
        self.pencereRengi = pencereRengi
        self.metinDüzenleyiciRengi = metinDüzenleyiciRengi
        self.menuRengi = menuRengi
        self.metinRengi = metinRengi
        self.menuHover = menuhover
    def uygula(self):
        STYLE = f"""
    QWidget {{
        background-color:{self.pencereRengi};
        color:{self.metinRengi};
    }}

    QMenuBar {{
        background-color:{self.menuRengi};
        color:{self.metinRengi};
    }}
    QMenuBar::item:selected {{
        background-color:{self.menuHover};
    }}

    QMenu {{
        background-color:{self.menuRengi};
        color:{self.metinRengi};
    }}
    QMenu::item:selected {{
        background-color:{self.menuHover};
    }}

    QAction {{
        background-color:{self.menuRengi};
        color:{self.metinRengi};
    }}
    QAction::item:selected {{
        background-color:{self.menuHover};
    }}

    QTextEdit {{
        background-color:{self.metinDüzenleyiciRengi};
        color:{self.metinRengi};
    }}
    """
        return STYLE

BEYAZ_TEMA = Tema(
    metinRengi="#1A1A1A",
    pencereRengi="#F9F9F9",
    metinDüzenleyiciRengi="#FFFFFF",
    menuRengi="#F9F9F9",
    menuhover="#CCCCCC"
)

SIYAH_TEMA = Tema(
    metinRengi="#EAEAEA",
    pencereRengi="#1E1E1E",
    metinDüzenleyiciRengi="#2C2C2C",
    menuRengi="#1E1E1E",
    menuhover="#444444"
)
CYBER_TEMA = Tema(
    metinRengi="#00FFD5",
    pencereRengi="#0F0F1F",
    metinDüzenleyiciRengi="#12122A",
    menuRengi="#0F0F1F",
    menuhover="#FF00FF"
)
MORUMSU_TEMA = Tema(
    metinRengi="#E0D0FF",
    pencereRengi="#2A1A3A",
    metinDüzenleyiciRengi="#331F4B",
    menuRengi="#2A1A3A",
    menuhover="#5E3A75"
)
PEMBEMSI_TEMA = Tema(
    metinRengi="#FFE0F0",
    pencereRengi="#4B1A3A",
    metinDüzenleyiciRengi="#5C1F50",
    menuRengi="#4B1A3A",
    menuhover="#FF69B4"
)
YESIL_TEMA = Tema(
    metinRengi="#D0FFD0",
    pencereRengi="#1A3A1A",
    metinDüzenleyiciRengi="#2E4B2E",
    menuRengi="#1A3A1A",
    menuhover="#00FF00"
)
MAVI_TEMA = Tema(
    metinRengi="#D0E0FF",
    pencereRengi="#1A1A3A",
    metinDüzenleyiciRengi="#2E2E4B",
    menuRengi="#1A1A3A",
    menuhover="#00BFFF"
)
KONTRAST_TEMA = Tema(
    metinRengi="#FFFFFF",
    pencereRengi="#000000",
    metinDüzenleyiciRengi="#000000",
    menuRengi="#000000",
    menuhover="#333333"
)
KONTRAST_BEYAZ = Tema(
    metinRengi="#000000",
    pencereRengi="#FFFFFF",
    metinDüzenleyiciRengi="#FFFFFF",
    menuRengi="#FFFFFF",
    menuhover="#AAAAAA"
)
KONTRAST_SIYAH = Tema(
    metinRengi="#FFFFFF",
    pencereRengi="#000000",
    metinDüzenleyiciRengi="#000000",
    menuRengi="#000000",
    menuhover="#333333"
)
def error(metin,başlık):
    msg = QMessageBox()
    msg.setText(metin)
    msg.setWindowTitle(başlık)
    msg.setIcon(QMessageBox.Icon.Critical)
    msg.exec()
# error("bubir deneme hata mesajıdır","baslik")
def dil_ve_tema_bulucu():
    try:
        with open("./config.txt","r",encoding="utf-8")as f:
            dosya = f.readlines()
            dil = dosya[1].strip()
            tema = dosya[0].strip()
        return dil, tema
    except Exception as e:
        dil = "EN"
        tema = "beyaz"
        return dil, tema

seçili_dil, seçili_tema = dil_ve_tema_bulucu()
def config_writer(satır_metni,index:int):
    yeni_satir = satır_metni
    try:
        # Dosyayı oku ve satırları al
        with open("config.txt", "r", encoding="utf-8") as f:
            satirlar = f.readlines()

        # İlk satırı değiştir
        satirlar[index] = yeni_satir + "\n"

        # Dosyayı tekrar yaz
        with open("config.txt", "w", encoding="utf-8") as f:
            f.writelines(satirlar)
    except:
        with open("config.txt","w",encoding="utf-8")as f:
            f.write("beyaz\nEN")
def tema_değişti():
    global seçili_tema
    if seçili_tema == "beyaz":
        TEMA = BEYAZ_TEMA
    if seçili_tema == "siyah":
        TEMA = SIYAH_TEMA
    if seçili_tema == "kont_beyaz":
        TEMA = KONTRAST_BEYAZ
    if seçili_tema == "kont_siyah":
        TEMA = KONTRAST_SIYAH
    if seçili_tema == "kont":
        TEMA = KONTRAST_TEMA
    if seçili_tema == "cyper":
        TEMA = CYBER_TEMA
    if seçili_tema == "yeşil":
        TEMA = YESIL_TEMA
    if seçili_tema == "mor":
        TEMA = MORUMSU_TEMA
    if seçili_tema == "pembe":
        TEMA = PEMBEMSI_TEMA
    if seçili_tema == "mavi":
        TEMA = MAVI_TEMA

    try:
        config_writer(seçili_tema,0)
    except:pass
    return TEMA.uygula()

def dil_değiştir():
    global seçili_dil
    if seçili_dil == "TR":#turkiye
        DİL = TÜRKÇE
    if seçili_dil == "EN":#ingilizce
        DİL = İNGİLİZCE
    if seçili_dil == "UK":#ukraynaca
        DİL = UKRAYNA
    if seçili_dil == "RU":#rusça
        DİL = RUSÇA
    if seçili_dil == "ES":#ispanyolca
        DİL = İSPANYOLCA
    if seçili_dil == "AZ":#azerbaycanca
        DİL = AZERBAYCANCA
    if seçili_dil == "AR":#suudi arabistanca
        DİL = ARAPÇA
    if seçili_dil == "DE":#almanca
        DİL = ALMANCA
    if seçili_dil == "UG":#uygurca
        DİL = UYGURCA
    if seçili_dil == "BG":#bulgarca
        DİL = BULGARCA
    if seçili_dil == "RO":#romanca
        DİL = ROMANCA

    try:
        config_writer(seçili_dil,1)
    except:pass
    return DİL

def confirm(parent,başlık,metin):
    msg = QMessageBox(parent)
    msg.setWindowTitle(başlık)
    msg.setText(metin)
    msg.setIcon(QMessageBox.Warning)

    # Buton ekleme ve isimlendirme
    evet = msg.addButton(DİL.evet, QMessageBox.YesRole)
    hayir = msg.addButton(DİL.hayır, QMessageBox.NoRole)

    msg.exec()

    if msg.clickedButton() == evet:
        return True
    else:
        return False

TEMA = tema_değişti()
DİL = dil_değiştir()
class MyTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.basili_tuslar = set()
        self.parent_app = parent
        self.font_size = 16
        self.setFont(QFont("Arial", self.font_size))
        self.setAcceptDrops(True)  # Sürükle bırak için
    def keyPressEvent(self, event):
        key = event.key()
        self.basili_tuslar.add(key)

        if Qt.Key.Key_Control in self.basili_tuslar and Qt.Key.Key_Shift in self.basili_tuslar and key == Qt.Key.Key_B:
            self.TumunuKalınYap()
        elif Qt.Key.Key_Control in self.basili_tuslar and Qt.Key.Key_Shift in self.basili_tuslar and key == Qt.Key.Key_I:
            self.TumunuItalikYap()
        elif Qt.Key.Key_Control in self.basili_tuslar and Qt.Key.Key_Shift in self.basili_tuslar and key == Qt.Key.Key_U:
            self.TumunuAltiCizgiliYap()
        elif Qt.Key.Key_Control in self.basili_tuslar and Qt.Key.Key_Shift in self.basili_tuslar and key == Qt.Key.Key_M:
            self.zoomIn(1)
        elif Qt.Key.Key_Control in self.basili_tuslar and Qt.Key.Key_Shift in self.basili_tuslar and key == Qt.Key.Key_L:
            self.zoomOut(1)
        elif Qt.Key.Key_Control in self.basili_tuslar and key == Qt.Key.Key_B:
            self.SatırKalın()
        elif Qt.Key.Key_Control in self.basili_tuslar and key == Qt.Key.Key_I:
            self.SatırItalik()
        elif Qt.Key.Key_Control in self.basili_tuslar and key == Qt.Key.Key_U:
            self.SatırAltiCizgili()
        elif Qt.Key.Key_Control in self.basili_tuslar and key == Qt.Key.Key_M:
            self.SatırBüyüt()
        elif Qt.Key.Key_Control in self.basili_tuslar and key == Qt.Key.Key_L:
            self.SatırKüçült()
        elif Qt.Key.Key_Control in self.basili_tuslar and key == Qt.Key.Key_S:
            self.parent_app.dosya_kaydet()
        elif Qt.Key.Key_Control in self.basili_tuslar and Qt.Key.Key_Shift in self.basili_tuslar and key == Qt.Key.Key_S:
            self.parent_app.dosya_farklı_kaydet()
        elif Qt.Key.Key_Control in self.basili_tuslar and key == Qt.Key.Key_O:
            self.parent_app.dosya_aç()
        elif Qt.Key.Key_Control in self.basili_tuslar and key == Qt.Key.Key_N:
            self.parent_app.yeni_dosya()
        elif event.text() == "(":
            cursor = self.textCursor()
            cursor.insertText(")")
            cursor.movePosition(QTextCursor.MoveOperation.Left, QTextCursor.MoveAnchor, 1)
            self.setTextCursor(cursor)
        elif event.text() == "[":
            cursor = self.textCursor()
            cursor.insertText("]")
            cursor.movePosition(QTextCursor.MoveOperation.Left, QTextCursor.MoveAnchor, 1)
            self.setTextCursor(cursor)
        elif event.text() == "{":
            cursor = self.textCursor()
            cursor.insertText("}")
            cursor.movePosition(QTextCursor.MoveOperation.Left, QTextCursor.MoveAnchor, 1)
            self.setTextCursor(cursor)
        elif event.text() == '"':
            cursor = self.textCursor()
            cursor.insertText('"')
            cursor.movePosition(QTextCursor.MoveOperation.Left, QTextCursor.MoveAnchor, 1)
            self.setTextCursor(cursor)
        elif event.text() == "'":
            cursor = self.textCursor()
            cursor.insertText("'")
            cursor.movePosition(QTextCursor.MoveOperation.Left, QTextCursor.MoveAnchor, 1)
            self.setTextCursor(cursor)



        super().keyPressEvent(event)

    def keyReleaseEvent(self, event):
        try:
            self.basili_tuslar.remove(event.key())
        except KeyError:
            pass
        super().keyReleaseEvent(event)

    # --------------------- Satır Bazlı Fonksiyonlar ---------------------
    def SatırItalik(self):
        cursor = self.textCursor()
        cursor.select(QTextCursor.LineUnderCursor)
        fmt = cursor.charFormat()
        fmt.setFontItalic(not fmt.fontItalic())  # tersine çevir
        cursor.mergeCharFormat(fmt)

    def SatırAltiCizgili(self):
        cursor = self.textCursor()
        cursor.select(QTextCursor.LineUnderCursor)
        fmt = cursor.charFormat()
        fmt.setFontUnderline(not fmt.fontUnderline())
        cursor.mergeCharFormat(fmt)

    def SatırBüyüt(self):
        cursor = self.textCursor()
        cursor.select(QTextCursor.LineUnderCursor)
        fmt = cursor.charFormat()
        size = fmt.fontPointSize() or self.font_size
        fmt.setFontPointSize(size + 4)
        cursor.mergeCharFormat(fmt)

    def SatırKüçült(self):
        cursor = self.textCursor()
        cursor.select(QTextCursor.LineUnderCursor)
        fmt = cursor.charFormat()
        size = fmt.fontPointSize() or self.font_size
        fmt.setFontPointSize(max(1, size - 4))
        cursor.mergeCharFormat(fmt)

    def SatırKalın(self):
        cursor = self.textCursor()
        cursor.select(QTextCursor.LineUnderCursor)
        fmt = cursor.charFormat()
        fmt.setFontWeight(QFont.Normal if fmt.fontWeight() == QFont.Bold else QFont.Bold)
        cursor.mergeCharFormat(fmt)

    # --------------------- Tüm Metin Fonksiyonları ---------------------
    def TumunuKalınYap(self):
        self.selectAll()
        cursor = self.textCursor()
        cursor.select(QTextCursor.Document)
        fmt = QTextCharFormat()

        # Mevcut formatı al
        current_fmt = cursor.charFormat()
        is_bold = current_fmt.fontWeight() == QFont.Bold

        # Tersine çevir
        fmt.setFontWeight(QFont.Normal if is_bold else QFont.Bold)

        cursor.mergeCharFormat(fmt)
        cursor.clearSelection()
        self.setTextCursor(cursor)

    def TumunuItalikYap(self):
        self.selectAll()
        cursor = self.textCursor()
        cursor.select(QTextCursor.Document)
        fmt = QTextCharFormat()

        # Mevcut formatı al
        current_fmt = cursor.charFormat()
        is_italic = current_fmt.fontItalic()

        # Tersine çevir
        fmt.setFontItalic(not is_italic)

        cursor.mergeCharFormat(fmt)
        cursor.clearSelection()
        self.setTextCursor(cursor)

    def TumunuAltiCizgiliYap(self):
        self.selectAll()
        cursor = self.textCursor()
        cursor.select(QTextCursor.Document)
        fmt = QTextCharFormat()

        # Mevcut formatı al
        current_fmt = cursor.charFormat()
        is_underlined = current_fmt.fontUnderline()

        # Tersine çevir
        fmt.setFontUnderline(not is_underlined)

        cursor.mergeCharFormat(fmt)
        cursor.clearSelection()
        self.setTextCursor(cursor)
    # --------------------- Metin Büyüt/Küçült ---------------------
    # --------------------- Sürükle Bırak ---------------------
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            self.parent_app.global_dosya_yolu = file_path
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                self.setPlainText(content)
            except Exception as e:
                print(f"Dosya açılamadı: {e}")
    def wheelEvent(self, event):
          # tekerlek yönü
        
        if event.modifiers() and Qt.Modifier.CTRL:  
            if event.angleDelta().y() > 0:
                self.zoomIn(1)
            else:
                self.zoomOut(1)
        else:
            super().wheelEvent(event)


class Application(QWidget):
    def __init__(self,height,width,title,resize,icon,global_dosya_yolu):
        super().__init__()
        global full_screen
        self.moniotors = screeninfo.get_monitors()[0]
        self.monitors_width, self.monitors_height = self.moniotors.width, self.moniotors.height
        if "max" in width and "max" in height:
            full_screen = True
        else:
            self.w = width#büyütüp küçültmek kaldı
            self.h = height
            full_screen = False
            self.px = (self.monitors_width/2) - (self.w/2)
            self.py = (self.monitors_height/2) - (self.h/2)
            self.setGeometry(self.px,self.py,self.w,self.h)
        self.setWindowTitle(title)
        self.resize = resize
        self.setWindowIcon(QIcon(icon))
        self.basili_tuslar = set()
        self.global_dosya_yolu = global_dosya_yolu
        #ana kod
        #menu bar ve üst menuler
        self.menu = QMenuBar(self)
        if full_screen:
            self.menu.setGeometry(5,5,self.monitors_width-20,self.monitors_height-20)
        else:
            self.menu.setGeometry(5,5,self.w-20,self.h-20)
        self.dosya = QMenu(title=DİL.dosya)
        self.theme = QMenu(title=DİL.tema)
        self.language = QMenu(title=DİL.dil)
        self.edit = QMenu(title=DİL.düzenle)

        #alt menuler
        #dosya
        self.dosyaYeni = QAction(text=DİL.yenidosya,shortcut="Ctrl+N")
        self.dosyaYeni.triggered.connect(lambda:self.yeni_dosya())
        self.dosyaDosyaAç = QAction(text=DİL.dosyaaç,shortcut="Ctrl+O")
        self.dosyaDosyaAç.triggered.connect(lambda:self.dosya_aç())
        self.dosyaKaydet = QAction(text=DİL.kaydet,shortcut="Ctrl+S")
        self.dosyaKaydet.triggered.connect(lambda:self.dosya_kaydet())
        self.dosyaFarklı = QAction(text=DİL.farklıkaydet,shortcut="Ctrl+Shift+S")
        self.dosyaFarklı.triggered.connect(lambda:self.dosya_farklı_kaydet())

        #edit
        self.edit_satırbüyüt = QAction(text=DİL.satır_büyüt,shortcut="Ctrl+M")
        self.edit_satırbüyüt.triggered.connect(lambda:self.textedit.SatırBüyüt())
        self.edit_satırküçült = QAction(text=DİL.satır_küçült,shortcut="Ctrl+L")
        self.edit_satırküçült.triggered.connect(lambda:self.textedit.SatırKüçült())
        self.edit_metinbüyüt = QAction(text=DİL.metin_büyüt,shortcut="Ctrl+Shift+M")
        self.edit_metinbüyüt.triggered.connect(lambda:self.textedit.zoomIn(1))
        self.edit_metinküçült = QAction(text=DİL.metin_küçült,shortcut="Ctrl+Shift+L")
        self.edit_metinküçült.triggered.connect(lambda:self.textedit.zoomOut(1))
        self.edit_satırkalın = QAction(text=DİL.satır_kalın,shortcut="Ctrl+B")
        self.edit_satırkalın.triggered.connect(lambda:self.textedit.SatırKalın())

        #tema
        self.teheme_beyaz = QAction(text=DİL.beyaz+" "+DİL.tema)
        self.teheme_beyaz.triggered.connect(lambda:self.tema_change("beyaz"))
        self.theme_siyah = QAction(text=DİL.siyah+" "+DİL.tema)
        self.theme_siyah.triggered.connect(lambda:self.tema_change("siyah"))
        self.theme_kont_beyaz = QAction(text=DİL.yüksek+" "+DİL.kontrast+" "+DİL.beyaz+" "+DİL.tema)
        self.theme_kont_beyaz.triggered.connect(lambda:self.tema_change("kont_beyaz"))
        self.theme_kont_siyah = QAction(text=DİL.yüksek+" "+DİL.kontrast+" "+DİL.siyah+" "+DİL.tema)
        self.theme_kont_siyah.triggered.connect(lambda:self.tema_change("kont_siyah"))
        self.theme_kont = QAction(text=DİL.kontrast +" "+DİL.tema)
        self.theme_kont.triggered.connect(lambda:self.tema_change("kont"))
        self.theme_yesil = QAction(text=DİL.yeşil+" "+DİL.tema)
        self.theme_yesil.triggered.connect(lambda:self.tema_change("yeşil"))
        self.theme_mor = QAction(text=DİL.mor+" "+DİL.tema)
        self.theme_mor.triggered.connect(lambda:self.tema_change("mor"))
        self.theme_pembe = QAction(text=DİL.pembe+" "+DİL.tema)
        self.theme_pembe.triggered.connect(lambda:self.tema_change("pembe"))
        self.theme_mavi = QAction(text=DİL.mavi+" "+DİL.tema)
        self.theme_mavi.triggered.connect(lambda:self.tema_change("mavi"))
        self.theme_cyper = QAction(text="Cyper "+DİL.tema)
        self.theme_cyper.triggered.connect(lambda:self.tema_change("cyper"))

        self.lang_turkçe = QAction(text=DİL.türkçe)
        self.lang_turkçe.triggered.connect(lambda:self.dil_change("TR"))
        self.lang_ingilizce= QAction(text=DİL.ingilizce)
        self.lang_ingilizce.triggered.connect(lambda:self.dil_change("EN"))
        self.lang_almanca = QAction(text=DİL.almanca)
        self.lang_almanca.triggered.connect(lambda:self.dil_change("DE"))
        self.lang_arapça = QAction(text=DİL.arapça)
        self.lang_arapça.triggered.connect(lambda:self.dil_change("AR"))
        self.lang_rusça = QAction(text=DİL.rusça)
        self.lang_rusça.triggered.connect(lambda:self.dil_change("RU"))
        self.lang_ukrayna = QAction(text=DİL.ukraynaca)
        self.lang_ukrayna.triggered.connect(lambda:self.dil_change("UK"))
        self.lang_romanca = QAction(text=DİL.romanca)
        self.lang_romanca.triggered.connect(lambda:self.dil_change("RO"))
        self.lang_bulgarca = QAction(text=DİL.bulgarca)
        self.lang_bulgarca.triggered.connect(lambda:self.dil_change("BG"))
        self.lang_azerbaycan = QAction(text=DİL.azerbaycanca)
        self.lang_azerbaycan.triggered.connect(lambda:self.dil_change("AZ"))
        self.lang_uygurca = QAction(text=DİL.uygurca)
        self.lang_uygurca.triggered.connect(lambda:self.dil_change("UG"))
        self.lang_ispanyol = QAction(text=DİL.ispanyolca)
        self.lang_ispanyol.triggered.connect(lambda:self.dil_change("ES"))

        #menu eklemeleri
        self.menu.addMenu(self.dosya)
        self.menu.addMenu(self.edit)
        self.menu.addMenu(self.theme)
        self.menu.addMenu(self.language)

        self.dosya.addAction(self.dosyaYeni)
        self.dosya.addAction(self.dosyaDosyaAç)
        self.dosya.addAction(self.dosyaKaydet)
        self.dosya.addAction(self.dosyaFarklı)

        self.edit.addAction(self.edit_satırbüyüt)
        self.edit.addAction(self.edit_satırküçült)
        self.edit.addAction(self.edit_satırkalın)
        self.edit.addAction(self.edit_metinbüyüt)
        self.edit.addAction(self.edit_metinküçült)

        self.theme.addAction(self.teheme_beyaz)
        self.theme.addAction(self.theme_siyah)
        self.theme.addAction(self.theme_kont_beyaz)
        self.theme.addAction(self.theme_kont_siyah)
        self.theme.addAction(self.theme_yesil)
        self.theme.addAction(self.theme_mavi)
        self.theme.addAction(self.theme_mor)
        self.theme.addAction(self.theme_pembe)
        self.theme.addAction(self.theme_kont)
        self.theme.addAction(self.theme_cyper)

        self.language.addAction(self.lang_turkçe)
        self.language.addAction(self.lang_ingilizce)
        self.language.addAction(self.lang_arapça)
        self.language.addAction(self.lang_almanca)
        self.language.addAction(self.lang_ispanyol)
        self.language.addAction(self.lang_azerbaycan)
        self.language.addAction(self.lang_rusça)
        self.language.addAction(self.lang_ukrayna)
        self.language.addAction(self.lang_uygurca)
        self.language.addAction(self.lang_romanca)
        self.language.addAction(self.lang_bulgarca)

        self.lbl_kaydedildi = QLabel(self)
        self.lbl_kaydedildi.setGeometry(220,5,600,20)
        self.lbl_kaydedildi.setText("")

        self.textedit = MyTextEdit(self)
        if full_screen:
            self.textedit.setGeometry(10,30,self.monitors_width-20,self.monitors_height-20)
        else:
            self.textedit.setGeometry(10,30,self.w-20,self.h-120)
        if self.global_dosya_yolu != "":
            with open(self.global_dosya_yolu, "r", encoding="utf-8") as f:
                dosya = f.read()
            df = dosya_yolu.split(".")
            i = len(df)-1
            if df[i] == "txt":
                try:
                    self.textedit.setHtml(b64decode(dosya).decode())
                except:
                    self.textedit.setText(dosya)
            else:
                self.textedit.setText(dosya)
        self.setStyleSheet(TEMA)

    def kaydedildi_efekti(self,dosya_yolu):
        self.lbl_kaydedildi.setText(DİL.kaydediliyor+dosya_yolu)
        time.sleep(3)
        self.lbl_kaydedildi.setText("")

    def dosya_farklı_kaydet(self):
        # Dosya kaydetme penceresi aç
        # dosya_yolu, _filtre = QFileDialog.getSaveFileName(
        #     self,
        #     DİL.farklıkaydet,
        #     "./",
        #     "(*.txt);;(*.py);;(*)"
        # )
        # self.textedit.setFocus()
        dlg = QFileDialog(self, DİL.farklıkaydet, "./")
        dlg.setNameFilters(["(*.txt)", "(*.py)", "(*)"])
        dlg.setAcceptMode(QFileDialog.AcceptSave)
        dlg.setOption(QFileDialog.DontUseNativeDialog, True)
        if dlg.exec():
            dosya_yolu = dlg.selectedFiles()[0]
            _filtre = dlg.selectedNameFilter()  # işte filtre artık gelir
        if dosya_yolu:  # kullanıcı iptal etmediyse
            dosya = b64encode(self.textedit.toHtml().encode()).decode()
            # with open(dosya_yolu+, "w", encoding="utf-8") as f:
            #     f.write(dosya)
            if _filtre == "(*.txt)":
                dosya = b64encode(self.textedit.toHtml().encode()).decode()
                with open(dosya_yolu+".txt", "w", encoding="utf-8") as f:
                    f.write(dosya)
                self.global_dosya_yolu = dosya_yolu+".txt"
            elif _filtre == "(*.py)":
                with open(dosya_yolu+".py", "w", encoding="utf-8") as f:
                    f.write(self.textedit.toPlainText())
                self.global_dosya_yolu = dosya_yolu+".py"
            else:
                # d = dosya_yolu.split(".")
                # sonuc = f".{len(d)-1}"
                with open(dosya_yolu, "w", encoding="utf-8") as f:
                    f.write(self.textedit.toPlainText())
                self.global_dosya_yolu = dosya_yolu
            self.th1 = Thread(target=lambda: self.kaydedildi_efekti(dosya_yolu))
            self.th1.start()

    def dosya_aç(self):
        # Dosya kaydetme penceresi aç
        dosya_yolu, _filtre = QFileDialog.getOpenFileName(
            self,
            DİL.dosyaaç,
            "",                          # başlangıç yolu (boş bırakılırsa masaüstü açılır)
            "(*.txt);;(*.py);;(*)"
        )

        if dosya_yolu:
            self.global_dosya_yolu = dosya_yolu
            with open(dosya_yolu, "r", encoding="utf-8") as f:
                dosya = f.read()
            df = dosya_yolu.split(".")
            i = len(df)-1
            if df[i] == "txt":
                try:
                    self.textedit.setHtml(b64decode(dosya).decode())
                except:
                    self.textedit.setText(dosya)
            else:
                self.textedit.setText(dosya)

    def dosya_kaydet(self):
        if self.global_dosya_yolu != "":
            dosya_yolu = self.global_dosya_yolu
            uzantı = len(dosya_yolu.split("."))-1
            if uzantı == ".txt":
                dosya = b64encode(self.textedit.toHtml().encode()).decode()
                with open(dosya_yolu,"w",encoding="utf-8")as f:
                    f.write(dosya)
            else:
                with open(dosya_yolu,"w",encoding="utf-8")as f:
                    f.write(self.textedit.toPlainText())
            self.global_dosya_yolu = dosya_yolu
            self.th2 = Thread(target=lambda: self.kaydedildi_efekti(dosya_yolu))
            self.th2.start()
    def yeni_dosya(self):
        metin = self.textedit.toPlainText()
        if metin != "":
            if self.global_dosya_yolu == "":
                cevap = confirm(self,DİL.onay,DİL.dosya_henüz_kaydedilmedi+" "+DİL.eminmisiniz+"?")
                if cevap:
                    self.textedit.clear()
                    self.global_dosya_yolu = ""
            else:
                self.textedit.clear()
                self.global_dosya_yolu = ""

        else:
            self.textedit.clear()
            self.global_dosya_yolu = ""

    def tema_change(self,tema:str):
        global seçili_tema
        seçili_tema = tema
        TEMA = tema_değişti()
        self.setStyleSheet(TEMA)
    def dil_change(self,dil_kodu:str):
        """TR,EN"""
        global seçili_dil,DİL
        seçili_dil = dil_kodu
        DİL = dil_değiştir()
        self.theme.setTitle(DİL.tema)
        self.language.setTitle(DİL.dil)
        self.dosya.setTitle(DİL.dosya)

        self.dosyaDosyaAç.setText(DİL.dosyaaç)
        self.dosyaFarklı.setText(DİL.farklıkaydet)
        self.dosyaKaydet.setText(DİL.kaydet)
        self.dosyaYeni.setText(DİL.yenidosya)

        self.teheme_beyaz.setText(DİL.beyaz+" "+DİL.tema)
        self.theme_cyper.setText("Cyper "+DİL.tema)
        self.theme_kont.setText(DİL.kontrast+" "+DİL.tema)
        self.theme_kont_beyaz.setText(DİL.yüksek+" "+DİL.kontrast+" "+DİL.beyaz+" "+DİL.tema)
        self.theme_kont_siyah.setText(DİL.yüksek+" "+DİL.kontrast+" "+DİL.siyah+" "+DİL.tema)
        self.theme_mavi.setText(DİL.mavi+" "+DİL.tema)
        self.theme_mor.setText(DİL.mor+" "+DİL.tema)
        self.theme_pembe.setText(DİL.pembe+" "+DİL.tema)
        self.theme_siyah.setText(DİL.siyah+" "+DİL.tema)
        self.theme_yesil.setText(DİL.yeşil+" "+DİL.tema)
        self.edit.setTitle(DİL.düzenle)
        self.edit_metinbüyüt.setText(DİL.metin_büyüt)
        self.edit_metinküçült.setText(DİL.metin_küçült)
        self.edit_satırkalın.setText(DİL.satır_kalın)
        self.edit_satırbüyüt.setText(DİL.satır_büyüt)
        self.edit_satırküçült.setText(DİL.satır_küçült)

if __name__ == "__main__":
    çatı = QApplication(sys.argv)
    dosya_yolu = ""
    if len(sys.argv) > 1:
        dosya_yolu = sys.argv[1]
    uygulama = Application("max","max","NoteNook++",resize=True,icon="./notenook.png",global_dosya_yolu=dosya_yolu)
    if full_screen:
        uygulama.showMaximized()
    else:
        uygulama.show()
    sys.exit(çatı.exec())
