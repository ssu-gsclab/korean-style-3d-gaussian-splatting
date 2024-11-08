"""
Converts between point cloud and generic data formats (e.g., CSV, Parquet).
The formats are deducted from the file extensions. All optional arguments are
not supported or relevant for all extensions.
"""
from formats.auto import load_to_dataframe, save_to_dataframe

if __name__ == '__main__':
    import argparse
    def parse_args():
        parser = argparse.ArgumentParser(description='Point cloud converter',
            epilog=__doc__)
        parser.add_argument('input_file', type=str, help='Input file')
        parser.add_argument('output_file', type=str, nargs='?', default=None, help='Output file')
        # All arguments are not supported for all conversion types
        parser.add_argument('--ply_input_format', default='nerfstudio')
        parser.add_argument('--html_template', default='')
        parser.add_argument('--r', default='rom_check')
        return parser.parse_args()
    
    args = parse_args()
    file_path = str(args.output_file)  
    if args.r == "1" : # object
        string_list = ["Z:/docker/gscServer/public/plyAssets/object/", args.output_file]
        file_path = "".join(string_list)
    elif args.r == "2" :
        string_list = ["Z:/docker/gscServer/public/plyAssets/room/", args.output_file]
        file_path = "".join(string_list)
    print(file_path)
    
    df = load_to_dataframe(args.input_file)
    if args.output_file is None:
        print(df)
    else:
        save_to_dataframe(df, file_path, args)

