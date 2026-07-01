import sys
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

import json
import tempfile
import matplotlib.pyplot as plt
import streamlit as st

from datetime import datetime
from pipeline.detector import Detector
from utils.fits_loader import FITSLoader

st.set_page_config(
    page_title="ExoDetect-AI",
    page_icon="🪐",
    layout="wide",
)

st.title("🪐 ExoDetect-AI")
st.caption("Developed by Team MYTHOS 2.0")

st.markdown("""
### Detecting Exoplanets from TESS Light Curves

Upload a NASA TESS FITS light curve to identify periodic transit-like
signals, estimate orbital parameters, and visualize potential
exoplanet candidates through an automated analysis pipeline.
""")

logo = Image.open("assets/mythos_logo.png")

left, center, right = st.sidebar.columns([0.5, 2, 0.5])

with center:
    st.image(logo, width=140)

st.sidebar.markdown(
    "<h3 style='text-align:right;'>Team MYTHOS 2.0</h3>",
    unsafe_allow_html=True
)

st.sidebar.header("About ExoDetect-AI")

st.sidebar.markdown("""
ExoDetect-AI is a scientific pipeline developed for the **Bharatiya Antariksh Hackathon 2026** by Team MYTHOS 2.0.

### Pipeline

- Signal preprocessing
- Detrending
- BLS period search
- Phase folding
- Transit characterization
- Signal significance estimation

Upload a TESS FITS file to begin the analysis.
""")

st.subheader("🧪 Try Example Datasets")

st.caption(
    "Don't have a FITS file? Select one of the built-in examples."
)

col1, col2 = st.columns(2)

with col1:
    example_planet = st.button("🟢 Example: Pi Mensae")

with col2:
    example_no_planet = st.button("🔴 Example: Vega")

example_path = None

if example_planet:
    example_path = "examples/Pi_Mensae.fits"

if example_no_planet:
    example_path = "examples/vega_no_transit.fits"

uploaded = st.file_uploader(
    "Upload a TESS FITS file",
    type=["fits"],
)

if uploaded or example_path:

    with st.spinner("Analyzing light curve..."):
        if uploaded:
            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".fits"
            ) as temp:

                temp.write(uploaded.read())
                path = temp.name

        else:
            path = example_path

        loader = FITSLoader()
        detector = Detector()

        time, flux = loader.load(path)
        result = detector.detect(path)

    st.header("🔍 Detection Result")

        # Decision logic
    if (
        result["snr"] >= 6
        and result["transit_depth"] < 0.05
        and result["bls_power"] > 0.05
    ):
        prediction = "Planet Candidate"

    elif (
        result["snr"] >= 3
        and result["transit_depth"] < 0.05
    ):
        prediction = "Possible Transit"

    else:
        prediction = "No Significant Transit"

        # Display prediction
    if prediction == "Planet Candidate":
        st.success("🟢 **Strong Transit Candidate Detected**")

    elif prediction == "Possible Transit":
        st.warning("🟡 **Possible Transit Candidate Detected**")

    else:
        st.error("🔴 **No Significant Transit Signal Detected**")

    if uploaded:
        st.info(f"📂 Dataset: {uploaded.name}")
    else:
        st.info(f"📂 Dataset: {Path(path).name}")

    fig = plt.figure(figsize=(12,4))
    plt.plot(
        time,
        flux,
        linewidth=0.7,
        
        color="royalblue"
    )
    plt.grid(alpha=0.3)
    plt.xlabel("Time")
    plt.ylabel("Flux")
    plt.title("Raw TESS Light Curve")
    plt.tight_layout()
    st.pyplot(fig)

    st.divider()

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Orbital Period",
        f"{result['period']:.3f} days"
    )

    c2.metric(
        "Normalized Transit Depth",
        f"{result['transit_depth']:.4f}"
    )

    c3.metric(
        "Transit Duration",
        f"{result['transit_duration']:.4f}"
    )

    c4, c5, c6 = st.columns(3)

    c4.metric(
        "SNR",
        f"{result['snr']:.2f}"
    )

    score = min(int(result["confidence"] * 100), 99)

    c5.metric(
    "Detection Score",
    f"{score}/100"
    )

    c6.metric(
        "BLS Power",
        f"{result['bls_power']:.4f}"
    )

    st.progress(result["confidence"])

    st.caption(
        f"Detection Score: {score}/100"
    )

    st.divider()

    st.subheader("Scientific Interpretation")

    if prediction == "Planet Candidate":
        st.success("""
    ### Strong Transit Candidate

    A statistically significant periodic transit-like signal has been identified in the uploaded TESS light curve.

    The recovered orbital period, transit depth and signal-to-noise ratio are consistent with a potential exoplanet transit. While additional astrophysical validation would be required, this target represents a promising exoplanet candidate.
    """)

    elif prediction == "Possible Transit":
        st.warning("""
    ### Possible Transit Candidate

    A periodic dimming event has been detected, although the recovered signal is of moderate significance.

    Further observations and additional validation would be recommended before interpreting this signal as a planetary transit.
    """)

    else:
        st.error("""
    ### No Significant Transit Detected

    No convincing periodic transit signature was identified in the uploaded light curve.

    The observed variations are more consistent with stellar variability, instrumental noise, or other non-transit effects than with a detectable exoplanet transit.
    """)
        
    st.info("""
    **Note**

    Transit depth is reported in normalized flux units after preprocessing and detrending.

    The Detection Score is an internal heuristic derived from the recovered transit signal and is intended to rank signal quality. It should not be interpreted as the probability that the object is a confirmed exoplanet.
    """)

    with st.expander("Advanced Detection Details"):
        st.json(result)

    st.download_button(
        label="⬇ Download JSON Report",
        data=json.dumps(result, indent=4),
        file_name=f"exodetect_report_{datetime.now():%Y%m%d_%H%M%S}.json",
        mime="application/json",
    )

    st.markdown("---")

    left, right = st.columns([3, 1])

    with left:
        st.caption(
            "ExoDetect-AI • Bharatiya Antariksh Hackathon 2026"
        )

    with right:
        st.caption("Version 1.0")

        st.markdown("---")

        col1, col2 = st.columns([4, 4])

    with col1:
        st.image(logo, width=90)

    with col2:
        st.caption(
            "Developed by Team MYTHOS 2.0 " 
        )  