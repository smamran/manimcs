#!/bin/bash
# Activate the virtual environment
source ~/dev/python/manimcs/venv/bin/activate

# Set the Manim preview command to ffplay with looping
export MANIM_PREVIEW_COMMAND="ffplay -loop 0"

# Run the Manim command
manim -pqh demo.py Demo
