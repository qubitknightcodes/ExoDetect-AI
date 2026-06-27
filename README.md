# ExoDetect-AI

ExoDetect-AI is an end-to-end software pipeline for detecting potential exoplanet transit signals from noisy astronomical light curves. It was developed as part of the **Bharatiya Antariksh Hackathon 2026** with the objective of combining classical astronomical signal processing techniques with modern machine learning components.

The project follows the standard workflow used in transit photometry instead of relying solely on a binary AI classifier. Starting from raw TESS observations, the pipeline performs preprocessing, detrending, periodic signal detection, phase folding, transit characterization and signal significance estimation before presenting the results through an interactive web application.

---

# Why this project?

Detecting exoplanets using the transit method is challenging because the brightness variations produced by a transiting planet are extremely small and are often hidden by instrumental noise, stellar variability and other astrophysical effects.

The goal of ExoDetect-AI is to build a reproducible and modular pipeline capable of identifying potential transit events while extracting physically meaningful parameters such as orbital period, transit depth and transit duration.

---

# Pipeline Overview

```
Raw TESS FITS Light Curve
            │
            ▼
      Signal Preprocessing
            │
            ▼
         Detrending
            │
            ▼
 Box Least Squares Period Search
            │
            ▼
       Phase Folding
            │
            ▼
   Transit Characterization
            │
            ▼
 Signal Significance Estimation
            │
            ▼
   Interactive Visualization
```

---

# Current Features

The current implementation includes:

* Reading raw TESS FITS light curves
* Missing value removal
* Sigma-clipping based noise filtering
* Flux normalization
* Light curve detrending
* Box Least Squares (BLS) period search
* Phase folding
* Transit depth estimation
* Transit duration estimation
* Signal-to-noise ratio estimation
* Confidence estimation
* Interactive Streamlit dashboard
* REST API using FastAPI

---

# Project Structure

```
ExoDetect-AI/

app/
│── api.py
│── streamlit_app.py

pipeline/
│── detector.py

features/
│── signal_processing.py
│── detrending.py
│── bls_search.py
│── phase_folding.py
│── transit_analysis.py
│── significance.py

utils/
│── fits_loader.py

models/

training/

evaluation/

data/
```

---

# Dataset

The project uses publicly available light curves obtained from NASA's **Transiting Exoplanet Survey Satellite (TESS)** mission.

Example targets used during development include:

* TOI-700
* WASP-18
* Pi Mensae
* HD 219134
* LHS 3844

---

# Installation

Install all required dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Application

Launch the Streamlit dashboard:

```bash
streamlit run app/streamlit_app.py
```

Launch the FastAPI server:

```bash
uvicorn app.api:app --reload
```

Interactive API documentation will be available at:

```
http://127.0.0.1:8000/docs
```

---

# Example Output

The pipeline estimates:

* Orbital period
* Transit depth
* Transit duration
* Transit center
* Signal-to-noise ratio (SNR)
* Detection confidence

The results are displayed together with the original light curve through the Streamlit interface.

---

# Technologies Used

* Python
* TensorFlow
* NumPy
* Pandas
* SciPy
* Scikit-learn
* Astropy
* Lightkurve
* Matplotlib
* Streamlit
* FastAPI

---

# Current Implementation

At the time of submission, the project provides a complete end-to-end scientific workflow capable of:

* Processing raw TESS observations
* Detecting periodic transit-like signals
* Estimating key transit parameters
* Computing signal significance
* Visualizing results through a web interface

The repository also contains the initial deep learning architecture (CNN, Transformer and XGBoost) that can be extended using larger labelled datasets in future work.

---

# Limitations

This implementation focuses on demonstrating a complete scientific workflow suitable for automated transit detection. While the deep learning models are included within the project structure, additional labelled TESS observations would be required to fully train and validate these models for large-scale classification tasks.

---

# Future Work

Potential future improvements include:

* Training deep learning models on curated labelled TESS datasets
* Multi-class classification of astrophysical events
* Improved false-positive rejection
* Bayesian uncertainty estimation
* Deployment on Hugging Face Spaces
* Support for batch processing of multiple light curves

---

# Acknowledgements

This project was developed for the **Bharatiya Antariksh Hackathon 2026** using publicly available data from NASA's TESS mission and the Mikulski Archive for Space Telescopes (MAST).

The project draws inspiration from established transit photometry workflows commonly used in observational astronomy while adapting them into a modular software pipeline suitable for interactive analysis.
