import numpy as np
from body_part_angle import BodyPartAngle
from utils import *


class TypeOfExercise(BodyPartAngle):
    def __init__(self, landmarks):
        super().__init__(landmarks)

    def push_up(self, counter, status):
        left_arm_angle = self.angle_of_the_left_arm()
        right_arm_angle = self.angle_of_the_left_arm()
        avg_arm_angle = (left_arm_angle + right_arm_angle) // 2

        if status:
            if avg_arm_angle < 70:
                counter += 1
                status = False
        else:
            if avg_arm_angle > 160:
                status = True

        return [counter, status]


    def pull_up(self, counter, status):
        nose = detection_body_part(self.landmarks, "NOSE")
        left_elbow = detection_body_part(self.landmarks, "LEFT_ELBOW")
        right_elbow = detection_body_part(self.landmarks, "RIGHT_ELBOW")
        avg_shoulder_y = (left_elbow[1] + right_elbow[1]) / 2

        if status:
            if nose[1] > avg_shoulder_y:
                counter += 1
                status = False

        else:
            if nose[1] < avg_shoulder_y:
                status = True

        return [counter, status]

    def squat(self, counter, status):
        left_leg_angle = self.angle_of_the_right_leg()
        right_leg_angle = self.angle_of_the_left_leg()
        avg_leg_angle = (left_leg_angle + right_leg_angle) // 2

        if status:
            if avg_leg_angle < 70:
                counter += 1
                status = False
        else:
            if avg_leg_angle > 160:
                status = True

        return [counter, status]

    def walk(self, counter, status):
        right_knee = detection_body_part(self.landmarks, "RIGHT_KNEE")
        left_knee = detection_body_part(self.landmarks, "LEFT_KNEE")

        if status:
            if left_knee[0] > right_knee[0]:
                counter += 1
                status = False

        else:
            if left_knee[0] < right_knee[0]:
                counter += 1
                status = True

        return [counter, status]

    def sit_up(self, counter, status):
        angle = self.angle_of_the_abdomen()
        if status:
            if angle < 55:
                counter += 1
                status = False
        else:
            if angle > 105:
                status = True

        return [counter, status]
    def jumping_jacks(self, counter, status):
        left_shoulder = detection_body_part(self.landmarks, "LEFT_SHOULDER")
        right_shoulder = detection_body_part(self.landmarks, "RIGHT_SHOULDER")
        avg_shoulder_x = (left_shoulder[0] + right_shoulder[0]) / 2

        if status:
            if avg_shoulder_x > 0.5:
                counter += 1
                status = False
        else:
            if avg_shoulder_x < 0.2:
                status = True

        return [counter, status]

    def lunges(self, counter, status):
        left_hip = detection_body_part(self.landmarks, "LEFT_HIP")
        right_hip = detection_body_part(self.landmarks, "RIGHT_HIP")

        if status:
            if left_hip[1] > right_hip[1]:
                counter += 1
                status = False
        else:
            if left_hip[1] < right_hip[1]:
                status = True

        return [counter, status]

    def leg_raises(self, counter, status):
        left_ankle = detection_body_part(self.landmarks, "LEFT_ANKLE")
        right_ankle = detection_body_part(self.landmarks, "RIGHT_ANKLE")

        if status:
            if left_ankle[1] < right_ankle[1]:
                counter += 1
                status = False
        else:
            if left_ankle[1] > right_ankle[1]:
                status = True

        return [counter, status]

    def burpees(self, counter, status):
        left_knee = detection_body_part(self.landmarks, "LEFT_KNEE")
        right_knee = detection_body_part(self.landmarks, "RIGHT_KNEE")
        avg_knee_y = (left_knee[1] + right_knee[1]) / 2

        if status:
            if avg_knee_y > 0.5:
                counter += 1
                status = False
        else:
            if avg_knee_y < 0.1:
                status = True

        return [counter, status]

    def calculate_exercise(self, exercise_type, counter, status):
        if exercise_type == "push-up":
            counter, status = TypeOfExercise(self.landmarks).push_up(
                counter, status)
        elif exercise_type == "pull-up":
            counter, status = TypeOfExercise(self.landmarks).pull_up(
                counter, status)
        elif exercise_type == "squat":
            counter, status = TypeOfExercise(self.landmarks).squat(
                counter, status)
        elif exercise_type == "walk":
            counter, status = TypeOfExercise(self.landmarks).walk(
                counter, status)
        elif exercise_type == "sit-up":
            counter, status = TypeOfExercise(self.landmarks).sit_up(
                counter, status)
        elif exercise_type == "jumping-jacks":
            counter, status = TypeOfExercise(self.landmarks).jumping_jacks(
                counter, status)
        elif exercise_type == "lunges":
            counter, status = TypeOfExercise(self.landmarks).lunges(
                counter, status)
        elif exercise_type == "leg-raises":
            counter, status = TypeOfExercise(self.landmarks).leg_raises(
                counter, status)
        elif exercise_type == "burpees":
            counter, status = TypeOfExercise(self.landmarks).burpees(
                counter, status)
        return [counter, status]