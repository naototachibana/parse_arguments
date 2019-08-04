import argparse
def parse_arguments():

    

    # Set up the argument parser.
    parser = argparse.ArgumentParser(description='help message of this parser')
    
    choise_list = ['hoge', 'huga']
    parser.add_argument('--method', '-m', type=str, choices=choise_list,
                        help='chosen method', default='hoge')
                        
    parser.add_argument('--label', '-l', nargs='+',
                        default=['value1', 'value2'],
                        help='labels')

    return parser.parse_args()
    
    

def main ():
    args = parse_arguments()
    print(vars(args))
