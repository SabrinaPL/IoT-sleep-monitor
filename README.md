# Tutorial on how to build a Sleep Environment Monitor

This tutorial will guide you through the process of building a sleep environment monitor using Raspberry Pi Pico W and various sensors. The monitor will measure light, temperature and humidity and send the data to Adafruit IO for visualization and analysis. A webhook will be used to trigger an alert when the light level, temperature or humidity exceeds a certain threshold recommended for a good sleep environment.

## Title

IoT Sleep Environment Monitor.

## By

Sabrina Prichard-Lybeck (sp223kz)

## Project Overview

This project aims to create a sleep environment monitoring system that can help users optimize their sleeping conditions. By leveraging the capabilities of the Raspberry Pi Pico W and various sensors, we can gather real-time data on environmental factors that affect sleep quality. The collected data will be visualized on the Adafruit IO platform, allowing users to monitor their sleep environment easily. Additionally, the webhook integration will ensure that users receive timely alerts when any of the monitored parameters deviate from the recommended sleep conditions.

## Time Estimate

The estimated time to complete this project is approximately 6-8 hours, depending on your familiarity with the components and programming involved.

## Objective

The reason I chose to build a sleep environment monitor is based on my professional background in insomnia therapy having previously worked as a Cognitive Behavioral Therapist (CBT) and counselor in psychiatric care. I wanted to create a tool that could help individuals better understand and improve their sleep environments, since factors such as temperature, humidity and light are a part of what makes for a good sleep hygiene, ultimately contributing to better sleep quality and overall well-being. Insights from this project can be beneficial for anyone looking to enhance their sleep conditions, whether they are struggling with insomnia or simply seeking to improve their sleep hygiene. It can also give insights to how sleep environment can differ between different seasons (where factors such as temperature, humidity and light can differ a lot in the Scandinavian climate), and how to adapt to these seasonal changes.

## Materials

- Raspberry Pi Pico W
- DHT11 sensor (for temperature and humidity measurement)
- Photoresistor (for light level detection)
- Resistors
- LED lights (green, red, yellow) for visual alerts
- Breadboard and jumper wires
- Adafruit IO (for data visualization and webhook integration)

## Computer Setup

1. Install the necessary software on your computer:
    - Visual Studio Code (VS Code)
    - MicroPython extension for VS Code
    - Thonny IDE (for MicroPython development and quick testing of components)
    - Adafruit IO account (for data visualization)
2. Set up the Raspberry Pi Pico W:
    - Connect the Pico W to your computer via USB.
    - Press and hold the BOOTSEL button on the Pico W while connecting it to your computer to enter bootloader mode.
    - Copy the newest MicroPython firmware file (downloaded from the official MicroPython website) to the Pico W to install MicroPython.

## Putting everything together

Add diagrams and images of the components and how they are connected. This will help visualize the setup and make it easier to follow along.

## Platform

Adafruit IO compared to TIG-stack:
Adafruit IO is a cloud-based platform that provides an easy way to visualize and analyze data from IoT devices. It offers features such as data logging, visualization, and webhook integration, making it suitable for projects like the sleep environment monitor. The TIG-stack (Telegraf, InfluxDB, Grafana) is another option for data collection and visualization but requires more setup and configuration. For this project, Adafruit IO is chosen for its simplicity and ease of use. I also wanted to keep the project accessible for those who may not have extensive experience with setting up and managing databases or server infrastructure and explore a new platform, since I have previously used the TIG-stack for other projects.

For scaling up the project, I would consider using the TIG-stack for more advanced data analysis and visualization capabilities. The TIG-stack allows for more flexibility in data handling and can be integrated with various data sources, making it suitable for larger-scale IoT projects. An alternative to the TIG-stack could be using a cloud service like AWS IoT or Azure IoT, which provides similar capabilities with additional features such as machine learning integration and advanced analytics.
