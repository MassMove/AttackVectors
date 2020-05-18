# Attack Vectors

A repository to monitor attack vectors mentioned in the [billion-dollar disinformation campaign to reelect the president in 2020](https://www.theatlantic.com/magazine/archive/2020/03/the-2020-disinformation-war/605530/)

## Text Messages

>In 2018, as early voting got under way in Tennessee’s Republican gubernatorial primary, [voters began receiving text messages](https://www.tennessean.com/story/news/politics/tn-elections/2018/07/13/tn-governors-race-tennesseans-receive-potentially-illegal-text-messages-attacking-randy-boyd-billlee/783785002/) attacking two of the candidates’ conservative credentials. The texts—written in a conversational style, as if they’d been sent from a friend—were unsigned, and people who tried calling the numbers received a busy signal. The local press covered the smear campaign. Law enforcement was notified. But the source of the texts was never discovered.

[17 text messages attacking Joe Biden](https://github.com/MassMove/AttackVectors/blob/master/Text%20Messages/djtfp-utm-variables.csv)

Expanded Rebrandly link: https://www.donaldjtrump.com/landing/sleepy-joe?utm_medium=sms&utm_source=opns_djt_audience11987_political&utm_campaign=20200512_na_sleepy-joe-china-nepotism-beijingbiden-az-2_djtfp_djt_na_na_audience11987_creative100112_na_na_na_na_political_na_na_na_opns_persuasion_na_na_na_na&utm_content=na&amount=na

Somebody recently shared an unsolicited text ad that they received (ostensibly) from the Trump campaign. Since they shared it, another friend shared a slightly different one with me.

We now have three data points for how their click tracking is set up. So I pulled it in for a few reasons:

1: If we see third parties using this same utm variable tracking system, it is likely they are either coordinating, sharing lists or even using the same systems. This is likely illegal and should be brought to the attention of media.

2: The campaign and other bodies may start sending people to fake news misinformation sites (the actual campaign site is full of misinformation). It may be useful to see how they are organizing their data to see if aligns with any of the sites we are tracking.

I just imported and set _ as the delimiter. A lot of the fields are still being populated with "na" but will likely be used at some point. A bunch of fields were fairly easy to identify their purpose, so Row 1 is just a rough name and Row 2 is the intuited field name that they are likely using some variant of.
