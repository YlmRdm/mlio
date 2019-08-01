from src.data import read_raw_data, preprocess_data, get_featues, get_label


def test_raw_shape():
    dframe = read_raw_data()
    assert dframe.shape == (150, 5)


def test_get_features_shape():
    dframe = read_raw_data()
    preprocessed = preprocess_data(dframe)
    features = get_featues(preprocessed)
    label = get_label(preprocessed)

    assert features.shape == (150, 4)
    assert label.shape == (150,)
