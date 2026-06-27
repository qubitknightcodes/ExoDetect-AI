from pipeline.detector import Detector

detector = Detector()

result = detector.detect(
    "data/raw/TOI-700.fits"
)

print(result)