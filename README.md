# Attack Vectors

A repository to monitor attack vectors mentioned in the [billion-dollar disinformation campaign to reelect the president in 2020](https://www.theatlantic.com/magazine/archive/2020/03/the-2020-disinformation-war/605530/)

## Local Journalism

>Parscale has indicated that he plans to open up a new front in this war: local news. Last year, he said the campaign intends to train “swarms of surrogates” to undermine negative coverage from local TV stations and newspapers. Polls have long found that Americans across the political spectrum trust local news more than national media. If the campaign has its way, that trust will be eroded by November.

>Running parallel to this effort, some conservatives have been experimenting with a scheme to exploit the credibility of local journalism. Over the past few years, hundreds of websites with innocuous-sounding names like the Arizona Monitor and The Kalamazoo Times have begun popping up. At first glance, they look like regular publications, complete with community notices and coverage of schools. But look closer and you’ll find that there are often no mastheads, few if any bylines, and no addresses for local offices. Many of them are organs of Republican lobbying groups; others belong to a mysterious company called Locality Labs, which is run by a conservative activist in Illinois. Readers are given no indication that these sites have political agendas—which is precisely what makes them valuable.

Findings:

|awsOrigin|domain|facebookUrl|facebookSiteName|facebookFollowers|twitterUrl|twitterFollowers|
|:-----------|:-----------|:------------|:------------|:------------|------------|------------|
|3.218.216.245|annarbortimes.com	|https://business.facebook.com/Ann-Arbor-Times-105059500884218/?business_id=898179107217559|Ann Arbor Times| 43|
|3.218.216.245|battlecreektimes.com|https://business.facebook.com/Battle-Creek-Times-101371024590467/?business_id=898179107217559|Battle Creek Times| 16 |
|52.7.148.177|wvrecord.com|https://www.facebook.com/WVRecord|West Virginia Record|3986|https://twitter.com/wvrecord|3990|
|52.7.148.177setexasrecord.com|https://www.facebook.com/SETexasRecord/|Southeast Texas Record|1285|	https://twitter.com/setexasrecord|1136|

But wait, there's [700+ more with 270+ with Facebook pages and thousands of Facebook accounts](https://github.com/MassMove/AttackVectors/blob/master/LocalJournals/sites.csv).
- https://kalamazootimes.com

Their shit looks really real: https://kalamazootimes.com until you start looking at all the articles at once: https://kalamazootimes.com/stories/tag/126-politics

Some quick Google-fu with a sentence from their about page:
https://www.google.com/search?q=%22Metric+Media+was+established+to+fill+the+void+in+community+news+after+years+of+decline+in+local+reporting+by+legacy+media.%22&rlz=1C1GCEU_nlNL823NL823&filter=0

## Legal Findings

https://www.fec.gov/files/legal/murs/7148/19044475209.pdf

[Legal Findings](https://github.com/MassMove/AttackVectors/blob/master/LocalJournals/README.md)

## Twitter

>But when Twitter employees later reviewed the activity surrounding Kentucky’s election, they concluded that the bots were largely based in America—a sign that political operatives here were learning to mimic [foreign tactics].

From the Twitter Transparency Report:

| Date     | Country  | Msg Info  | Media | Accounts |
|:-----------|:-----------:|:------------:|:------------:|------------:|
| 201906|Catalonia |1.5 MB|2.74 GB|130 |
| 201906|Iran|316 MB|258 GB|1,666 |
| 201906|Iran|318 MB|183 GB|248 |
| 201906|Iran|46 MB|55 GB|2,865 |
| 201906|Russia|260 KB|72 MB|4|
| 201906|Venezuela |64 MB|24 GB|33 |
| 201906|China |158 MB|85 GB|744  |
| 201906|China |169 MB|40 GB|196 |
| 201906|China |913 MB|604 GB|4,301| 
| 201910|Saudi Arabia |4.3 GB|1.3 TB|5,929|

[12 more in the war room with further sources](https://www.reddit.com/r/MassMove/wiki/warroom)

## Websites resembling official campaigns

>Last year, a website resembling an official Biden campaign page appeared on the internet. It emphasized elements of the candidate’s legislative record likely to hurt him in the Democratic primary—opposition to same-sex marriage, support for the Iraq War—and featured video clips of his awkward encounters with women. The site quickly became one of the most-visited Biden-related sites on the web. It was designed by a Trump consultant.

Nothing to report on this front yet. Scouts?