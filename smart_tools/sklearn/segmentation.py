import pandas as pd


def segment(df, features, n_clusters=3):
    """
    Segment based on features in a dataframe.
    :param df: Pandas dataframe.
    :param features: A list of features (columns)
    :param n_clusters: Number of clusters.
    :return: model, list of segments
    """
    from sklearn.cluster import KMeans
    from sklearn.preprocessing import StandardScaler

    scaler = StandardScaler()
    s = scaler.fit_transform(df[features])
    model = KMeans(n_clusters=n_clusters, random_state=0)
    segments = model.fit_predict(s)

    return model, segments


def plot(df, segments='segment', segmented_by=('feature1', 'feature2')):
    import matplotlib.pyplot as plt
    from matplotlib import colormaps as cm

    fig, ax = plt.subplots()

    # Get a color map
    cmap = cm.get_cmap('tab10')

    # Loop over each group, using the index `i` to get distinct colors
    for i, (key, group) in enumerate(df.groupby(segments)):
        group.plot(ax=ax, kind='scatter', x=segmented_by[0], y=segmented_by[1],
                   label=key, color=cmap(i % 10))  # Mod by 10 to cycle through colors if needed

    plt.legend()
    plt.show()
