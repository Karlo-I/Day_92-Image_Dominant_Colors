import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Force non-GUI backend (headless)
import io
import base64

def generate_bar_chart(colours_info):
    plt.clf()  # Clear any existing figure

    fig, ax = plt.subplots(figsize=(8, 6))

    # Get hex codes and percentages
    hex_codes = [hex_code for _, hex_code, _ in colours_info]
    percentages = [percentage for _, _, percentage in colours_info]

    # Bar chart with bars along the x-axis and percentages along the y-axis
    ax.bar(hex_codes, percentages,
           color=[(r / 255, g / 255, b / 255) for r, g, b in [colour for colour, _, _ in colours_info]])
    ax.set_xlabel('Colors (HEX)')
    ax.set_ylabel('Dominance (%)')

    # Display percentage values on top of bars, where i=index(position) and v=value(percentage)
    for i, v in enumerate(percentages):
        ax.text(i, v + 0.2, f'{v:.2f}%', ha='center', va='bottom', color='black')

    plt.xticks(rotation=45, ha='right', fontsize=8) # Rotate x-axis labels for better readability

    plt.tight_layout() # Adjust the layout to avoid cutting off labels

    # Save the plot to a BytesIO object to serve as an image in the web page
    img_bytes = io.BytesIO()
    plt.savefig(img_bytes, format='png')
    img_bytes.seek(0)
    img_base64 = base64.b64encode(img_bytes.getvalue()).decode('utf-8')

    return img_base64