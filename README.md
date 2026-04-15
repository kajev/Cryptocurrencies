# Cryptocurrency Market Clustering

Unsupervised machine learning analysis of the tradeable cryptocurrency market, using PCA and K-Means clustering to group coins by market behavior. Built to explore how dimensionality reduction and clustering can surface meaningful structure in a noisy, high-dimensional financial dataset.

## Tech Stack

- Python 3, Jupyter Notebook
- scikit-learn (PCA, KMeans, StandardScaler)
- Plotly Express, hvPlot
- pandas, NumPy

## What it does

Takes raw cryptocurrency market data, preprocesses and scales it, reduces it to three principal components via PCA, then uses K-Means clustering to group coins into four clusters based on shared behavior patterns.

The elbow curve analysis in `Using the Elbow Curve.ipynb` confirmed four as the optimal cluster count. The final clusters are visualized in both 2D and 3D scatter plots using Plotly.

## Methodology

1. **Preprocessing** - filter to only tradeable coins, drop nulls, encode categorical features, scale with StandardScaler
2. **PCA** - reduce to 3 components, retaining most of the variance while making clustering more stable
3. **Elbow curve** - test K from 1 to 10 to find the inflection point
4. **K-Means** - fit with K=4, assign each coin to a cluster
5. **Visualization** - 2D hvPlot and 3D Plotly scatter showing cluster separation across PCs

## Setup

```bash
git clone https://github.com/kajev/Cryptocurrencies.git
cd Cryptocurrencies

pip install pandas numpy scikit-learn plotly hvplot jupyter

jupyter notebook crypto_clustering.ipynb
```

## Notebooks

- `crypto_clustering.ipynb` - main analysis: full pipeline from raw data to labeled clusters
- `Principal Component Analysis.ipynb` - PCA exploration
- `KMeans.ipynb` - clustering experiments
- `Running Hierarchical Clustering.ipynb` - alternative clustering approach for comparison

## Key Findings

Four distinct clusters emerged from the data. Most coins grouped into two dominant clusters with similar volatility profiles. A smaller third cluster captured coins with unusually high supply-to-mined ratios, and a fourth isolated a couple of outlier coins with extreme trading behavior.

PCA compression made the cluster boundaries noticeably cleaner compared to running K-Means on the raw features directly.
