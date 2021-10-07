suntransit
==========

**Simple, fast approximation of sunrise, sunset time on Earth.**

[![DOI](https://zenodo.org/badge/414701058.svg)](https://zenodo.org/badge/latestdoi/414701058)

Earth system models and other biogeochemical simulations often require an estimate of the day length and, therefore, of sunrise and sunset times. Highly precise solar transit information can be obtained from Python libraries like `pyephem` and `astral`, but these are general-purpose libraries and the corresponding routines are slow. If we can tolerate an error in transit times on the order of a few minutes, then we should also be able to calculate transit times much faster! That's the idea here: using a fast approximation for sunrise and sunset times. [Read more about the alternatives and the performance of an earlier version of this library.](http://karthur.org/2021/day-length-calculation-earth-system-models.html)


Example Use
-----------

```py
import datetime
import numpy as np
from suntransit import sunrise_sunset

missoula = (46.8625, -114.0117)
today = datetime.date(2021, 10, 7)

# Get (sunrise, sunset) hour in UTC
sunrise_sunset(missoula, today)
# (13.733140671716853, 1.062543659843307)

# Get (sunrise, sunset) hour in local time (GMT-6:00)
(np.array(sunrise_sunset(missoula, today)) - 6) % 24
# array([ 7.73314067, 19.06254366])
```

And for (quasi-)vectorization:

```py
from functools import partial

calgary = (51.0458, -114.0575)
ankara = (39.93, 32.85)

data = np.stack([missoula, calgary, ankara], axis = 0)

alt_sunrise_sunset = partial(sunrise_sunset, dt = today)
np.apply_along_axis(alt_sunrise_sunset, 1, data).round(1)
# array([[13.7,  1.1],
#        [13.8,  1. ],
#        [ 3.9, 15.4]])
```


Installation
------------

It is recommended to install with `pip`:

```sh
pip install suntransit
```

The only dependency is `numpy`.


Documentation
-------------

[Online documentation can be found here.](https://arthur-e.github.io/suntransit/)


Testing
-------

```sh
python tests/tests.py
```


References
----------

Meeus, Jean. "Astronomical Algorithms." 1991. William-Bell Inc. Richmond, Virginia, U.S.A.

U.S. Naval Observatory. "Almanac for Computers." 1990. Reproduced by
    Ed Williams. https://www.edwilliams.org/sunrise_sunset_algorithm.htm
