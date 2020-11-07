import json
import sys
from reposcorer.scorer import score_repository

if __name__ == '__main__':
    scores = score_repository(sys.argv[1], sys.argv[2], sys.argv[3])
    print(json.dumps(scores))
