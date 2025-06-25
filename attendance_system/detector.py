import cv2
import requests

# Initialize camera safely
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Use CAP_DSHOW for Windows stability

if not cap.isOpened():
    print("❌ ERROR: Could not open camera.")
    exit()

# ARUCO dictionary
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
parameters = cv2.aruco.DetectorParameters()

print("✅ Camera opened. Showing webcam feed...")

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ Failed to read frame.")
        break

    # Detect markers
    corners, ids, rejected = cv2.aruco.detectMarkers(frame, aruco_dict, parameters=parameters)

    if ids is not None:
        # Draw boxes around detected markers
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)

        for id in ids.flatten():
            print(f"📷 Detected ARUCO ID: {id}")
            try:
                res = requests.post("http://127.0.0.1:8000/mark_attendance/", data={'aruco_id': int(id)})
                print(f"📝 Server Response: {res.json()}")
            except Exception as e:
                print(f"❌ Could not reach server: {e}")
    else:
        print("🔍 No markers detected in this frame.")

    # Show the video feed
    cv2.imshow("ARUCO Attendance (Press Q to quit)", frame)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
print("🛑 Camera closed.")
