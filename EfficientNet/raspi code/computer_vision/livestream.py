#from pyimagesearch.motion_detection import SingleMotionDetector
from imutils.video import VideoStream
from flask import Response
from flask import Flask
from flask import render_template
import threading
import argparse
import datetime
import imutils
import time
import cv2


# Get the webcam
#cap = cv2.VideoCapture(0)

# initialize the output frame and a lock used to ensure thread-safe
# exchanges of the output frames (useful when multiple browsers/tabs
# are viewing the stream)
outputFrame = None
lock = threading.Lock()
# initialize a flask object
app = Flask(__name__)
# initialize the video stream and allow the camera sensor to
# warmup
#vs = VideoStream(usePiCamera=1).start()
vs = VideoStream(src=0).start()
time.sleep(2.0)

@app.route("/")
def index():
	# return the rendered template
	return render_template("index.html")

def generate():
	# grab global references to the output frame and lock variables
	global outputFrame, lock
	# loop over frames from the output stream
	while True:
		# wait until the lock is acquired
		with lock:
			# check if the output frame is available, otherwise skip
			# the iteration of the loop
			if outputFrame is None:
				continue
			# encode the frame in JPEG format
			(flag, encodedImage) = cv2.imencode(".jpg", outputFrame)
			# ensure the frame was successfully encoded
			if not flag:
				continue
		# yield the output frame in the byte format
		yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
			bytearray(encodedImage) + b'\r\n')

@app.route("/video_feed")
def video_feed():
	# return the response generated along with the specific media
	# type (mime type)
	return Response(generate(),
		mimetype = "multipart/x-mixed-replace; boundary=frame")

def process_image(put_time_stamp):
	# grab global references to the video stream, output frame, and
	# lock variables
	global vs, outputFrame, lock
	# initialize the motion detector and the total number of frames
	
    # loop over frames from the video stream
	while True:
		# read the next frame from the video stream, resize it,
		# convert the frame to grayscale, and blur it
		frame = vs.read()
		if put_time_stamp:
			# grab the current timestamp and draw it on the frame
			timestamp = datetime.datetime.now()
			cv2.putText(frame, timestamp.strftime("%A %d %B %Y %I:%M:%S%p"),
                        (10, frame.shape[0] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
        
		# acquire the lock, set the output frame, and release the
		# lock
		with lock:
			outputFrame = frame.copy()



# check to see if this is the main thread of execution
if __name__ == '__main__':
	# construct the argument parser and parse command line arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--ip", type=str, required=True,
		help="ip address of the device")
	ap.add_argument("-o", "--port", type=int, required=True,
		help="ephemeral port number of the server (1024 to 65535)")
	ap.add_argument("-f", "--time_stamp", type=int, default=1,
		help="Whether to print time stamp on the video")
	args = vars(ap.parse_args())
	# start a thread that will perform motion detection
	t = threading.Thread(target=process_image, args=(
		args["time_stamp"],))
	t.daemon = True
	t.start()
	
	# start the flask app
	app.run(host=args["ip"], port=args["port"], debug=True,
		threaded=True, use_reloader=False)
# release the video stream pointer
vs.stop()



'''

while True:
    # Step 1: Capture the frame
    _, frame = cap.read()

    # Step 2: Show the frame with blurred background
    cv2.imshow("Webcam", frame)
    
    # If q is pressed terminate
    if cv2.waitKey(1) == ord('q'):
        break
    

# Release and destroy all windows
cap.release()
cv2.destroyAllWindows()



'''













