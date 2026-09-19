# 🏗️ Concrete Surface Crack Detection & Structural Defect Inspection v1.0

<div align="center">

[![Deep Learning](https://img.shields.io/badge/Deep%20Learning-YOLO-blue.svg?style=for-the-badge)](https://pytorch.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-Computer%20Vision-EE4C2C.svg?style=for-the-badge&logo=pytorch)](https://pytorch.org)
[![OpenCV](https://img.shields.io/badge/OpenCV-Image%20Analysis-5C3EE8.svg?style=for-the-badge)](https://opencv.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

**Automated computer vision system for detecting and localizing concrete cracks, surface fissures, and structural wear on bridges, buildings, and pavements.**

</div>

---

## 📌 Overview

Visual inspection of concrete civil infrastructure is traditionally labor-intensive and dangerous. This project automates structural health monitoring by employing deep learning to inspect concrete surfaces and localize cracks before catastrophic failures occur.

---

## 🎯 Defect Classes

| Class | Description | Severity |
| :--- | :--- | :--- |
| **Longitudinal Cracks** | Linear cracks along the stress axis | Medium ⚠️ |
| **Transverse Cracks** | Perpendicular fractures across structure beams | High 🚨 |
| **Alligator Cracks** | Interconnected pattern indicative of base failure | High 🚨 |
| **Surface Spalling** | Concrete flaking exposing internal aggregate | Critical 🛑 |

---

## ⚡ Features

- **🔍 High-Resolution Crack Segmentation**: Detects micro-fissures and macro-fractures across diverse concrete textures.
- **📸 Batch Image & Video Analysis**: Tested on both stationary drone imagery and mobile camera video feeds.
- **📊 Pre-Trained Weights**: Ready-to-evaluate model weights stored in `model/best.pt`.

---

## 🛠️ Quick Start

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Detection on Test Image**:
   ```bash
   python detect.py --weights model/best.pt --source Output_image.jpg
   ```

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for details.
