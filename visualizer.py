import matplotlib.pyplot as plt
import seaborn as sns

class Visualizer:
    @staticmethod
    def plot_mappability(f0, f1):
        """Plot a bar chart for F0 and F1 scores."""
        substrings = list(f0.keys())
        exact_matches = list(f0.values())
        tolerant_matches = [f1.get(k, 0) for k in substrings]

        x = range(len(substrings))
        plt.figure(figsize=(12, 6))
        plt.bar(x, exact_matches, width=0.4, label="F0 (Exact Matches)", align="center")
        plt.bar(x, tolerant_matches, width=0.4, label="F1 (One Mismatch)", align="edge")
        plt.xticks(x, substrings, rotation=45)
        plt.xlabel("Substrings")
        plt.ylabel("Counts")
        plt.title("Mappability Scores")
        plt.legend()
        plt.tight_layout()
        plt.show()
