from sklearn.model_selection import train_test_split

from data.loader import (
    load_kepler_data,
    normalize_light_curves,
    reshape_for_cnn,
)


def prepare_data(dataset_path):

    X, y = load_kepler_data(dataset_path)

    X = normalize_light_curves(X)

    X = reshape_for_cnn(X)

    return train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )