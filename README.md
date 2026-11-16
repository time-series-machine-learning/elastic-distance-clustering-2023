# A review and evaluation of elastic distance functions for time series clustering

Code and results for the paper "A review and evaluation of elastic distance functions
for time series clustering" published in Knowledge and Information Systems, which
compares nine elastic distance functions and Euclidean distance with k-means and
k-medoids clustering on 112 UCR datasets.

The paper is open access and available from
[Springer](https://doi.org/10.1007/s10115-023-01952-0).

## Contents

| Path | Description |
|---|---|
| [results/5.1](results/5.1) | Distances with k-means, Section 5.1 (`normalised`: Figures 9 and 11, `regular`: Figure 10) |
| [results/5.2](results/5.2) | Distances with k-medoids, Section 5.2 (`normalised`: Figure 12, `regular`: Figure 13) |
| [results/5.3](results/5.3) | Clustering initialisation algorithms, Section 5.3 (Figure 14) |
| [results/5.4.1](results/5.4.1) | DTW warping window variants, Sections 5.4.1 and 5.4.2 (Figure 15) |
| [results/5.4.3](results/5.4.3) | k-means with DBA against the best k-means and k-medoids distances, Section 5.4.3 (Figures 19 and 20) |
| [results/5.4.3-Fig21](results/5.4.3-Fig21) | Two DBA implementations against MSM, Section 5.4.3 (Figure 21) |
| [set_distance_clusterer.py](set_distance_clusterer.py) | The clusterers used in the experiments |
| [run_distance_experiments.py](run_distance_experiments.py) | Script to run a single experiment |
| [distance_based_clustering.ipynb](distance_based_clustering.ipynb) | Example of using the clusterers directly |
| [alignment_and_paths_figures.ipynb](alignment_and_paths_figures.ipynb) | Distances, alignment paths and the path and alignment figures |
| [package_distance_timing.ipynb](package_distance_timing.ipynb) | DTW timing comparison of Python packages, with outputs from the time of publication |
| [static_publication_reqs.txt](static_publication_reqs.txt) | Dependency versions used at the time of publication |

Each results file is named `<split>_<metric>.csv`, where the split is the `TRAIN` or
`TEST` data and the metric is clustering accuracy (`clacc`), Rand index (`ri`),
adjusted Rand index (`ari`), mutual information (`mi`), normalised mutual information
(`nmi`) or adjusted mutual information (`ami`). Files have one row per dataset and one
column per clusterer. `normalised` results use z-normalised series and `regular`
results use the raw series. The [results/5.3](results/5.3) files are named
`<clusterer>_<initialisation>_TEST_clacc.csv`, where `Plus` is k-means++
initialisation.

## Datasets

The 112 UCR datasets are from the
[UCR Time Series Classification Archive 2018](https://doi.org/10.5281/zenodo.11198697).
More information on the datasets is available at
[timeseriesclassification.com](http://www.timeseriesclassification.com).

## Running the experiments

There are two ways to run the code: with the latest versions, or with the versions
recorded at the time of publication. Results from the latest versions may differ from
the published results files, as the algorithms have changed since publication.

### Latest versions

Clone this repository and install the latest `tsml-eval`:

    pip install -r requirements.txt

Run [run_distance_experiments.py](run_distance_experiments.py) from the repository
root with the following arguments:

1. Path to the data directory
2. Path to the results directory
3. The name of the model to run (see
   [set_distance_clusterer.py](set_distance_clusterer.py), i.e. KMeans-dtw,
   KMeans-msm, KMedoids-dtw)
4. The name of the problem to run
5. The resample number to run (0 is base train/test split)

i.e. to run the ItalyPowerDemand problem using k-means with the MSM distance on the
base train/test split:

    python run_distance_experiments.py data/ results/ KMeans-msm ItalyPowerDemand 0

Add `-rn` to z-normalise the series. Running the script without arguments runs
KMeans-dtw on a small example dataset included with `tsml-eval` and writes to
`test_output/`.

The code in this repository was last checked in November 2026 with `tsml-eval` 0.7.0,
`aeon` 1.5.0 and `tsml` 0.10.0 on Python 3.12. It is not actively maintained against
new releases.

### As published

The paper used `aeon` 0.4.0. `tsml-eval` 0.1.1 contains this code, so install it with
the dependency versions recorded at the time of publication. This requires Python 3.9,
3.10 or 3.11. Results from this setup may not match the published results files
exactly.

    pip install -r static_publication_reqs.txt
    pip install --no-deps tsml-eval==0.1.1
    python -m tsml_eval.publications.y2023.distance_based_clustering.run_distance_experiments data/ results/ KMeans-msm ItalyPowerDemand 0

The requirements file was generated on Windows, so `ansicon` and `jinxed` should be
removed on other operating systems.

## Using the clusterers

The clusterers and distances are available in the
[aeon](https://github.com/aeon-toolkit/aeon) Python package. They follow the
`scikit-learn` interface. See
[distance_based_clustering.ipynb](distance_based_clustering.ipynb) for an example and
[alignment_and_paths_figures.ipynb](alignment_and_paths_figures.ipynb) for the
distances and alignment paths, which can be run online using Binder:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/time-series-machine-learning/elastic-distance-clustering-2023/main?filepath=distance_based_clustering.ipynb)

## Parameters

The distance parameters, from Table 2 of the paper:

| Distance | Parameters |
|---|---|
| DTW | Window: 0.2 |
| DDTW | Window: 0.2 |
| WDTW | g: 0.05 |
| WDDTW | g: 0.05 |
| LCSS | Epsilon: 0.05 |
| ERP | g: 0.05 |
| EDR | Epsilon: 0.05 |
| MSM | c: 1 |
| TWE | Nu: 0.05, Lambda: 1 |

The clusterers use random initialisation, 10 restarts and at most 30 iterations, and
k-means uses the arithmetic mean to find the centroids. The number of clusters is the
number of classes in the dataset.

## Citation

If you use this work, please cite the paper:

```bibtex
@article{holder2024review,
  title={A review and evaluation of elastic distance functions for time series clustering},
  author={Holder, Christopher and Middlehurst, Matthew and Bagnall, Anthony},
  journal={Knowledge and Information Systems},
  volume={66},
  number={2},
  pages={765--809},
  year={2024},
  publisher={Springer},
  doi={10.1007/s10115-023-01952-0}
}
```

## Contact

For questions about the paper or this repository, feel free to email the authors or
contact us on the [aeon Discord](https://discord.gg/D6rzqHGKRJ).
