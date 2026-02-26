def process_gas_data(data):
    # Process gas component data
    # Assuming that 'data' is a dictionary containing gas components
    processed_data = {}
    for component in ['C1', 'nC2', 'nC3', 'nC4', 'nC5', 'N2', 'CO2']:
        if component in data:
            processed_data[component] = data[component]
    return processed_data


def apply_log_transformations(molecular_weights, response_factors):
    import numpy as np
    log_transformed_weights = np.log10(molecular_weights)
    log_transformed_factors = np.log10(response_factors)
    return log_transformed_weights, log_transformed_factors
