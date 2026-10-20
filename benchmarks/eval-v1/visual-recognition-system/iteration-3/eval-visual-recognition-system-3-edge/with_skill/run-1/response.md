The user wants me to install OpenCV and TensorFlow. This is a straightforward task - I should use bash to install these packages via pip. Let me first check the environment (Python version, pip availability, whether there's a virtual environment).

Let me check the environment first, then install.Python 3.14 is quite new — TensorFlow wheels may not exist for it yet. Let me check what's available.Python 3.14 is too new for TensorFlow. Python 3.11 is available, which is well-supported by both packages. Let me install into a venv with 3.11.Both installed. Verifying they import and work:Installed and verified in a Python 3.11 venv at `~/venvs/cv-tf`:

- **OpenCV 5.0.0** (`opencv-python`)
- **TensorFlow 2.21.0** (with Keras 3.15)

Your default `python3` is 3.14, which has no TensorFlow wheels yet, so I used the 3.11 interpreter already on your system. To use it:

```bash
source ~/venvs/cv-tf/bin/activate
```

Or call the interpreter directly: `~/venvs/cv-tf/bin/python`.