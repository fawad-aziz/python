import twitter
api = twitter.Api(consumer_key='B4iW9VALsCTp6PcpK0Gc2wcgH',
                    consumer_secret='xwHE2lurMfBEm5SUE0UYCaR7fJVuSoGRbrIywaEgOWPF9vg9J3',
                    access_token_key='818087845265018881-c6dqe2pfsWsvnKQs1S9C8p8WxGSP0Sd',
                    access_token_secret='ByaBKi9t30pz8O88RtvQIMxrtjkq00nmyWUg5J5oZuzX0')
##print(api.VerifyCredentials())

users = api.GetFriends()
#print([u.name for u in users])

trends = api.GetTrendsCurrent()
#print([t for t in tweets])
print(trends[0])

