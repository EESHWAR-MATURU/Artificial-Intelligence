import cv2
import requests
from ibm_watson import ApiException, ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


api_key = "YOUR_API_KEY"
url = "YOUR_URL"
authenticator = IAMAuthenticator(api_key)
tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    authenticator=authenticator
)
tone_analyzer.set_service_url(url)



def detect_object(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    faces = cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))


    if len(faces) > 0:
        face = faces[0]
        x, y, w, h = face
        face_image = gray[y:y+h, x:x+w]
        try:
            response = tone_analyzer.tone({'text': face_image}).get_result()
            tones = response['document_tone']['tones']
            if len(tones) > 0:
                strongest_tone = max(tones, key=lambda x: x['score'])
                if strongest_tone['tone_id'] == 'anger':
                    return '😠'
                elif strongest_tone['tone_id'] == 'disgust':
                    return '🤢'
                elif strongest_tone['tone_id'] == 'fear':
                    return '😱'
                elif strongest_tone['tone_id'] == 'joy':
                    return '😊'
                elif strongest_tone['tone_id'] == 'sadness':
                    return '😢'
                elif strongest_tone['tone_id'] == 'analytical':
                    return '🤔'
                elif strongest_tone['tone_id'] == 'confident':
                    return '😎'
                elif strongest_tone['tone_id'] == 'tentative':
                    return '😕'
        except ApiException as ex:
            print("Method failed with status code " +
                  str(ex.code) + ": " + ex.message)
    return None


cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    if not ret:
        break

    emoticon = detect_object(frame)

    if emoticon is not None:
        cv2.putText(frame, emoticon, (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Object recognition and sentiment analysis", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
