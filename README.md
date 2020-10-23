# fViz

![GitHub Contributors](https://img.shields.io/github/contributors/fastboardAI/fViz?style=for-the-badge)
![Lines of Code](https://img.shields.io/tokei/lines/github/fastboardAI/fViz?style=for-the-badge)

> A light-weight visualization library for multi-platform visualization.

## Key Features

* Multi-platform Python library for visualization.
* Selectable and highly configurable plotter modules.

## Usage

The following script initializes and updates a simple square function:

```python
# dependencies
from fViz.ui import Figure
import numpy as np

# initialize figure
dim = 101
xs = np.linspace(0, 1, dim).tolist()
plot_params = {
    'title': 'UI Figure Example',
    'x_label': 'X-axis',
    'y_label': 'Y-axis'
}
f = Figure(plot_params, xs)

# update figure
ys = np.zeros(dim)
ys[:] = np.NaN
for i in range(dim):
    ys[i] = (i/dim)**2
    f.update(xs, ys, hold=False)
```

Examples on usage of various modules can be found in the [`examples`](./examples) folder.

### Structure

```
ROOT_DIR/
|
│───examples/
│   └───...
|
│───fViz/
│   ├───foo/
│   │   ├───__init__.py
│   │   ├───bar.py
│   │   └───...
│   │   
│   └───__init__.py
│
├───.gitignore
├───CHANGELOG.md
├───LICENSE
├───README.md
├───requirements.txt
└───setup.py
```