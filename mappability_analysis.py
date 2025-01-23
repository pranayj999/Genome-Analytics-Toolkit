class MappabilityAnalysis:
    def __init__(self, sequence, substring_length):
        self.sequence = sequence
        self.substring_length = substring_length

    def compute_scores(self):
        """Compute F0 (exact matches) and F1 (one mismatch allowed) scores."""
        f0 = {}
        f1 = {}
        n = len(self.sequence)
        for i in range(n - self.substring_length + 1):
            substring = self.sequence[i:i + self.substring_length]
            f0[substring] = f0.get(substring, 0) + 1
            for j in range(len(substring)):
                for char in "ACGT":
                    if char != substring[j]:
                        mutated = substring[:j] + char + substring[j + 1:]
                        f1[mutated] = f1.get(mutated, 0) + 1
        return f0, f1

    def display_scores(self, f0, f1):
        """Display the mappability scores."""
        print("Substring | F0 | F1")
        print("-------------------")
        for key in sorted(f0.keys()):
            print(f"{key} | {f0[key]} | {f1.get(key, 0)}")
