import requests, time

DANK_URL = "http://partify.club/api/vote"
DANK_PARAMS = {
    "accessCode":"knighthacks",
    "upvote":"true",
    "songId": None
}

DANK_SONGS = ["6Sy9BUbgFse0n0LPA5lwy5", "2kWB9IV8EHDOU9EjgxWFrF", "6JEK0CvvjDjjMUBFoXShNZ"]

def main():
    while True:
        for song_id in DANK_SONGS:
            dank_param_copy = DANK_PARAMS.copy()
            dank_param_copy["songId"] = song_id
            req = requests.post(DANK_URL, params=dank_param_copy)
            if req.status_code == 200:
                print "Mad3 a 200o|< D@n|< r3Qu3st f0r: %s" % song_id
            else:
                print "F@i13d th3 r3q w1th: %s on %s" % (str(req.status_code), song_id)
        time.sleep(3)

if __name__ == '__main__':
    main()
