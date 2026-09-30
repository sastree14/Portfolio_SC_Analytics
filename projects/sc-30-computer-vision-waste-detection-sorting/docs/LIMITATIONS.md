# Limitations

- Detection quality depends heavily on the real camera view and labeled training data.
- Transparent glass and clear plastic can be difficult under reflections and glare.
- Heavy overlap can hide objects from the detector.
- A broad residual-waste class is intrinsically less visually stable than rigid product classes.
- New packaging or object types can create distribution shift.
- A detector can count visible objects, but it cannot infer the contents of opaque packaging without additional signals.
- Production accuracy should not be assumed from the public representative example.

These are normal design constraints for a computer-vision system and should be tested during a feasibility phase.
