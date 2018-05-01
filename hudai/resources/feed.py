from ..helpers.resource import Resource


class FeedResource(Resource):
    def __init__(self, client):
        Resource.__init__(self, client, base_path='/users/feed')
        self.resource_name = 'Feed'

    def list(
        self,
        userId,
        companyIds=None,
        keyTerms=None,
        maxImportance=None,
        maxRelevance=None,
        minImportance=None,
        minRelevance=None,
        publishedAfter=None,
        publishedBefore=None,
        scoredAfter=None,
        scoredBefore=None,
        sourceIds=None,
        tags=None,
        text=None,
        types=None,
        weights=None
    ):
        return self._list(
            userId=userId,
            companyIds=companyIds,
            keyTerms=keyTerms,
            maxImportance=maxImportance,
            maxRelevance=maxRelevance,
            minImportance=minImportance,
            minRelevance=minRelevance,
            publishedAfter=publishedAfter,
            publishedBefore=publishedBefore,
            scoredAfter=scoredAfter,
            scoredBefore=scoredBefore,
            sourceIds=sourceIds,
            tags=tags,
            text=text,
            types=types,
            weights=weights
        )
