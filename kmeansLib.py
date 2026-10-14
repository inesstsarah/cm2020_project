import numpy as np
from scipy.cluster.vq import whiten, kmeans, vq

def feature_calculation_sino(y_rvp):
    """Feature calculation for sinogram data from RVP data.
    Parameters:
        y_rvp: array of RVP sinogram data -> RVP stands for Radius, View, Plane
    Returns:
        features: array of calculated features
    """ 
    avg_pixel_values = np.mean(y_rvp, axis=(0, 1)) # average pixel values across the axes of the sinogram
    min_pixel_values = np.min(y_rvp, axis=(0, 1))
    max_pixel_values = np.max(y_rvp, axis=(0, 1))
    center_of_mass = np.array([np.sum(np.arange(y_rvp.shape[0]) * np.sum(y_rvp, axis=(1, 2))) / np.sum(y_rvp),
                               np.sum(np.arange(y_rvp.shape[1]) * np.sum(y_rvp, axis=(0, 2))) / np.sum(y_rvp)])
    # Insert center of mass calculation here 
    return avg_pixel_values, min_pixel_values, max_pixel_values, center_of_mass

# PCA for feature reduction
def pca(X, num_components):
    # Center the data
    X_centered = X - np.mean(X, axis=0)
    
    # Compute covariance matrix
    cov_matrix = np.cov(X_centered, rowvar=False)
    
    # Eigen decomposition
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
    
    # Sort eigenvalues and eigenvectors
    sorted_indices = np.argsort(eigenvalues)[::-1]
    sorted_eigenvalues = eigenvalues[sorted_indices]
    sorted_eigenvectors = eigenvectors[:, sorted_indices]
    
    # Select the top 'num_components' eigenvectors
    selected_eigenvectors = sorted_eigenvectors[:, :num_components]
    
    # Project the data onto the new feature space
    X_reduced = np.dot(X_centered, selected_eigenvectors)
    
    return X_reduced, selected_eigenvectors, sorted_eigenvalues[:num_components]

# Make K-Means Clustering Function
def kmeans_clustering(data, num_clusters):
    '''Function for clustering sinogram data with K-means algorithm
    Parameters:
        data: PCA reduced data from the sinograms
        num_clusters: number of clusters to form
        Returns:
        cluster_labels: 1D array of cluster labels for each data point
        centroids: 2D array of cluster centroids'''
    # normalize
    data = whiten(data)
    # perform k-means clustering
    centroids, distortion = kmeans(data, num_clusters)
    # assign each data point to a cluster
    cluster_labels, _ = vq(data, centroids)
    return cluster_labels, centroids, distortion

