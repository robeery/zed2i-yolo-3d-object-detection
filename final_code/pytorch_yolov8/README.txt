//RO
1) Camera ZED2i este conectata si trece cu succes de aplicatia ZED Diagnostic
2) Se activeaza mediul virtual (requirements.txt de pe github)
3) Se intra din terminal in folder descarcat
4) se adauga best2.pt in folderul pytorch_yolov8
5*) Se deschide detector.py
5) Se ruleaza din terminal comanda:
python detector.py --weights best2.pt --img_size 640 --conf_thres 0.4

MENTIUNE: Fisierul best2.pt (modelul YOLO antrenat de noi) este prea mare pentru a fi incarcat pe github, acesta poate fi trimis pe mail printr-un drive la cerere daca este nevoie.

//EN
1) The ZED2i camera is connected and successfully passes the ZED Diagnostic application
2) Activate the virtual environment (requirements.txt from github)
3) Navigate into the downloaded folder from terminal
4) Add best2.pt to the pytorch_yolov8 folder
5*) Open detector.py
5) Run the command from terminal:
python detector.py --weights best2.pt --img_size 640 --conf_thres 0.4

NOTE: The best2.pt file (our trained YOLO model) is too large to be uploaded to GitHub. It can be sent via email through a drive link upon request if needed.
