from setuptools import setup, find_packages

setup(
    name="Nova-AI-Assistant",
    version="1.0.0",
    author="Ritesh Rawat",
    description="Voice Controlled AI Desktop Assistant",
    packages=find_packages(),
    install_requires=[
        "SpeechRecognition",
        "pyttsx3",
        "wikipedia",
        "os",
        "webbrowser",
        "datetime",
        "pywhatkit",
    ],
)