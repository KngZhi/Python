from sys import argv

script, user_name, relationship = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me now %s, %s?" % (user_name,relationship)
lieks = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "And How old are you?"
year = input(prompt)

print """
Alright, so you said %r about liking me, %s.
Meanwhile You live in %r. Not sure Where that is,
have a %r computer. That's great.
And  I wanna tell you even you're %r-year-old, however, I don't give a shit.
I like you.
""" %(lieks, relationship, lives, computer, year)