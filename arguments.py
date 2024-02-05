import argparse

def main():
    parser = argparse.ArgumentParser(description='Parse string, int, and float arguments.')
    
    parser.add_argument('input_string', type=str, help='Input string argument')
    parser.add_argument('input_int', type=int, help='Input integer argument')
    parser.add_argument('input_float', type=float, help='Input float argument')
    
    args = parser.parse_args()

if __name__ == '__main__':
    main()