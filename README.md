# Quaternion and DualQuaternion Package

This package provides a simple implementation of Quaternion and DualQuaternion classes for representing and manipulating quaternions and dual quaternions in Python.

## Installation

Clone this repository to your local machine using `git`:

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

## Dependencies

Before using this package, you need to have Python installed on your system. The package requires the following Python libraries:

- `numpy`

You can install the required libraries using `pip`:

```bash
pip install numpy
```

## Usage

Here's how to use the `Quaternion` and `DualQuaternion` classes:

### Quaternion

```python
from quaternion_package import Quaternion
import math

# Create a quaternion
q = Quaternion(w=1, x=0, y=1, z=0)

# Quaternion multiplication
q1 = Quaternion(w=math.cos(math.pi/4), x=0, y=math.sin(math.pi/4), z=0)
q2 = Quaternion(w=0, x=1, y=0, z=0)
q_product = q1 * q2

print(q_product)
```

### DualQuaternion

```python
from quaternion_package import DualQuaternion, Quaternion

# Create dual quaternions
dq1 = DualQuaternion(
    real=Quaternion(w=1, x=0, y=1, z=0),
    dual=Quaternion(w=0, x=0.5, y=0.5, z=0)
)

dq2 = DualQuaternion(
    real=Quaternion(w=0, x=1, y=0, z=0),
    dual=Quaternion(w=0, x=0, y=0.5, z=0.5)
)

# DualQuaternion addition
dq_sum = dq1 + dq2

print(dq_sum)
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
