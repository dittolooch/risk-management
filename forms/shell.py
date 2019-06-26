from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from forms.models import Incident, Complaint, RiskFactor
# And now, the end is near
# And so I face the final curtain
# My friend, I'll say it clear
# I'll state my case, of which I'm certain
# I've lived a life that's full
# I've traveled each and every highway
# But more, much more than this
# I did it my way
# Regrets, I've had a few
# But then again, too few to mention
# I did what I had to do
# And saw it through without exemption
# I planned each charted course
# Each careful step along the byway
# And more, much more than this
# I did it my way
# Yes, there were times, I'm sure you knew
# When I bit off more than I could chew
# But through it all, when there was doubt
# I ate it up and spit it out
# I faced it all and I stood tall
# And did it my way
# I've loved, I've laughed and cried
# I've had my fill my share of losing
# And now, as tears subside
# I find it all so amusing
# To think I did all that
# And may I say - not in a shy way
# Oh no, oh no, not me
# I did it my way
# For what is a man, what has he got
# If not himself, then he has naught
# To say the things he truly feels
# And not the words of one who kneels
# The record shows I took the blows
# And did it my way
# Yes, it was my way
for c in Complaint.objects.all():
    risk_factor = c.risk_factor
    risk_factor_instance = RiskFactor.objects.get(name = risk_factor)
    c.risk_factor_m = risk_factor_instance
    c.save()

for c in Incident.objects.all():
    risk_factor = c.risk_factor
    risk_factor_instance = RiskFactor.objects.get(name = risk_factor)
    c.risk_factor_m = risk_factor_instance
    c.save()



rating_map = {
'LOW':"1. Low",
"MODERATE":"2. Moderate",
"HIGH": "3. High",
"EXTREME": "4. Extreme",
"NEW":"5. New"
}
from forms.models import RiskFactor
for rf in RiskFactor.objects.all():
    rf.initial_risk_rating = rating_map[rf.initial_risk_rating]
    rf.residual_risk_rating = rating_map[rf.residual_risk_rating]
    rf.previous_residual_risk_rating = rating_map[rf.previous_residual_risk_rating]
    rf.save()
