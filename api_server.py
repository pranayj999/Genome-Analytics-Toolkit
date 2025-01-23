from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/analyze', methods=['POST'])
def analyze_sequence():
    """API endpoint to analyze a given sequence."""
    data = request.json
    sequence = data.get('sequence', '')
    substring_length = data.get('substring_length', 3)

    # Perform mappability analysis
    analysis = MappabilityAnalysis(sequence, substring_length)
    f0, f1 = analysis.compute_scores()

    return jsonify({
        'f0_scores': f0,
        'f1_scores': f1
    })


if __name__ == '__main__':
    app.run(debug=True)
