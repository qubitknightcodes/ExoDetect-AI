import sys
from pathlib import Path

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

st.markdown("""
### Detecting Exoplanets from TESS Light Curves

Upload a NASA TESS FITS light curve to identify periodic transit-like
signals, estimate orbital parameters, and visualize potential
exoplanet candidates through an automated analysis pipeline.
""")

st.sidebar.header("About ExoDetect-AI")

st.sidebar.markdown("""
ExoDetect-AI is a scientific pipeline developed for the **Bharatiya Antariksh Hackathon 2026**.

### Pipeline

- Signal preprocessing
- Detrending
- BLS period search
- Phase folding
- Transit characterization
- Signal significance estimation

Upload a TESS FITS file to begin the analysis.
""")

uploaded = st.file_uploader(
    "Upload a TESS FITS file",
    type=["fits"],
)

if uploaded:

    with st.spinner("Analyzing light curve..."):

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".fits"
        ) as temp:

            temp.write(uploaded.read())
            path = temp.name

        loader = FITSLoader()
        detector = Detector()

        time, flux = loader.load(path)
        result = detector.detect(path)

    st.header("🔍 Detection Result")

    if result["confidence"] > 0.90:
        st.success("🟢 **Strong Transit Candidate Detected**")
    elif result["confidence"] > 0.70:
        st.warning("🟡 **Possible Transit Candidate Detected**")
    else:
        st.error("🔴 **No Significant Transit Signal Detected**")

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

    if result["confidence"] > 0.90:
        st.success("""
    ### Strong Transit Candidate

    A clear periodic transit-like signal was detected in the uploaded TESS light curve.

    The recovered orbital period is consistent with a stable repeating event. Based on the current analysis, this object represents a promising exoplanet candidate that would merit further astrophysical validation.
    """)

    elif result["confidence"] > 0.70:
        st.warning("""
    ### Possible Transit Candidate

    A periodic signal was identified, but additional observations and validation would be required to confirm its origin.
    """)

    else:
        st.error("""
    ### No Significant Transit Detected

    The current light curve does not contain a sufficiently strong periodic transit signal according to the implemented detection pipeline.
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

        st.caption(
        "ExoDetect-AI • Developed for Bharatiya Antariksh Hackathon 2026 • "
        "Transit detection using TESS light curves"
    )