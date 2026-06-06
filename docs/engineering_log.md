# Engineering Log — OpenCV Conveyor Sorting System

---

## Initial Project Planning
- Chose computer vision sorting system project because of previous experience with OpenCV
- Researched conveyer belt designs and mechanisms

#### Planned the integration of:
  - ultrasonic sensor
  - ESP-32 CAM for OpenCV object classification
  - servo-driven sorting
  - motor-powered conveyor belt 

## Research
- Looked into the use of HC-SR04 ultrasonic sensors to detect objects on a moving conveyor
- Experimented with cross-platform communication through interfacing the ESP32 with Arduino via Serial (UART) communication
- Researched basic conveyor roller design principles


---

# May 24, 2026

## Progress
- Built first physical prototype of the conveyor belt
- Tested belt movement using DC brush motors.
- Verified basic roller and frame concept.

## Challenges
- Current housing/frame is too small and needs larger dimensions.
- Roller design is unstable and needs improvement for smoother belt tracking.
- DC brush motors do not provide enough torque/control for reliable movement.

## Planned Improvements
- Redesign rollers with better alignment/flanges.
- Increase frame size and structural rigidity.
- Replace DC brush motors with gearbox motors for improved torque and speed control.

## Notes
- Belt tracking/alignment appears to be the main mechanical challenge so far.
- Need to test different belt materials and roller spacing.


---

# June 5, 2026

## Progress
- Researched MobileNetv1 and FOMO CV models for ESP32
## Notes
- Need to choose between training a computer vision model or using a pretrained model
- Need to figure out how to establish serial communication between the ESP32 and the Arduino board
