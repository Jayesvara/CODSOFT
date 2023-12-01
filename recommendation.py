import numpy as np
from scipy.spatial.distance import cosine

# Sample user-item matrix (rows represent users, columns represent items)
user_item_matrix = np.array([
    [5, 4, 0, 0, 1],
    [0, 5, 4, 3, 2],
    [2, 3, 5, 0, 0],
    [0, 0, 4, 5, 0],
])

def cosine_similarity(user1, user2):
    """
    Compute the cosine similarity between two users.
    """
    non_zero_indices = np.logical_and(user1 != 0, user2 != 0)
    if np.any(non_zero_indices):
        return 1 - cosine(user1[non_zero_indices], user2[non_zero_indices])
    else:
        return 0  # Users have no common items

def get_similar_users(target_user, user_item_matrix):
    """
    Find users similar to the target user based on cosine similarity.
    """
    similarities = [cosine_similarity(target_user, other_user) for other_user in user_item_matrix]
    sorted_indices = np.argsort(similarities)[::-1]
    return sorted_indices[1:]  # Exclude the target user itself

def recommend_items(target_user, user_item_matrix, k=2):
    """
    Recommend items to the target user based on collaborative filtering.
    """
    similar_users = get_similar_users(target_user, user_item_matrix)[:k]
    
    # Calculate weighted average of item ratings from similar users
    recommended_items = np.average(user_item_matrix[similar_users], axis=0, weights=similarities[similar_users])

    # Exclude items already rated by the target user
    recommended_items[target_user != 0] = 0

    # Sort and return indices of recommended items
    sorted_indices = np.argsort(recommended_items)[::-1]
    return sorted_indices

# Example usage
target_user_index = 0
recommended_items = recommend_items(user_item_matrix[target_user_index], user_item_matrix)
print("Recommended items for user {}: {}".format(target_user_index, recommended_items))
