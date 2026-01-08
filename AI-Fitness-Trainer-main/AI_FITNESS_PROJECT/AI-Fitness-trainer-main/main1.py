import cv2
import threading
import time
import mediapipe as mp
from utils import score_table
from body_part_angle import BodyPartAngle
from types_of_exercise import TypeOfExercise

class ExerciseTracker:
    def __init__(self, exercise_type):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_pose = mp.solutions.pose
        self.exercise_type = exercise_type

    def run(self):
        cap = cv2.VideoCapture(0)
        cap.set(3, 800)
        cap.set(4, 480)

        with self.mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            counter = 0
            status = True
            start_time = time.time()

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                frame = cv2.resize(frame, (800, 480))
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False
                results = pose.process(image)
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                try:
                    landmarks = results.pose_landmarks.landmark
                    if self.exercise_type.lower() == 'walk':
                        elapsed = int(time.time() - start_time)
                        cv2.putText(image, f"Walking Time: {elapsed}s", (30, 60),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 200, 0), 3)
                        if elapsed >= 120:
                            break
                    else:
                        counter, status = TypeOfExercise(landmarks).calculate_exercise(
                            self.exercise_type, counter, status)

                        image = score_table(self.exercise_type, image, counter, status)

                        if counter >= 15:
                            break
                except:
                    pass

                self.mp_drawing.draw_landmarks(
                    image,
                    results.pose_landmarks,
                    self.mp_pose.POSE_CONNECTIONS,
                    self.mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2, circle_radius=2),
                    self.mp_drawing.DrawingSpec(color=(174, 139, 45), thickness=2, circle_radius=2),
                )

                cv2.imshow('Workout', image)

                key = cv2.waitKey(10) & 0xFF
                if key == ord('q') or cv2.getWindowProperty('Workout', cv2.WND_PROP_VISIBLE) < 1:
                    break

            cap.release()
            cv2.destroyAllWindows()

    def run_in_thread(self):
        thread = threading.Thread(target=self.run)
        thread.start()
        return thread


# For standalone usage
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--exercise_type", required=True, type=str,
                        help="Type of exercise: push-up, pull-up, sit-up, walk, etc.")
    args = parser.parse_args()

    tracker = ExerciseTracker(args.exercise_type)
    tracker.run()
