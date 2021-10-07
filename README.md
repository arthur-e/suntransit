suntransit
==========

**Simple, fast approximation of sunrise, sunset time on Earth.**

[![DOI](https://zenodo.org/badge/414701058.svg)](https://zenodo.org/badge/latestdoi/414701058)


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
np.array(sunrise_sunset(missoula, today)) + 6
# array([19.73314067,  7.06254366])
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
