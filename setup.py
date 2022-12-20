from setuptools import setup

setup(name='dart',
      version='0.1.0',
      install_requires=["gym==0.7.4",
                        "numpy",
                        "scipy",
                        "matplotlib",
                        "pandas",
                        "sklearn",
                        "tensorflow==2.11.0",
                        "mujoco-py==0.5.7"]
)