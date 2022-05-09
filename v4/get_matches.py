import sys, getopt # Needed for Arguments
import json, requests
import constants, secrets, d2dw_lib as d2dw

valid_args =  "-h                   --help                          | Information about the script. \n"
valid_args += "-d                   --debug                         | Enable detailed output for debugging. Default is False. \n"
valid_args += "-m 'Mode Name'       --mode          'Mode Name'     | Default: detail. Valid modes: " + str(constants.VALID_RUN_MODES) + " \n"
valid_args += "-b <number>          --batch_size    <number>        | Default: " + str(constants.DEFAULT_BATCH_SIZE) + ". Any amount greater than the default requires pagination. \n"
valid_args += "-l 'Language Code'   --language      'Language Code' | Default: " + constants.DEFAULT_LANGUAGE + ". Valid lenguages (tbd): " + str(constants.ALTERNATE_LANGUAGES) + " \n"
valid_args += "-f 'Format Name'     --format        'Format Name'   | Default: " + constants.DEFAULT_RESULT_FORMAT + ". 'xml' is also valid, but please, just use json. Seriously, please. \n"
valid_args += "-p {Json}            --method_params {Json}          | Optional. A json-formatted string or json object containing method specific parameters to use. \n"

help_info  = "Help Info: \n"
help_info += "This script will manage data requests using the API methods and save results to files. \n"
help_info += ". \n"

def main(argv):
    arguments = {
        'mode': 'detail',
        'batch_size': constants.DEFAULT_BATCH_SIZE,
        'language': constants.DEFAULT_LANGUAGE,
        'format': constants.DEFAULT_RESULT_FORMAT,
        'method_params': {},
        'debug': False
    }

    # get arguments
    try:
        opts, args = getopt.getopt(argv,'hdm:b:l:f:p:',['help','debug','mode=','batch_size=','language=','format=','method_params=',])
    except getopt.GetoptError:
        print('Unknown argument. Valid arguments: ' + valid_args)
        sys.exit(2)
    for opt, arg in opts: # Set the arguments as usable variables.
        if opt in ('-h', '--help'): # Print the usage when receiving -h
            print('Valid arguments: \n' + valid_args)
            print(help_info)
            sys.exit()
        elif opt in ('-m', '--mode'):
            arguments['mode'] = arg
        elif opt in ('-d', '--debug'):
            arguments['debug'] = True
        elif opt in ('-b', '--batch_size'):
            arguments['batch_size'] = arg
        elif opt in ('-l', '--language'):
            arguments['language'] = arg
        elif opt in ('-f', '--format'):
            arguments['format'] = arg
        elif opt in ('-p', '--method_params'):
            arguments['method_params'] = arg
    
    if False: # Thank you, I hate it.
        print(args)

    return arguments

def go(creds, settings):

    url = d2dw.format_url('dota2_matches', 'history', creds['key'])




    return True

# my_creds = json.loads(secrets.get_secret('steam/api', constants.DEFAULT_AWS_REGION))

# url = d2dw.format_url('dota2_matches', 'history', my_creds['key'])
# print(url)

# print(requests.api)

if __name__ == '__main__':
    # Run this with creds built in.
    settings_dict = main(sys.argv[1:])
    use_creds = json.loads(secrets.get_secret('steam/api', constants.DEFAULT_AWS_REGION))
    main_result = go(use_creds, settings_dict)
