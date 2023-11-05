# Quaternion and DualQuaternion Package

This package provides a simple implementation of Quaternion and DualQuaternion classes for representing and manipulating quaternions and dual quaternions in Python.

## Installation

You can install the library using `pip`:

```bash
pip install neura_dual_quaternions
```

## Usage

Here's how to use the `Quaternion` and `DualQuaternion` classes:

### Quaternion

```python
import numpy as np
from neura_dual_quaternions import Quaternion

# Create an identity quaternion
q = Quaternion(1,0,0,0)

# create quaternions from axis angle constructor
rotation_axis_x = np.array([1,0,0])
rotation_axis_z = np.array([0,1,0])

q1 = Quaternion.fromAxisAngle(0.2*np.pi, rotation_axis_x)
q2 = Quaternion.fromAxisAngle(0.5*np.pi, rotation_axis_y)

# Quaternion multiplication
q_product = q1 * q2

print(q_product)
```

### DualQuaternion

```python
import numpy as np
from neura_dual_quaternions import DualQuaternion

# Create identity dual quaternions
dq1 = DualQuaternion(1,0,0,0, 0,0,0,0)

rotation_axis_x = np.array([1,0,0])

rot = Quaternion.fromAxisAngle(0.2*np.pi, rotation_axis_x)
pos = np.array([1, 0.4, 0.55])

dq2 = DualQuaternion.fromQuatPos(rot, pos)

# DualQuaternion multiplication and addition
dq_sum = dq1 + dq2
dq_product = dq1 * dq2

print(dq_sum)
print(dq_product)
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
