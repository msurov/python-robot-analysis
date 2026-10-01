Project structure:
=

The project demonstrates the structure of a typical python project.

```txt
root/
│
├── src/                          ← source files folder
│	│
│	├── robot_dynamics/           ← package
│	│   ├── __init__.py           ← marks robot_dynamics as a package
│	│   ├── dynamics.py           ← submodule "robot_dynamics.dynamics"
│	│   └── parameters.py         ← submodule "robot_dynamics.parameters"
│	│
│	├── robot_visualization/      ← package
│	│   ├── __init__.py
│	│   ├── draw_primitives.py    ← submodule "robot_visualization.draw_primitives"
│	│   ├── animate.py            ← submodule "robot_visualization.animate"
│	│   └── record_video.py       ← submodule "robot_visualization.record_video"
│	│
│	├── common/                   ← package
│	│   ├── __init__.py
│	│   ├── geom_utils.py         ← submodule "common.geom_utils"
│	│   ├── quaternions.py        ← submodule "common.quaternions"
│	│   └── linalg.py             ← submodule "common.linalg"
│	│
│	└── robot_scenarios/          ← package
│	    ├── __init__.py
│	    └── launch_free_motion.py ← submodule "robot_scenarios.launch_free_motion"
│	 
└── tests/                      ← tests folder
	│
	├── robot_dynamics/
	│   ├── test_dynamics.py
	│   └── test_parameters.py
	│
	├── common/
	│   ├── __init__.py
	│   ├── test_geom_utils.py
	│   ├── test_quaternions.py
	│   └── test_linalg.py
    ...
```
