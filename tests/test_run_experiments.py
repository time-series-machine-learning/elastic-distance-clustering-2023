"""Test file checking that the distance clustering experiments run correctly."""

import os
import runpy
import sys

import pytest
from tsml_eval.testing.testing_utils import _TEST_DATA_PATH
from tsml_eval.utils.results_validation import validate_results_file

from run_distance_experiments import (
    _DISTANCE_TEST_RESULTS_PATH,
    _REPO_PATH,
    _run_experiment,
    classifiers,
)


def test_run_distance_based_clustering_experiment(monkeypatch):
    """Test paper clustering experiments with test data and clusterer."""
    clusterer = "KMeans-dtw"
    dataset = "MinimalChinatown"
    resample = 0

    args = [
        _TEST_DATA_PATH,
        _DISTANCE_TEST_RESULTS_PATH,
        clusterer,
        dataset,
        resample,
        "-ow",
    ]

    _run_experiment(args)

    train_file = (
        f"{_DISTANCE_TEST_RESULTS_PATH}{clusterer}/Predictions/{dataset}/"
        "trainResample0.csv"
    )
    test_file = (
        f"{_DISTANCE_TEST_RESULTS_PATH}{clusterer}/Predictions/{dataset}/"
        "testResample0.csv"
    )
    assert os.path.exists(train_file)
    assert os.path.exists(test_file)
    assert validate_results_file(train_file)
    assert validate_results_file(test_file)

    # this covers both the main method and present result file checking
    monkeypatch.setattr(sys, "argv", sys.argv[:1])
    runpy.run_path(f"{_REPO_PATH}/run_distance_experiments.py", run_name="__main__")

    os.remove(train_file)
    os.remove(test_file)


@pytest.mark.parametrize("clusterer", classifiers)
def test_run_experiment_clusterers(clusterer):
    """Test each clusterer from the paper runs with the experiment settings."""
    dataset = "MinimalChinatown"

    _run_experiment(
        [_TEST_DATA_PATH, _DISTANCE_TEST_RESULTS_PATH, clusterer, dataset, 0, "-ow"]
    )

    for split in ["train", "test"]:
        file = (
            f"{_DISTANCE_TEST_RESULTS_PATH}{clusterer}/Predictions/{dataset}/"
            f"{split}Resample0.csv"
        )
        assert validate_results_file(file)
        os.remove(file)
