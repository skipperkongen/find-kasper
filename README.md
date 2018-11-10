# Find Kasper

> Niveau: let øvet

Dette repository indeholder kode til at finde min søns hundebamse på billeder. Hundebamsen hedder Kasper.

Du kan naturligvis skifte hundebamsen ud med hvad du vil, men lad os antage at det er Kasper du gerne vil finde på billeder. Her er et billede af Kasper.

![Kasper](eksempel.JPG)

Første skridt er, at indsamle en masse billeder af Kasper. Vi skal bruge cirka 300 billeder af Kasper i forskellige situationer. I mappen `images` finder du en masse billeder af Kasper, som min søn har taget.

Næste skridt er, at markere hvor Kasper er placeret på hvert billede. For at træne en algoritme skal vi bruge en label for hvert sted hvor Kasper findes på et billede. Dine labels er de eksempler som algoritmen skal lære fra, så sørg for at være præcis når du angiver hvor Kasper er i billedet. Jeg anbefaler, at du bruger programmet [https://github.com/tzutalin/labelImg](https://github.com/tzutalin/labelImg) til at oprette labels.

![Labeling](labeling.gif)

I programmet vælger du om labels skal gemmes i enten PascalVOC format eller YOLO format. Vælg PascalVOC hvis du vil bruge Google's TensorFlow senere og YOLO hvis du vil bruge Joseph Redmons YOLO model. I denne tutorial har jeg valgt at bruge Tensorflow.

## Hvis du vil bruge dine egne billeder

Følg tjeklisten herunder.

- Tag 300 billeder af en bestemt ting, som du vil kunne genkende. Billederne skal være i JPEG format og gemmes i mappen 'images_raw'.
- Kør `python shrink_images.py`, hvilket gør billederne mindre og kopierer dem til mappen 'images'.

### TensorFlow Object Detection API

Vi kan benytte TensorFlows object detection API til det. Denne fremgangsmåde er baseret på følgende walk-throughs:
- [Installer tensorflow](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md)
- [Forbered data](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/preparing_inputs.md)
- [Tensorflow Object Detection guide](https://github.com/tensorflow/models/tree/master/research/object_detection)
