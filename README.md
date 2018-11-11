# Find Kasper

> Niveau: let øvet

Dette repository indeholder kode til at finde min søns hundebamse på billeder. Hundebamsen hedder Kasper.

Du kan naturligvis skifte hundebamsen ud med hvad du vil, men lad os antage at det er Kasper du gerne vil finde på billeder. Her er et billede af Kasper.

![Kasper](eksempel.JPG)

Første skridt er, at indsamle en masse billeder af Kasper. Vi skal bruge cirka 300 billeder af Kasper i forskellige situationer. I mappen `images` finder du en masse billeder af Kasper, som min søn har taget.

Næste skridt er, at markere hvor Kasper er placeret på hvert billede. For at træne en algoritme skal vi bruge en markering (labels) for hvert sted hvor Kasper optræder i et billede. Vi bliver nødt til at oprette markeringerne i hånden. For at algoritmen kan lære at finde Kasper på billeder, bliver du nødt til at være ret præcis når du angiver markeringerne. Jeg anbefaler, at du bruger programmet [https://github.com/tzutalin/labelImg](https://github.com/tzutalin/labelImg) til at oprette labels.

![Labeling](labeling.gif)

I programmet vælger du om labels skal gemmes i enten PascalVOC format eller YOLO format. Vælg PascalVOC hvis du vil bruge Google's TensorFlow senere og YOLO hvis du vil bruge Joseph Redmons YOLO model. I denne tutorial går vi vores egne veje, men vi kan fint bruge det simple YOLO format.

## Hvis du vil bruge dine egne billeder

Følg tjeklisten herunder.

- Tag 300 billeder af en bestemt ting, som du vil kunne genkende. Billederne skal være i JPEG format og gemmes i mappen 'images_raw'.
- Kør `python shrink_images.py`, hvilket gør billederne mindre og kopierer dem til mappen 'images'.

### TensorFlow Object Detection API

Vi kan benytte TensorFlows object detection API til det. Denne fremgangsmåde er baseret på følgende walk-throughs:
- [Installer tensorflow](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md)
- [Forbered data](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/preparing_inputs.md)
- [Tensorflow Object Detection guide](https://github.com/tensorflow/models/tree/master/research/object_detection)

Andre gode resourcer:
- [Review of Deep Learning Algorithms for Object Detection](https://medium.com/comet-app/review-of-deep-learning-algorithms-for-object-detection-c1f3d437b852)
