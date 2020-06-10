# DLearn
DLearn, a deep learning based application that helps you better understand online video lectures by utilizing your facial expressions to determine if you are confused or stressed while watching a video, and provide you with topic recommendations that you might not have understood.

# Components
1. CNN model : Costom trained Convolution Neural Net for facial expression/emotion recognition trained on [FER-2013 dataset](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data). Certain classes were merged to create new expressions so that there are 4 classes HAPPY, NEUTRAL, CONFUSED, STRESSED.
[Trained model](https://drive.google.com/open?id=1MNhezLab0lH2n4GLV4wb8icycJKZpggR) for the CNN is available for download !
2. Text analysis : This performs recommendations of topics depending upon the exact time when you were confused during the lecture.

# How it Works
1. Select a video lecture that you want to learn from.
2. The moment you click on play button, emotion detection model kicks in and continuously monitors your behavior.
3. When the model detects that the user is stressed/confused for few continuous frames it pauses the video, analyse the transcripts of the video upto the exact time when the user seemed confused.
4. The model looks few moments into the future and past and recommend topics that might have confuseed the user. The text analays model does this by learning distributed representations form the wikipedia text of the topic and comparing the similarity of the words in the transcripts.
5. These topics are then presented to the user with a brief description abut each of them, giving user time to understand them before they jump to other advanced concepts deep into the video.

# Tech Stack
1. Tensorflow-gpu(1.7) : for creating and training CNN.
2. Flask : For deplopyment.
3. OpenCV: face-detection.
4. YouTube transcript API: To get transcripts for a given video.
5. Python ,Javascript and HTML.

# Awards
"Most technically difficult HACK" - [HACKOH/IO-2019](https://hack.osu.edu/2019/#about), NOV 2-3 (THE OHIO STATE UNIVERSITY)

# Creators: HACK_FORCE_ONE
## [Jaydeep Thik](https://www.linkedin.com/in/jaydeep-thik-7a524b12a/ "Jaydeep's LinkedIn"), [Vasudev Purandare](https://www.linkedin.com/in/vasudev-purandare/ "Vasudev's LinkedIn")
