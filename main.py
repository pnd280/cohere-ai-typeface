from fontTools.ttLib import woff2

def convert_woff2_to_ttf(input_path, output_path):
    with open(input_path, 'rb') as infile:
        with open(output_path, 'wb') as outfile:
            woff2.decompress(infile, outfile)

# Example usage
convert_woff2_to_ttf('./CohereMono-Regular.d3cdd41a.woff2', './CohereMono-Regular.ttf')
convert_woff2_to_ttf('./CohereText-Regular.870d4a70.woff2', './CohereText-Regular.ttf')
convert_woff2_to_ttf('./CohereVariable.e68773ed.woff2', './CohereVariable.ttf')