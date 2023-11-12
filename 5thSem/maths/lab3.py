import numpy as np

def seasonal_fish_inference(seasonal_prior_bass, seasonal_prior_salmon, seasonal_likelihood_bass_given_bass, seasonal_likelihood_salmon_given_salmon, observed_bass, current_season):
    if current_season == "summer":
        seasonal_prior_bass = 0.3
        seasonal_prior_salmon = 0.7
    elif current_season == "winter":
        seasonal_prior_bass = 0.7
        seasonal_prior_salmon = 0.3
    elif current_season == "autumn":
        seasonal_prior_bass = 0.5
        seasonal_prior_salmon = 0.5
    elif current_season == "spring":
        seasonal_prior_bass = 0.6
        seasonal_prior_salmon = 0.4
    else:
        seasonal_prior_bass = 0.4
        seasonal_prior_salmon = 0.6

    seasonal_likelihood_bass = seasonal_likelihood_bass_given_bass * seasonal_prior_bass + seasonal_likelihood_salmon_given_salmon * seasonal_prior_salmon
    seasonal_likelihood_salmon = seasonal_likelihood_bass_given_bass * seasonal_prior_salmon + seasonal_likelihood_salmon_given_salmon * (1 - seasonal_prior_salmon)

    seasonal_posterior_bass = (seasonal_likelihood_bass_given_bass * seasonal_prior_bass) / seasonal_likelihood_bass
    seasonal_posterior_salmon = (seasonal_likelihood_salmon_given_salmon * seasonal_prior_salmon) / seasonal_likelihood_salmon

    normalized_posterior_bass = seasonal_posterior_bass / (seasonal_posterior_bass + seasonal_posterior_salmon)
    normalized_posterior_salmon = seasonal_posterior_salmon / (seasonal_posterior_bass + seasonal_posterior_salmon)

    if normalized_posterior_bass > normalized_posterior_salmon:
        seasonal_prediction = "SeaBass"
    else:
        seasonal_prediction = "Salmon"

    return seasonal_prediction

# Example 1 - Summer
seasonal_prior_bass = 0.4
seasonal_prior_salmon = 0.6
seasonal_likelihood_bass_given_bass = 0.9
seasonal_likelihood_salmon_given_salmon = 0.85
observed_bass = True
current_season = "summer"

seasonal_prediction = seasonal_fish_inference(seasonal_prior_bass, seasonal_prior_salmon, seasonal_likelihood_bass_given_bass, seasonal_likelihood_salmon_given_salmon, observed_bass, current_season)
print("Example 1 - Seasonal Prediction:", seasonal_prediction)

# Example 2 - Winter
seasonal_prior_bass = 0.4
seasonal_prior_salmon = 0.6
seasonal_likelihood_bass_given_bass = 0.9
seasonal_likelihood_salmon_given_salmon = 0.85
observed_bass = False
current_season = "winter"

seasonal_prediction = seasonal_fish_inference(seasonal_prior_bass, seasonal_prior_salmon, seasonal_likelihood_bass_given_bass, seasonal_likelihood_salmon_given_salmon, observed_bass, current_season)
print("Example 2 - Seasonal Prediction:", seasonal_prediction)

# Example 3 - Autumn
seasonal_prior_bass = 0.4
seasonal_prior_salmon = 0.6
seasonal_likelihood_bass_given_bass = 0.9
seasonal_likelihood_salmon_given_salmon = 0.85
observed_bass = True
current_season = "autumn"

seasonal_prediction = seasonal_fish_inference(seasonal_prior_bass, seasonal_prior_salmon, seasonal_likelihood_bass_given_bass, seasonal_likelihood_salmon_given_salmon, observed_bass, current_season)
print("Example 3 - Seasonal Prediction:", seasonal_prediction)

# Example 4 - Spring
seasonal_prior_bass = 0.4
seasonal_prior_salmon = 0.6
seasonal_likelihood_bass_given_bass = 0.9
seasonal_likelihood_salmon_given_salmon = 0.85
observed_bass = True
current_season = "spring"

seasonal_prediction = seasonal_fish_inference(seasonal_prior_bass, seasonal_prior_salmon, seasonal_likelihood_bass_given_bass, seasonal_likelihood_salmon_given_salmon, observed_bass, current_season)
print("Example 4 - Seasonal Prediction:", seasonal_prediction)
