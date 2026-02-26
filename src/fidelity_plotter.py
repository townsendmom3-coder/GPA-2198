import matplotlib.pyplot as plt
import numpy as np


def generate_fidelity_plot(data):
    log_mw = np.log10(data['MW'])
    log_rf = np.log10(data['RF'])

    plt.figure(figsize=(10, 6))
    plt.scatter(log_mw, log_rf, c='blue', label='Fidelity Data')
    plt.title('Fidelity Plot: Log10(MW) vs Log10(RF)')
    plt.xlabel('Log10(MW)')
    plt.ylabel('Log10(RF)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()


def export_plot(filename):
    plt.savefig(f'{filename}.png')
    plt.savefig(f'{filename}.pdf')
    plt.close()


# Example Usage
# if __name__ == '__main__':
#     data = {'MW': [1, 10, 100], 'RF': [1, 5, 10]} # Example data
#     generate_fidelity_plot(data)
#     export_plot('fidelity_plot')
