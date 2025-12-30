import base64
from IPython.display import Image, display


def render_circuit(gain_val, cutoff_val):
    """
    Generates a Mermaid block diagram with dynamic values.
    """
    # We use an f-string to inject the actual Python variables into the graph syntax
    mm_graph = f"""
    graph LR
        Input((Guitar)) --> Gain[Pre-Amp<br/>Gain: {gain_val}x]
        Gain --> Bias{{Bias}}
        Bias --> Clip[Hard Clipper<br/>Limit: 0.5]
        Clip --> Filter[Tone Stack<br/>Cutoff: {cutoff_val}Hz]
        Filter --> Output((Amp))

        style Input fill:#f9f,stroke:#333,stroke-width:2px
        style Output fill:#f9f,stroke:#333,stroke-width:2px
        style Clip fill:#e63946,stroke:#333,stroke-width:4px,color:white
        style Filter fill:#457b9d,stroke:#333,stroke-width:2px,color:white
    """

    # 1. Encode the graph string to Base64
    graphbytes = mm_graph.encode("ascii")
    base64_bytes = base64.b64encode(graphbytes)
    base64_string = base64_bytes.decode("ascii")

    # 2. Generate the URL for the rendering service
    url = "https://mermaid.ink/img/" + base64_string

    # 3. Display the image
    display(Image(url=url))


# --- Example Usage ---
# Use the variables from your previous DSP code!
current_gain = 80
current_cutoff = 4000

print(f"Generating System Diagram for Gain={current_gain}...")
render_circuit(current_gain, current_cutoff)