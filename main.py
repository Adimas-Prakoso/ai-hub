import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *
import io
from PIL import Image
from gtts import lang


## ==> SPLASH SCREEN
from lib.ui_splash import Ui_SplashWindow

## ==> MAIN WINDOW
from lib.ui_main import Ui_MainWindow
from lib.window.ui_tti import Ui_TextToImage
from lib.window.ui_ttv import Ui_TextToVideo
from lib.window.ui_ittxt import Ui_ImageToText
from lib.window.ui_iti import Ui_ITI
from lib.window.ui_question import Ui_Question
from lib.window.ui_tg import Ui_TextGen
from lib.window.ui_ttc import Ui_TextToCode
from lib.window.ui_ttm import Ui_TextToMusic
from lib.window.ui_tts import Ui_TTS
from lib.window.ui_chat import Ui_Conversation
from lib.window.settingsC import Ui_Settings
from lib.window.ui_maker import Ui_Maker

## ==> POPUP MESSAGE
from lib.message.ui_render_mess import Ui_RenderMess
from lib.message.sucess import Ui_SavedMess
from lib.message.prompt import Ui_PromptMess
from lib.message.cek import Ui_CekMess
from lib.message.not_support import Ui_NotSupported 

## ==> GENERATES
from lib.main.random import *
from lib.main.tti import *
from lib.main.ttv import *
from lib.main.tttxt import *
from lib.main.iti import *
from lib.main.qa import *
from lib.main.textgen import *
from lib.main.ttc import *
from lib.main.ttm import *
from lib.main.towav import *
from lib.main.tts import *
from lib.main.getSettings import *
from lib.main.maker import *

photooxy_list = ['Create Blackpink style logo effects',
        'Elegant 3D neon dark metal text effect',  
        'Online 3D white stone text effect',
        'Shadow text effect in the sky',
        'Write name, text on the cup',
        'Romantic Messages for Your Loved One',
        'Create a smoke text effect',
        'Write text on burn paper',
        'Write name on the funny cup',
        'Make Naruto banner',
        'Create a picture of love message',
        'Write your message under the grass',
        'Text effect on romantic double hearts',
        'Put any text in to Coffee cup',
        'Write art quote on wood heart',
        'Write text on the flower heart',
        '"Writing your text on wooden boards',
        'Make 3D summer text effect',
        'Create A Wolf Metal Text Effect',
        'Make nature 3D text effects',
        'Creating text underwater ocean',
        'Write text on golden roses background',
        'Summer nature background with your text',
        'Create typography letters with leaves',
        'Write text, quotes under fall leaves',
        'Create glowing neon text effect',
        'Make rainbow shine text effects',
        'Graffiti text cover generator',
        'Army Camouflage Fabric Text Effect',
        'Create a 3D Glowing Text Effect',
        'Customize vintage text style',
        'Making candy text effect',
        'Create 3D text effect under white cube',
        'Glow rainbow text effect',
        'Write stars text on the night sky',
        'Fur text effect',
        'Realistic Flaming Text effect',
        'Create a Crisp Chrome Text Effect']

## ==> GLOBALS
counter = 0


class TtiWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_TextToImage()
        self.ui.setupUi(self)

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.ui.close_btn.clicked.connect(lambda: self.close())
        self.ui.models.addItem("runwayml/stable-diffusion-v1-5")#
        self.ui.models.addItem("Linaqruf/animagine-xl-2.0")#
        self.ui.models.addItem("SimianLuo/LCM_Dreamshaper_v7")#
        self.ui.models.addItem("stabilityai/stable-diffusion-2-1")#
        self.ui.models.addItem("prompthero/openjourney-v4")#
        self.ui.models.addItem("nerijs/pixel-art-xl")#
        self.ui.models.addItem("segmind/SSD-1B")#
        self.ui.models.addItem("CompVis/stable-diffusion-v1-4")#
        self.ui.models.addItem("openskyml/dalle-3-xl")#
        self.ui.models.addItem("hakurei/waifu-diffusion")#
        self.ui.models.addItem("Linaqruf/anime-detailer-xl-lora")#
        self.ui.models.addItem("Lykon/dreamshaper-7")#
        self.ui.models.addItem("Linaqruf/style-enhancer-xl-lora")#
        self.ui.models.addItem("gsdf/Counterfeit-V2.5")#
        self.ui.models.addItem("Linaqruf/sketch-style-xl-lora")#
        self.ui.models.addItem("digiplay/majicMIX_realistic_v1")#
        self.ui.models.addItem("Linaqruf/animagine-xl")#
        self.ui.models.addItem("stablediffusionapi/anime-model-v2")#
        self.ui.models.addItem("stablediffusionapi/animexl-xuebimix")#
        self.ui.models.addItem("Yntec/realistic-vision-v12")#
        self.ui.models.addItem("stablediffusionapi/realistic-vision-v51")#
        self.ui.models.addItem("stablediffusionapi/beautiful-realistic-asian")#
        self.ui.models.addItem("stablediffusionapi/realistic-vi")#
        self.ui.models.addItem("digiplay/majicMIX_realistic_v6")#
        
        self.mess = RenderMess()
        self.saved = SavedMess()
        self.prompt = PromptMess()
        
        selected_item = self.ui.models.currentText()
        if selected_item in ["runwayml/stable-diffusion-v1-5","Linaqruf/animagine-xl-2.0","SimianLuo/LCM_Dreamshaper_v7", "stabilityai/stable-diffusion-2-1", "prompthero/openjourney-v4", "nerijs/pixel-art-xl", "segmind/SSD-1B", "CompVis/stable-diffusion-v1-4", "openskyml/dalle-3-xl", "hakurei/waifu-diffusion", "Linaqruf/anime-detailer-xl-lora", "Lykon/dreamshaper-7", "Linaqruf/style-enhancer-xl-lora", "gsdf/Counterfeit-V2.5", "Linaqruf/sketch-style-xl-lora", "digiplay/majicMIX_realistic_v1", "Linaqruf/animagine-xl", "stablediffusionapi/anime-model-v2", "stablediffusionapi/animexl-xuebimix", "Yntec/realistic-vision-v12", "stablediffusionapi/realistic-vision-v51", "stablediffusionapi/beautiful-realistic-asian", "stablediffusionapi/realistic-vi", "digiplay/majicMIX_realistic_v6"]:
            self.ui.cpu.hide()
            self.ui.cuda.hide()
            
        def generate():
            if self.ui.apis.isChecked():
                if self.ui.prompt.toPlainText() == "":
                    self.prompt.show()
                else:
                    if selected_item == "runwayml/stable-diffusion-v1-5":#
                        nama_file = nama()
                        img_binary = query(api_url="https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5", prompt=self.ui.prompt.toPlainText())
                        image = Image.open(io.BytesIO(img_binary))
                        image.save(f'./res/saved/ai-hub-{nama_file}.jpg', 'JPEG')
                        self.ui.hasil.setPixmap(QPixmap(f'./res/saved/ai-hub-{nama_file}.jpg'))
                        self.saved.show()
                        pass
                    elif selected_item == "Linaqruf/animagine-xl-2.0":#
                        nama_file = nama()
                        img_binary = query(api_url="https://api-inference.huggingface.co/models/Linaqruf/animagine-xl-2.0", prompt=self.ui.prompt.toPlainText())
                        image = Image.open(io.BytesIO(img_binary))
                        image.save(f'./res/saved/ai-hub-{nama_file}.jpg', 'JPEG')
                        self.ui.hasil.setPixmap(QPixmap(f'./res/saved/ai-hub-{nama_file}.jpg'))
                        self.saved.show()
                        pass
                    elif selected_item == "SimianLuo/LCM_Dreamshaper_v7":#
                        nama_file = nama()
                        img_binary = query(api_url="https://api-inference.huggingface.co/models/SimianLuo/LCM_Dreamshaper_v7", prompt=self.ui.prompt.toPlainText())
                        image = Image.open(io.BytesIO(img_binary))
                        image.save(f'./res/saved/ai-hub-{nama_file}.jpg', 'JPEG')
                        self.ui.hasil.setPixmap(QPixmap(f'./res/saved/ai-hub-{nama_file}.jpg'))
                        self.saved.show()
                        pass
                    elif selected_item == "stabilityai/stable-diffusion-2-1":#
                        nama_file = nama()
                        img_binary = query(api_url="https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1", prompt=self.ui.prompt.toPlainText())
                        image = Image.open(io.BytesIO(img_binary))
                        image.save(f'./res/saved/ai-hub-{nama_file}.jpg', 'JPEG')
                        self.ui.hasil.setPixmap(QPixmap(f'./res/saved/ai-hub-{nama_file}.jpg'))
                        self.saved.show()
                        pass
                    elif selected_item == "prompthero/openjourney-v4":#
                        nama_file = nama()
                        img_binary = query(api_url="https://api-inference.huggingface.co/models/prompthero/openjourney-v4", prompt=self.ui.prompt.toPlainText())
                        image = Image.open(io.BytesIO(img_binary))
                        image.save(f'./res/saved/ai-hub-{nama_file}.jpg', 'JPEG')
                        self.ui.hasil.setPixmap(QPixmap(f'./res/saved/ai-hub-{nama_file}.jpg'))
                        self.saved.show()
                        pass
                    elif selected_item == "nerijs/pixel-art-xl":#
                        nama_file = nama()
                        img_binary = query(api_url="https://api-inference.huggingface.co/models/nerijs/pixel-art-xl", prompt=self.ui.prompt.toPlainText())
                        image = Image.open(io.BytesIO(img_binary))
                        image.save(f'./res/saved/ai-hub-{nama_file}.jpg', 'JPEG')
                        self.ui.hasil.setPixmap(QPixmap(f'./res/saved/ai-hub-{nama_file}.jpg'))
                        self.saved.show()
                        pass
                    elif selected_item == "segmind/SSD-1B":#
                        nama_file = nama()
                        img_binary = query(api_url="https://api-inference.huggingface.co/models/segmind/SSD-1B", prompt=self.ui.prompt.toPlainText())
                        image = Image.open(io.BytesIO(img_binary))
                        image.save(f'./res/saved/ai-hub-{nama_file}.jpg', 'JPEG')
                        self.ui.hasil.setPixmap(QPixmap(f'./res/saved/ai-hub-{nama_file}.jpg'))
                        self.saved.show()
                        pass
                    elif selected_item == "CompVis/stable-diffusion-v1-4":#
                        nama_file = nama()
                        img_binary = query(api_url="https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4", prompt=self.ui.prompt.toPlainText())
                        image = Image.open(io.BytesIO(img_binary))
                        image.save(f'./res/saved/ai-hub-{nama_file}.jpg', 'JPEG')
                        self.ui.hasil.setPixmap(QPixmap(f'./res/saved/ai-hub-{nama_file}.jpg'))
                        self.saved.show()
                        pass
                    elif selected_item == "openskyml/dalle-3-xl":#
                        nama_file = nama()
                        img_binary = query(api_url="https://api-inference.huggingface.co/models/openskyml/dalle-3-xl", prompt=self.ui.prompt.toPlainText())
                        image = Image.open(io.BytesIO(img_binary))
                        image.save(f'./res/saved/ai-hub-{nama_file}.jpg', 'JPEG')
                        self.ui.hasil.setPixmap(QPixmap(f'./res/saved/ai-hub-{nama_file}.jpg'))
                        self.saved.show()
                        pass
                    elif selected_item == "hakurei/waifu-diffusion":#
                        nama_file = nama()
                        img_binary = query(api_url="https://api-inference.huggingface.co/models/hakurei/waifu-diffusion", prompt=self.ui.prompt.toPlainText())
                        image = Image.open(io.BytesIO(img_binary))
                        image.save(f'./res/saved/ai-hub-{nama_file}.jpg', 'JPEG')
                        self.ui.hasil.setPixmap(QPixmap(f'./res/saved/ai-hub-{nama_file}.jpg'))
                        self.saved.show()
                        pass
                    elif selected_item == "Lykon/dreamshaper-7":#
                        nama_file = nama()
                        img_binary = query(api_url="https://api-inference.huggingface.co/models/Lykon/dreamshaper-7", prompt=self.ui.prompt.toPlainText())
                        image = Image.open(io.BytesIO(img_binary))
                        image.save(f'./res/saved/ai-hub-{nama_file}.jpg', 'JPEG')
                        self.ui.hasil.setPixmap(QPixmap(f'./res/saved/ai-hub-{nama_file}.jpg'))
                        self.saved.show()
                        pass
                    elif selected_item == "Linaqruf/style-enhancer-xl-lora":#
                        nama_file = nama()
                        img_binary = query(api_url="https://api-inference.huggingface.co/models/Linaqruf/style-enhancer-xl-lora", prompt=self.ui.prompt.toPlainText())
                        image = Image.open(io.BytesIO(img_binary))
                        image.save(f'./res/saved/ai-hub-{nama_file}.jpg', 'JPEG')
                        self.ui.hasil.setPixmap(QPixmap(f'./res/saved/ai-hub-{nama_file}.jpg'))
                        self.saved.show()
                        pass
                    elif selected_item == "gsdf/Counterfeit-V2.5":#
                        nama_file = nama()
                        img_binary = query(api_url="https://api-inference.huggingface.co/models/gsdf/Counterfeit-V2.5", prompt=self.ui.prompt.toPlainText())
                        image = Image.open(io.BytesIO(img_binary))
                        image.save(f'./res/saved/ai-hub-{nama_file}.jpg', 'JPEG')
                        self.ui.hasil.setPixmap(QPixmap(f'./res/saved/ai-hub-{nama_file}.jpg'))
                        self.saved.show()
                        pass
                    elif selected_item == "Linaqruf/sketch-style-xl-lora":#
                        nama_file = nama()
                        img_binary = query(api_url="https://api-inference.huggingface.co/models/Linaqruf/sketch-style-xl-lora", prompt=self.ui.prompt.toPlainText())
                        image = Image.open(io.BytesIO(img_binary))
                        image.save(f'./res/saved/ai-hub-{nama_file}.jpg', 'JPEG')
                        self.ui.hasil.setPixmap(QPixmap(f'./res/saved/ai-hub-{nama_file}.jpg'))
                        self.saved.show()
                        pass
                    elif selected_item == "digiplay/majicMIX_realistic_v1":#
                        nama_file = nama()
                        img_binary = query(api_url="https://api-inference.huggingface.co/models/digiplay/majicMIX_realistic_v1", prompt=self.ui.prompt.toPlainText())
                        image = Image.open(io.BytesIO(img_binary))
                        image.save(f'./res/saved/ai-hub-{nama_file}.jpg', 'JPEG')
                        self.ui.hasil.setPixmap(QPixmap(f'./res/saved/ai-hub-{nama_file}.jpg'))
                        self.saved.show()
                        pass
                    elif selected_item == "Linaqruf/animagine-xl":#
                        nama_file = nama()
                        img_binary = query(api_url="https://api-inference.huggingface.co/models/Linaqruf/animagine-xl", prompt=self.ui.prompt.toPlainText())
                        image = Image.open(io.BytesIO(img_binary))
                        image.save(f'./res/saved/ai-hub-{nama_file}.jpg', 'JPEG')
                        self.ui.hasil.setPixmap(QPixmap(f'./res/saved/ai-hub-{nama_file}.jpg'))
                        self.saved.show()
                        pass
                    elif selected_item == "stablediffusionapi/anime-model-v2":#
                        nama_file = nama()
                        img_binary = query(api_url="https://api-inference.huggingface.co/models/stablediffusionapi/anime-model-v2", prompt=self.ui.prompt.toPlainText())
                        image = Image.open(io.BytesIO(img_binary))
                        image.save(f'./res/saved/ai-hub-{nama_file}.jpg', 'JPEG')
                        self.ui.hasil.setPixmap(QPixmap(f'./res/saved/ai-hub-{nama_file}.jpg'))
                        self.saved.show()
                        pass
                    elif selected_item == "stablediffusionapi/animexl-xuebimix":#
                        nama_file = nama()
                        img_binary = query(api_url="https://api-inference.huggingface.co/models/stablediffusionapi/animexl-xuebimix", prompt=self.ui.prompt.toPlainText())
                        image = Image.open(io.BytesIO(img_binary))
                        image.save(f'./res/saved/ai-hub-{nama_file}.jpg', 'JPEG')
                        self.ui.hasil.setPixmap(QPixmap(f'./res/saved/ai-hub-{nama_file}.jpg'))
                        self.saved.show()
                        pass
                    elif selected_item == "Yntec/realistic-vision-v12":#
                        nama_file = nama()
                        img_binary = query(api_url="https://api-inference.huggingface.co/models/Yntec/realistic-vision-v12", prompt=self.ui.prompt.toPlainText())
                        image = Image.open(io.BytesIO(img_binary))
                        image.save(f'./res/saved/ai-hub-{nama_file}.jpg', 'JPEG')
                        self.ui.hasil.setPixmap(QPixmap(f'./res/saved/ai-hub-{nama_file}.jpg'))
                        self.saved.show()
                        pass
                    elif selected_item == "stablediffusionapi/realistic-vision-v51":#
                        nama_file = nama()
                        img_binary = query(api_url="https://api-inference.huggingface.co/models/stablediffusionapi/realistic-vision-v51", prompt=self.ui.prompt.toPlainText())
                        image = Image.open(io.BytesIO(img_binary))
                        image.save(f'./res/saved/ai-hub-{nama_file}.jpg', 'JPEG')
                        self.ui.hasil.setPixmap(QPixmap(f'./res/saved/ai-hub-{nama_file}.jpg'))
                        self.saved.show()
                        pass
                    elif selected_item == "stablediffusionapi/beautiful-realistic-asian":#
                        nama_file = nama()
                        img_binary = query(api_url="https://api-inference.huggingface.co/models/stablediffusionapi/beautiful-realistic-asian", prompt=self.ui.prompt.toPlainText())
                        image = Image.open(io.BytesIO(img_binary))
                        image.save(f'./res/saved/ai-hub-{nama_file}.jpg', 'JPEG')
                        self.ui.hasil.setPixmap(QPixmap(f'./res/saved/ai-hub-{nama_file}.jpg'))
                        self.saved.show()
                        pass
                    elif selected_item == "stablediffusionapi/realistic-vi":#
                        nama_file = nama()
                        img_binary = query(api_url="https://api-inference.huggingface.co/models/stablediffusionapi/realistic-vi", prompt=self.ui.prompt.toPlainText())
                        image = Image.open(io.BytesIO(img_binary))
                        image.save(f'./res/saved/ai-hub-{nama_file}.jpg', 'JPEG')
                        self.ui.hasil.setPixmap(QPixmap(f'./res/saved/ai-hub-{nama_file}.jpg'))
                        self.saved.show()
                        pass
                    elif selected_item == "digiplay/majicMIX_realistic_v6":#
                        nama_file = nama()
                        img_binary = query(api_url="https://api-inference.huggingface.co/models/digiplay/majicMIX_realistic_v6", prompt=self.ui.prompt.toPlainText())
                        image = Image.open(io.BytesIO(img_binary))
                        image.save(f'./res/saved/ai-hub-{nama_file}.jpg', 'JPEG')
                        self.ui.hasil.setPixmap(QPixmap(f'./res/saved/ai-hub-{nama_file}.jpg'))
                        self.saved.show()
                        pass
            else:
                self.mess.show()
            pass
        
        self.ui.generate.clicked.connect(lambda: generate())
        self.ui.frame_3.mousePressEvent = self.moveWindow
    
    def moveWindow(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clickPosition = event.globalPos()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()
        
        
class RenderMess(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_RenderMess()
        self.ui.setupUi(self)

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
class SavedMess(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SavedMess()
        self.ui.setupUi(self)

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        nama_file = nama()
        self.ui.message.setText(f"File Saved at ./res/saved/")
        
class PromptMess(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_PromptMess()
        self.ui.setupUi(self)

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
class ChekMess(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_CekMess()
        self.ui.setupUi(self)

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
class NoSupport(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_NotSupported()
        self.ui.setupUi(self)

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
class TtvWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_TextToVideo()
        self.ui.setupUi(self)

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.cpu.hide()
        self.ui.models.addItem("cerspense/zeroscope_v2_576w")
        self.ui.pushButton.clicked.connect(lambda: self.close())
        self.prompt = PromptMess()
        self.mess = RenderMess()
        self.ceks = ChekMess()
        self.device = NoSupport()
        
        def setInterferanceStep():
            self.ui.num_inference_steps.setText("25")
            pass
        
        def setNumFrames():
            self.ui.num_frames.setText("200")
            pass
        
        def generate():
            p = self.ui.num_frames.text()
            q = self.ui.num_inference_steps.text()
            if p.isalpha() or q.isalpha():
                self.ceks.show()
            else:
                if self.ui.prompt.toPlainText() == "":
                    self.prompt.show()
                else:
                    if self.ui.cuda.isChecked():
                        video_path = TextToVideo(prompt=self.ui.prompt.toPlainText(), num_frames=int(self.ui.num_frames.text()), num_inference_steps=int(self.ui.num_inference_steps.text()))
                        if video_path == "Sorry Your Device Is Not Supported":
                            self.device.show()
                        else:
                            print(video_path)
                        pass
                    else:
                        self.mess.show()
        
        self.ui.set_default1.clicked.connect(lambda: setInterferanceStep())
        self.ui.set_defautl2.clicked.connect(lambda: setNumFrames())
        self.ui.generate.clicked.connect(lambda: generate())
        self.ui.frame_3.mousePressEvent = self.moveWindow
    
    def moveWindow(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clickPosition = event.globalPos()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()
        
class IttxtWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_ImageToText()
        self.ui.setupUi(self)

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.frame_2.mousePressEvent = self.moveWindow
        self.ui.select_file.clicked.connect(lambda: self.open_file_dialog())
        self.ui.generate.clicked.connect(lambda: self.generate())
        self.ui.close_btn.clicked.connect(lambda: self.close())
        
    def generate(self):
        path = self.ui.path.text()
        captions = imagetotext(image_path=path)
        get = captions[0]
        res = get["generated_text"]
        self.ui.hasil.setText(res)
        
    def open_file_dialog(self):
        file_name = QFileDialog.getOpenFileName()
        path = file_name[0]
        self.ui.path.setText(path)
        
    def moveWindow(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clickPosition = event.globalPos()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()
            
class QAWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_Question()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.frame_3.mousePressEvent = self.moveWindow
        self.ui.close_btn.clicked.connect(lambda: self.close())
        self.ui.generate.clicked.connect(lambda: self.generate())
        self.mess = RenderMess()
    
    def generate(self):
        if self.ui.apis.isChecked():
            question = self.ui.question.toPlainText()
            context = self.ui.context.toPlainText()
            res = qa(question=question, context=context)
            self.ui.label_2.setText(res["answer"])
        else:
            self.mess.show()
        
    def moveWindow(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clickPosition = event.globalPos()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()

class TxtGen(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_TextGen()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.frame_3.mousePressEvent = self.moveWindow
        self.mess = RenderMess()
        self.ui.generate.clicked.connect(lambda: self.generate())
        
    def generate(self):
        if self.ui.apis.isChecked():
            text = self.ui.text.toPlainText()
            self.ui.text.setText(textgen(prompt=text)[0]['generated_text'])
            print(textgen(prompt=text)[0]['generated_text'])
        else:
            self.mess.show()

    def moveWindow(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clickPosition = event.globalPos()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()
            
class TextToCode(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_TextToCode()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.close_btn.clicked.connect(lambda: self.close())
        self.ui.headers.mousePressEvent = self.moveWindow
        self.ui.generate.clicked.connect(lambda: self.generate())
        self.prompt = PromptMess()
        
    def generate(self):
        if self.ui.prompt.toPlainText() == "":
            self.prompt.show()
        else:
            res = generate_code(prompt=self.ui.prompt.toPlainText())
            self.ui.code.setText(res)
        pass

    def moveWindow(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clickPosition = event.globalPos()
            event.accept()
    
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()
            
class TextToMusic(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_TextToMusic()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.frame_3.mousePressEvent = self.moveWindow
        self.ui.generate.clicked.connect(lambda: self.generate())
        self.prompt = PromptMess()
        
    def generate(self):
        nama_file = nama()
        if self.ui.prompt.toPlainText() == "":
            self.prompt.show()
        else:
            res = generate_music(prompt=self.ui.prompt.toPlainText())
            convert_audio_bytes_to_wav(audio_bytes=res, output_path=f"./res/saved/ai-hub-{nama_file}.wav")
        pass

    def moveWindow(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clickPosition = event.globalPos()
            event.accept()
            
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()
            
class TTS(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_TTS()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.frame_3.mousePressEvent = self.moveWindow
        self.ui.generate.clicked.connect(lambda: self.generate())
        self.prompt = PromptMess()
        languages = lang.tts_langs()
        for code, name in languages.items():
            self.ui.comboBox.addItem(f'{name} - {code}')
        
    def generate(self):
        nama_file = nama()
        if self.ui.prompt.toPlainText() == "":
            self.prompt.show()
        else:
            text = self.ui.comboBox.currentText()
            separator = " - "
            parts = text.split(separator, 1)
            code = parts[1] if len(parts) > 1 else parts[0]
            text_to_speech(text=self.ui.prompt.toPlainText(), language=code, output_file=f"./res/saved/ai-hub-{nama_file}.mp3")
        pass

    def moveWindow(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clickPosition = event.globalPos()
            event.accept()
    
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()
            
class Conversation(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_Conversation()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.frame_3.mousePressEvent = self.moveWindow
        self.ui.generate.clicked.connect(lambda: self.generate())
        self.prompt = PromptMess()
        self.setting = OpenSettings()
        self.ui.settings.clicked.connect(lambda: self.settings())
        self.ui.chat_list.setWordWrap(True)
        
    def settings(self):
        self.setting.show()
    
    def generate(self):
        teks = self.ui.prompt.toPlainText()
        self.ui.chat_list.addItem(f'You: {teks}')
        j = open("./config.json")
        data = json.load(j)
        models = data["chat_models"]
        res = ChatModels(text=teks, models=models)
        self.ui.chat_list.addItem(f'AI: {insert_newline(res)}')
        pass
    
    def moveWindow(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clickPosition = event.globalPos()
            event.accept()
    
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()
            
class OpenSettings(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.frame_3.mousePressEvent = self.moveWindow
        self.ui.comboBox.addItem("GPT-3.5")
        self.ui.comboBox.addItem("BARD-AI")
        self.ui.comboBox.addItem("SIM-SIMI")
        self.ui.comboBox.addItem("CHATTY-AI")
        self.ui.pushButton.clicked.connect(lambda: self.generate())
        
    def generate(self):
        if self.ui.comboBox.currentText() == "GPT-3.5":
            # Buka file config.json
            with open("config.json", "r") as f:
                data = json.load(f)

            # Ubah nilai chat_models
            data["chat_models"] = "GPT-3.5"

            # Simpan perubahan ke file
            with open("config.json", "w") as f:
                json.dump(data, f)
        elif self.ui.comboBox.currentText() == "BARD-AI":
            with open("config.json", "r") as f:
                data = json.load(f)

            # Ubah nilai chat_models
            data["chat_models"] = "BARD-AI"

            # Simpan perubahan ke file
            with open("config.json", "w") as f:
                json.dump(data, f)
        elif self.ui.comboBox.currentText() == "SIM-SIMI":
            with open("config.json", "r") as f:
                data = json.load(f)

            # Ubah nilai chat_models
            data["chat_models"] = "SIM-SIMI"

            # Simpan perubahan ke file
            with open("config.json", "w") as f:
                json.dump(data, f)
        elif self.ui.comboBox.currentText() == "CHATTY-AI":
            with open("config.json", "r") as f:
                data = json.load(f)

            # Ubah nilai chat_models
            data["chat_models"] = "CHATTY-AI"

            # Simpan perubahan ke file
            with open("config.json", "w") as f:
                json.dump(data, f)
        pass
    
    def moveWindow(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clickPosition = event.globalPos()
            event.accept()
    
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()
            
class Maker(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Maker()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.frame_3.mousePressEvent = (self.moveWindow)
        self.ui.effect_list.addItems(photooxy_list)
        self.ui.generate.clicked.connect(lambda: self.generate())
        self.saved = SavedMess()
    
    def generate(self):
        nama_file = nama()
        models="PhotoOxy"
        #print(self.ui.effect_list.currentText())
        img_binary = maker(models=models, text1=self.ui.input.toPlainText(), name=self.ui.effect_list.currentText())
        image = Image.open(io.BytesIO(img_binary))
        image.save(f'./res/saved/ai-hub-{nama_file}.jpg', 'JPEG')
        self.ui.label_4.setPixmap(QPixmap(f'./res/saved/ai-hub-{nama_file}.jpg'))
        self.saved.show()
        pass
    
    def moveWindow(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clickPosition = event.globalPos()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
                
         # Initialize UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Set and start GIF
        gif_file = "./res/image/vader.gif"
        movie = QtGui.QMovie(gif_file)
        self.ui.gif_lable.setMovie(movie)
        movie.start()

        # Define and connect button clicks
        self.window2 = TtiWindow()
        self.window3 = TtvWindow()
        self.window4 = IttxtWindow()
        self.window5 = QAWindow()
        self.window6 = TxtGen()
        self.window7 = TextToCode()
        self.window8 = TextToMusic()
        self.window9 = TTS()
        self.window10 = Conversation()
        self.window11 = Maker()
        
        self.ui.frame_10.hide()
        def openWindow2():
            self.window2.show()

        def openWindow3():
            self.window3.show()
            
        def openWindow4():
            self.window4.show()
            
        def openWindow5():
            self.window5.show()
            
        def openWindow6():
            self.window6.show()
        
        def openWindow7():
            self.window7.show()
            
        def openWindow8():
            self.window8.show()
            
        def openWindow9():
            self.window9.show()
            
        def openWindow10():
            self.window10.show()
            
        def openWindow11():
            self.window11.show()

        self.ui.tti_button.clicked.connect(openWindow2)
        self.ui.ttv_button.clicked.connect(openWindow3)
        self.ui.tttxt_button.clicked.connect(openWindow4)
        self.ui.qa_buttton.clicked.connect(openWindow5)
        self.ui.tg_button.clicked.connect(openWindow6)
        self.ui.ttc_button.clicked.connect(openWindow7)
        self.ui.ttm_button.clicked.connect(openWindow8)
        self.ui.tts_button.clicked.connect(openWindow9)
        self.ui.con_button.clicked.connect(openWindow10)
        self.ui.im_button.clicked.connect(openWindow11)

                # Move window when frame_2 is clicked
        self.ui.frame_2.mousePressEvent = self.moveWindow

    def moveWindow(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clickPosition = event.globalPos()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()


# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashWindow()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(80)

        # CHANGE DESCRIPTION

        # Change Texts
        QtCore.QTimer.singleShot(1000, lambda: self.ui.label_loading.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_loading.setText("<strong>LOADING</strong> USER INTERFACE"))
        QtCore.QTimer.singleShot(5000, lambda: self.ui.label_loading.setText("<strong>CHECKING</strong> UPDATES"))
        QtCore.QTimer.singleShot(7000, lambda: self.ui.label_loading.setText("<strong>INITIALIZING</strong> APPLICATION"))
        QtCore.QTimer.singleShot(9000, lambda: self.ui.label_loading.setText("<strong>DONE</strong> "))
        


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec())