from config import GRAVITY_SPEED, GRAVITY_ACCELERATION, GRAVITY_THRESHOLD

class Gravity:
    def __init__(self):
        self.speed = GRAVITY_SPEED
        self.progress = 0

    def reset_progress(self):
        self.progress = 0

    def update_progress(self, dt):
        self.speed += GRAVITY_ACCELERATION * dt
        self.progress += self.speed * dt

        if self.progress >= GRAVITY_THRESHOLD:
            return True
        return False