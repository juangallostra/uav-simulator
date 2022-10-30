from abc import ABC, abstractmethod
import math

class BaseController(ABC):
    def __init__(self, parent_entity, linear_velocity, angular_velocity):
        self._parent_entity = parent_entity

        self._linear_velocity = linear_velocity
        self._angular_velocity = angular_velocity

    @abstractmethod
    def move(self, dt, held_keys):
        pass

class DroneController(BaseController):
    def __init__(self, parent_entity, linear_velocity, angular_velocity):
        super().__init__(parent_entity, linear_velocity, angular_velocity)

    def move(self, dt, held_keys):
        dist = held_keys['w'] * dt * self._linear_velocity


        self._parent_entity.x -= dist * math.cos(self._parent_entity.rotation_y * math.pi / 180)
        self._parent_entity.z += dist * math.sin(self._parent_entity.rotation_y * math.pi / 180)

        ny = self._parent_entity.y + held_keys['z'] * dt * self._linear_velocity - held_keys['x'] * dt * self._linear_velocity
        if ny >= 0.2:
            self._parent_entity.y = ny
        if ny >= 0.5:
            # Tilt drone when going forward if above threshold
            self._parent_entity.rotation_z = held_keys['w'] * -15

        self._parent_entity.rotation_y += held_keys['a'] * dt * self._angular_velocity
        self._parent_entity.rotation_y -= held_keys['d'] * dt * self._angular_velocity
