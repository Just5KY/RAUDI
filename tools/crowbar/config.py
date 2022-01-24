import helper


def get_config(organization, common_args):
    api_results = {
        'GITHUB_INFO': helper.get_latest_github_release_no_browser_download('galkan/crowbar'),
    }

    config = {
        'name': organization+'/crowbar',
        'version': api_results['GITHUB_INFO']['version'][1:],
        'buildargs': {
            'PYTHON_ALPINE_VERSION': common_args['PYTHON_ALPINE_VERSION'],
            'DOWNLOAD_URL': api_results['GITHUB_INFO']['url'], 
        },
        'tests': ['--help']
    }
    return config