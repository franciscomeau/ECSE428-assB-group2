# ECSE428-assB-group2

Implementation of **ramp**, a rest API postal rate calculator application with TDD implemented as a local host application.

ramp is implemented as a rest api service on a local host environment, using flask.

ramp computes postal rate of letter mail given width, height and weight and destination.

ramp rules: 

#### • The application supports linear units in mm or inches.

#### • The application supports weight units in grams or ounces.

#### • The rules for postal rate calculation are as follows:

– A standard envelope has a minimum length of 140 mm and a maximum length of 245 mm.

– A standard envelope has a minimum width of 90 mm and a maximum width of 156 mm.

– A standard envelope has a minimum weight of 3.0 g.

– A standard envelope has a maximum weight of 50.0 g.

– Non-standard envelopes cannot exceed a length of 380 mm.

– Non-standard envelopes cannot exceed a width of 270 mm.

– Non-standard envelopes cannot exceed a weight of 500 g.

– The postal rate for standard envelopes up to 30 g is $0.49.

– The postal rate for standard envelopes over 30 g up to 50 g is $0.80.

– The postal rate for non-standard envelopes up to 100 g is $0.98.

– The postal rate for non-standard envelopes over 100 g up to 500 g is $2.40.