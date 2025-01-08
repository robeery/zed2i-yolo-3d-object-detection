<S7:
3D Object Detection
![image](https://github.com/user-attachments/assets/ebe20d5e-c550-4f8d-a697-d31fd604d927)
![pi-proiect -2png](https://github.com/user-attachments/assets/97848f42-db0a-4fbf-905d-aa6a2e64e7a9)

S13:
--FINAL--
Cum se ruleaza codul final?

1) Camera ZED2i este conectata si trece cu succes de aplicatia ZED Diagnostic
2) Se activeaza mediul virtual (requirements.txt de pe github)
3) Se intra din terminal in folder descarcat
4) se adauga best2.pt in folderul pytorch_yolov8
5*) Se deschide detector.py
5) Se ruleaza din terminal comanda:
python detector.py --weights best2.pt --img_size 640 --conf_thres 0.4

MENTIUNE: Fisierul best2.pt (modelul YOLO antrenat de noi) este prea mare pentru a fi incarcat pe github, acesta poate fi trimis pe mail printr-un drive la cerere daca este nevoie.
