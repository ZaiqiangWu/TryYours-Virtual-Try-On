from util.gdrive_downloader import download_gdrive_file
import os

download_gdrive_file("./mtviton.pth","1XJTCdRBOPVgVTmqzhVGFAgMm2NLkw5uQ")
download_gdrive_file("./discriminator_mtviton.pth","1Gi185XUAI3w4srReTbp3eIzkjFC51ym-")
download_gdrive_file("./gen.pth","1T5_YDUhYSSKPC_nZMk2NeC-XXUFoYeNy")
os.makedirs('./eval_models/weights/v0.1', exist_ok=True)
download_gdrive_file("./eval_models/weights/v0.1/alex.pth","1FF3BBSDIA3uavmAiuMH6YFCv09Lt8jUr")