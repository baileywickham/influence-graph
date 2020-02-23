import twitter

def create_api(filename):
    with open(filename, 'r') as f:
        api_key = f.readline().strip('\n')
        api_secret = f.readline().strip('\n')
        ac_token = f.readline().strip('\n')
        ac_token_sc = f.readline().strip('\n')
    return twitter.Api(api_key, api_secret, ac_token, ac_token_sc)


def print_tl(api):
    # Just for testing
    # Timeline a list of status objects
    # https://python-twitter.readthedocs.io/en/latest/_modules/twitter/models.html#Status
    timeline = api.GetUserTimeline(screen_name='realDonaldTrump', count=50)
    for t in timeline:
        print(t.text)
    return timeline


def main():
    api = create_api('secret.key')
    print_tl(api)

if __name__ == "__main__":
    main()
