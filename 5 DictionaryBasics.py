def AboutMe(Myself):
    for key,data in Myself.iteritems():
        print "My", key, "is" , data

Myself = {}
Myself["name"] = "Raquel"
Myself["age"] = "100"
Myself["country of birth"] = "America"
Myself["favorite language"] = "Python"

AboutMe(Myself)