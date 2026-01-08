import cv2
import argparse
from utils import *
import mediapipe as mp
from body_part_angle import BodyPartAngle
from types_of_exercise import TypeOfExercise
import time
import sys
class ExerciseTracker:
    

    def __init__(self, args):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_pose = mp.solutions.pose
        self.exercise_types = ['pull-up', 'sit-up', 'push-up', 'squat', 'walk', 'jumping-jacks', 'lunges', 'leg-raises', 'burpees']
        self.current_index = self.exercise_types.index(args["exercise_type"])
        self.args = args

    def move_to_next_exercise(self):
        self.current_index += 1
        if self.current_index < len(self.exercise_types):
            return self.exercise_types[self.current_index]
        else:
            return None  # All exercises completed


    def run(self):
        cap = cv2.VideoCapture(0)
        cap.set(3, 800)
        cap.set(4, 480)

        with self.mp_pose.Pose(min_detection_confidence=0.5,
                                min_tracking_confidence=0.5) as pose:
            counter = 0
            status = True
            start_time = time.time()

            while self.current_index < len(self.exercise_types) and cap.isOpened():
                ret, frame = cap.read()
                frame = cv2.resize(frame, (800, 480), interpolation=cv2.INTER_AREA)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame.flags.writeable = False
                results = pose.process(frame)
                frame.flags.writeable = True
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

                try:
                    landmarks = results.pose_landmarks.landmark
                    counter, status = TypeOfExercise(landmarks).calculate_exercise(
                        self.exercise_types[self.current_index], counter, status)
                except:
                    pass

                frame = score_table(self.exercise_types[self.current_index], frame, counter, status)

                self.mp_drawing.draw_landmarks(
                    frame,
                    results.pose_landmarks,
                    self.mp_pose.POSE_CONNECTIONS,
                    self.mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2, circle_radius=2),
                    self.mp_drawing.DrawingSpec(color=(174, 139, 45), thickness=2, circle_radius=2),
                )

                cv2.imshow('Video', frame)

                key = cv2.waitKey(10) & 0xFF
                if key == ord('q') or cv2.getWindowProperty('Video', cv2.WND_PROP_VISIBLE) < 1:
                    print("🛑 User exited via back button.")
                    break

                if counter == 15:
                    self.current_index += 1
                    if self.current_index < len(self.exercise_types):
                        print(f"🎯 Moving to next exercise: {self.exercise_types[self.current_index]}")
                        time.sleep(15)
                        counter = 0
                        status = True
                        start_time = time.time()
                    else:
                        print("✅ All exercises completed.")
                        break

                if time.time() - start_time >= 120:
                    print("⌛ Time out. Moving to next.")
                    self.current_index += 1
                    counter = 0
                    status = True
                    start_time = time.time()

            cap.release()
            cv2.destroyAllWindows()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-t",
                    "--exercise_type",
                    type=str,
                    help='Type of activity to do',
                    required=True)
    args = vars(ap.parse_args())

    tracker = ExerciseTracker(args)
    tracker.run()
    sys.exit(0)

