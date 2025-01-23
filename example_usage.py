if __name__ == "__main__":
    sequence = "ACGTACGTACGT"
    substring_length = 3

    # Suffix Tree Example
    print("\nBuilding Suffix Tree:")
    s_tree = SuffixTree(sequence)
    s_tree.visualize()

    # Heavy Path Decomposition Example
    print("\nFinding Heavy Paths:")
    hpd = HeavyPathDecomposition()
    hpd.add_node(1)  # Root
    hpd.add_node(2, 1, weight=5)
    hpd.add_node(3, 1, weight=3)
    hpd.find_heavy_paths()
    hpd.display_paths()

    # Mappability Example
    print("\nCalculating Mappability:")
    mappability = MappabilityAnalysis(sequence, substring_length)
    f0, f1 = mappability.compute_scores()
    mappability.display_scores(f0, f1)

    # Visualization Example
    print("\nVisualizing Mappability:")
    Visualizer.plot_mappability(f0, f1)
